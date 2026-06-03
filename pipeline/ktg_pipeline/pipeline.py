"""Main pipeline orchestrator."""

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

from .config import Config
from .providers.ollama import OllamaProvider
from .providers.google import GoogleProvider
from .providers.lmstudio import LMStudioProvider
from .providers.openrouter import OpenRouterProvider


class ContentPipeline:
    """KTG Content Pipeline — reusable, AI-powered."""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.llm = self._init_llm()
        self.voice_system = self._load_voice_system()

    def _load_voice_system(self) -> Optional[str]:
        """Load the Myth-Hilarity house voice system prompt once.

        Robust: if blog/user_voice.md is missing, return None and proceed
        (calls fall back to system=None, i.e. no voice injection).
        """
        voice_path = Path('blog/user_voice.md')
        try:
            return voice_path.read_text(encoding='utf-8')
        except OSError as e:
            # Signal the regression: locked-voice brand + no test suite means a
            # silently-missing voice file would ship generic prose unnoticed.
            print(f"[warn] House voice not loaded ({voice_path}): {e} — prose will be generic.")
            return None

    def _init_llm(self):
        """Initialize LLM provider based on config."""
        provider = self.config.llm_provider
        llm_config = self.config.llm_config
        
        if provider == 'ollama':
            return OllamaProvider(llm_config)
        elif provider == 'lmstudio':
            return LMStudioProvider(llm_config)
        elif provider == 'google':
            return GoogleProvider(llm_config)
        elif provider == 'openrouter':
            return OpenRouterProvider(llm_config)
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")
    
    def parse_input(self, input_path: str) -> Dict[str, Any]:
        """Parse blog post with YAML frontmatter."""
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter = {}
        body = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                import yaml
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
        
        # Extract slug
        slug = frontmatter.get('slug', Path(input_path).stem)
        
        return {
            'frontmatter': frontmatter,
            'body': body,
            'slug': slug,
            'title': frontmatter.get('title', 'Untitled'),
            'topic': frontmatter.get('topic', ''),
            'tone': frontmatter.get('tone', 'professional'),
            'audience': frontmatter.get('target_audience', 'general'),
            'call_to_action': frontmatter.get('call_to_action', ''),
            'key_points': frontmatter.get('key_points', [])
        }
    
    def run(self, input_path: str, output_dir: str = None) -> Dict[str, Any]:
        """Run full pipeline."""
        # Parse input
        post = self.parse_input(input_path)
        slug = post['slug']
        
        # Setup output directories
        if output_dir is None:
            output_dir = f"pipeline/output/{slug}"
        
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        
        results = {
            'slug': slug,
            'input': input_path,
            'output_dir': str(out_path),
            'platforms': {},
            'seo': None,
            'ads': None,
            'images': {}
        }
        
        print(f"=== KTG Pipeline: {slug} ===")
        print(f"LLM Provider: {self.config.llm_provider}")
        print(f"Model: {self.config.llm_config.get('model', 'unknown')}")
        print()
        
        # Build the list of stages to run. Each entry is a (name, fn) pair;
        # `name` keys the result back into `results`. The 5 repurpose stages are
        # gated by their per-platform `enabled` flag (default True), matching the
        # previous sequential behaviour exactly.
        platforms = self.config.platforms

        repurpose_stages = [
            ('medium', self._repurpose_medium),
            ('reddit', self._repurpose_reddit),
            ('x', self._repurpose_x),
            ('linkedin', self._repurpose_linkedin),
            ('meta', self._repurpose_meta),
        ]

        # name -> (callable, result-assignment key). Platform stages land in
        # results['platforms'][name]; seo/ads/images are top-level keys.
        stages = []
        for name, fn in repurpose_stages:
            if platforms.get(name, {}).get('enabled', True):
                stages.append(('platform', name, fn))
        stages.append(('top', 'seo', self._generate_seo))
        stages.append(('top', 'ads', self._generate_ads))
        stages.append(('top', 'images', self._generate_image_prompts))

        # Stages are independent (each takes (post, out_path), writes its own
        # distinct file, returns its own value, shares no mutable state), so run
        # them concurrently. Work is I/O-bound HTTP via requests -> threads.
        print(f"Running {len(stages)} stages concurrently...")
        with ThreadPoolExecutor(max_workers=8) as executor:
            future_map = {
                executor.submit(fn, post, out_path): (kind, name)
                for kind, name, fn in stages
            }
            for future in as_completed(future_map):
                kind, name = future_map[future]
                try:
                    value = future.result()
                except Exception as e:
                    # Per-stage error isolation: one failing stage must not abort
                    # the rest. Record it and move on (None / omit from platforms).
                    print(f"[error] {name}: {e}")
                    if kind == 'top':
                        # leave the pre-seeded default (None for seo/ads, {} for images)
                        pass
                    # platform stages: omit on failure (key simply not added)
                    continue
                if kind == 'platform':
                    results['platforms'][name] = value
                else:
                    results[name] = value
                print(f"[done] {name}")

        # Save manifest
        manifest_path = out_path / 'manifest.json'
        with open(manifest_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print()
        print(f"=== Complete ===")
        print(f"Output: {out_path}")
        print(f"Files: {len(list(out_path.glob('*.md')))}")
        
        return results
    
    def _repurpose_medium(self, post: Dict, out_path: Path) -> str:
        """Repurpose for Medium."""
        prompt = f"""Repurpose this blog post for Medium.

Original Title: {post['title']}
Content:
{post['body'][:2000]}...

Requirements:
- Full article format
- Clean markdown
- Professional tone
- Keep key points but expand slightly
- Add Medium-appropriate formatting
- End with: "Originally published on [KTG](https://ktg.one)"

Output only the repurposed article, no explanations."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'medium.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\nplatform: medium\nsource: {post['slug']}\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _repurpose_reddit(self, post: Dict, out_path: Path) -> str:
        """Repurpose for Reddit."""
        prompt = f"""Repurpose this blog post for Reddit discussion.

Title: {post['title']}
Key Points:
{chr(10).join(f"- {p}" for p in post['key_points'])}

Requirements:
- Conversational, not promotional
- Start with "I know this sounds like [hook] but..."
- Present key insight as a question/discussion
- End with engaging question for comments
- Keep it under 2000 characters
- No emojis, Reddit doesn't like them

Output only the Reddit post text."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'reddit.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\nplatform: reddit\nsource: {post['slug']}\n---\n\n")
            f.write(content)
            if post['call_to_action']:
                f.write(f"\n\n{post['call_to_action']}")
        
        return str(output_file)
    
    def _repurpose_x(self, post: Dict, out_path: Path) -> str:
        """Repurpose for X/Twitter thread."""
        prompt = f"""Create an X/Twitter thread from this blog post.

Title: {post['title']}
Key Points:
{chr(10).join(f"- {p}" for p in post['key_points'])}

Requirements:
- 8 posts in the thread
- Each post under 280 characters
- Numbered 1/, 2/, etc.
- Post 1: Hook (attention-grabbing)
- Posts 2-5: Key insights
- Post 6-7: Evidence/examples
- Post 8: CTA + hashtags
- Each post should standalone (people see it in isolation)

Output format:
1/ [text]
2/ [text]
etc."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'x-thread.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\nplatform: x\nsource: {post['slug']}\ntype: thread\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _repurpose_linkedin(self, post: Dict, out_path: Path) -> str:
        """Repurpose for LinkedIn."""
        prompt = f"""Repurpose this blog post for LinkedIn professional article.

Title: {post['title']}
Key Points:
{chr(10).join(f"- {p}" for p in post['key_points'])}

Requirements:
- Professional, thought leadership tone
- Use bold headers for sections
- Bullet points for readability
- No emojis (LinkedIn professional)
- Structure: Hook → Data → Analysis → Framework → CTA
- 1500-2000 characters
- End with hashtags

Output only the LinkedIn post text."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'linkedin.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\nplatform: linkedin\nsource: {post['slug']}\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _repurpose_meta(self, post: Dict, out_path: Path) -> str:
        """Repurpose for Meta/Facebook."""
        prompt = f"""Repurpose this blog post for Meta/Facebook casual post.

Title: {post['title']}
Key Points:
{chr(10).join(f"- {p}" for p in post['key_points'])}

Requirements:
- Casual, friendly tone
- Heavy emoji use (✅ 🚨 👇)
- Short paragraphs
- Numbered list with emoji
- Question at end to drive engagement
- Under 1500 characters
- Image required (note this)

Output only the Facebook post text."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'meta.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\nplatform: meta\nsource: {post['slug']}\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _generate_seo(self, post: Dict, out_path: Path) -> str:
        """Generate SEO package."""
        prompt = f"""Generate SEO metadata for this blog post.

Title: {post['title']}
Topic: {post['topic']}
Key Points: {', '.join(post['key_points'])}

Generate:
1. Title tag (under 60 chars)
2. Meta description (under 160 chars)
3. 5 target keywords with priority
4. Open Graph title/description
5. Twitter Card title/description
6. Schema.org JSON-LD (Article type)

Output as structured markdown."""

        # Voice deliberately skipped: SEO output contains length-capped title/meta
        # tags and Schema.org JSON-LD — house-voice prose would blow char limits
        # and corrupt the structured/JSON output.
        content = self.llm.generate(prompt)

        output_file = out_path / 'seo.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntype: seo\nsource: {post['slug']}\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _generate_ads(self, post: Dict, out_path: Path) -> str:
        """Generate ads package."""
        prompt = f"""Generate ad copy for this blog post.

Title: {post['title']}
Key Points: {', '.join(post['key_points'])}
Audience: {post['audience']}

Generate for:
1. Google Search Ads (3 headlines, 2 descriptions)
2. Meta Ads (primary text, headline, CTA)
3. LinkedIn Ads (sponsored content text)

Output as structured markdown."""

        content = self.llm.generate(prompt, system=self.voice_system)
        
        output_file = out_path / 'ads.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntype: ads\nsource: {post['slug']}\n---\n\n")
            f.write(content)
        
        return str(output_file)
    
    def _generate_image_prompts(self, post: Dict, out_path: Path) -> Dict[str, str]:
        """Generate image generation prompts."""
        images = {}
        
        # Hero image
        prompt = f"""Create a detailed image generation prompt for this blog post header.

Title: {post['title']}
Topic: {post['topic']}
Tone: {post['tone']}

Requirements:
- Aspect ratio 16:9
- Bold editorial style
- Dark background with neon accents
- Abstract/tech aesthetic
- Include specific colors, composition, mood

Output only the prompt text (for image generator)."""

        # Voice deliberately skipped: this produces a literal image-generator
        # prompt (visual composition spec), not house prose — narrative voice
        # would derail the concrete visual directives.
        hero_prompt = self.llm.generate(prompt)
        images['hero'] = hero_prompt
        
        # Save all prompts
        output_file = out_path / 'image-prompts.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ntype: image-prompts\nsource: {post['slug']}\n---\n\n")
            f.write("## Hero Image (16:9)\n\n")
            f.write(hero_prompt)
            f.write("\n\n## LinkedIn Image (1.91:1)\n\n")
            f.write("[Use similar style, professional, data-focused]\n")
            f.write("\n\n## X Image (2:1)\n\n")
            f.write("[Bold, high contrast, scroll-stopping]\n")
            f.write("\n\n## Square Image (1:1)\n\n")
            f.write("[Icons, educational, carousel-friendly]\n")
        
        return images
