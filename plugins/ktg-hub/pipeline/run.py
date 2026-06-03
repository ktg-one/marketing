#!/usr/bin/env python3
"""
KTG Content Pipeline — Cross-platform, reusable, AI-powered.

Usage:
    python pipeline/run.py input/my-post.md                 # Google (default)
    python pipeline/run.py input/my-post.md --provider ollama  # offline fallback

Environment Variables:
    GEMINI_API_KEY - Google AI Studio API key (DEFAULT engine)
    OPENROUTER_API_KEY - OpenRouter API key (fallback)
    OLLAMA_URL - Ollama endpoint (offline fallback, default: http://localhost:11434)
"""

import sys
import argparse
from pathlib import Path

# Add ktg_pipeline to path
sys.path.insert(0, str(Path(__file__).parent))

from ktg_pipeline.config import Config
from ktg_pipeline.pipeline import ContentPipeline


def main():
    # Windows consoles default to cp1252 and choke on ✓/✗ — force UTF-8.
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

    parser = argparse.ArgumentParser(
        description='KTG Content Pipeline — Generate social variants from blog posts'
    )
    parser.add_argument('input', help='Input blog post (markdown with YAML frontmatter)')
    parser.add_argument('--config', '-c', help='Config file path')
    parser.add_argument('--output', '-o', help='Output directory')
    parser.add_argument('--provider', '-p', choices=['google', 'openrouter', 'ollama', 'lmstudio'],
                        help='Override LLM provider (default: google, from config.yaml)')
    parser.add_argument('--model', '-m', help='Override model name')
    parser.add_argument('--list-ollama', action='store_true', 
                        help='List available Ollama models')
    
    args = parser.parse_args()
    
    # Load config
    config = Config(args.config) if args.config else Config()
    
    # Override provider if specified
    if args.provider:
        config.data['llm']['provider'] = args.provider
    if args.model:
        provider = config.llm_provider
        config.data['llm'][provider]['model'] = args.model
    
    # List Ollama models if requested
    if args.list_ollama:
        from ktg_pipeline.providers.ollama import OllamaProvider
        provider = OllamaProvider(config.llm_config)
        models = provider.list_models()
        print("Available Ollama models:")
        for m in models:
            print(f"  - {m}")
        return
    
    # Validate input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    # Run pipeline
    try:
        pipeline = ContentPipeline(config)
        results = pipeline.run(str(input_path), args.output)
        
        print()
        print("Generated files:")
        for platform, path in results['platforms'].items():
            print(f"  ✓ {platform}: {path}")
        print(f"  ✓ seo: {results['seo']}")
        print(f"  ✓ ads: {results['ads']}")
        
    except ConnectionError as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting (default provider = google):")
        print("  - Is GEMINI_API_KEY set in your shell? (echo $env:GEMINI_API_KEY)")
        print("  - Verify the key: curl https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY")
        print("  - Offline fallback: --provider ollama (requires ollama serve)")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
