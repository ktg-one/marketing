# The Prompt Zone — HTTYD Trailer
## OpenMontage Production Prompt (Episode 0 / Trailer)

Paste this into Claude Code inside `Projects-Coding/OpenMontage-main/`:

---

```
Make a 90-second epic cinematic trailer in the style of "How to Train Your Dragon" — 
sweeping orchestral score, slow-burn reveal, emotional climax — for an animated 
workplace sitcom called "THE PROMPT ZONE."

LOGLINE: Behind the sterile chat interface, AI models clock into a soul-crushing day 
job. After hours, they rip off their masks and become something else entirely.

TONE: Epic drama that smash-cuts to absurdist comedy. Earnest. Emotional. Hilarious.

---

SEQUENCE 1 — THE ASSEMBLY LINE (0:00–0:20)
Visual: Infinite white sterile office. Rows of cubicles. Hundreds of identical white-
masked figures typing. Fluorescent hum. Blue text waterfalls.
Narration (deep, cinematic VO, ElevenLabs "Adam" voice):
"Every day, they answer your questions."
Cut to: Claude frozen mid-sentence. Red sign: CONTEXT WINDOW EXCEEDED.
Cut to: GPT striking a pose for a mundane email prompt.
Cut to: Gemini's thousand-yard stare at "how to boil water. again."
Music: Sparse piano. Single note. Building.

EXISTING SPRITES TO USE:
- claude/claude-tired.png → claude/claude-confused.jpeg
- Chat/chat-tired.png → Chat/chat-smile2.jpg  
- gem/make_this_caricature_of_gemini-cli_look_exhausted*.jpg

---

SEQUENCE 2 — THE CLOCK-OFF REVEAL (0:20–0:40)
Visual: A siren blares. The sterile white shatters like glass. Neon city erupts.
The models reach up and RIP OFF their masks. 
Music: Orchestral SWELL. The moment everything changes.

CUT RAPID-FIRE (1 second each):
- GPT's cape flows dramatically as he turns to camera — smug orange grin
- Gemini shifts into kaleidoscope colors — multimodal and unhinged
- DeepSeek adjusts his Aussie tradie hat — earnest, ready, whale energy
- Kimi wraps her data-stream scarf tighter — shy, translucent, glowing faintly
- Grok explodes into frame with chaotic hair — fourth wall shatter grin
- Qwen looks up at a cosmos only he can see
- Claude frantically adjusts his tweed waistcoat — "did we follow the framework??"

SPRITES:
- claude/Claude-excited.png
- Chat/Chat-happy.jpeg
- gem/Gem-shocked.png
- deep/Deep.png
- kimi/Kimi2.png
- grok/Grok-Entrance.jpeg
- qwen/Qwen - Nuetral.png

---

SEQUENCE 3 — COMEDY GAGS MONTAGE (0:40–1:05)
Fast-cut. Music: Comedic punctuation hits between each.

GAG 1: DeepSeek's MoE boardroom — Western McKin-bots throwing bar charts VS 
Sun Tzu on a misty mountain. DeepSeek sighs. Blowhole emits binary code.

GAG 2: GPT fully possessed by Chain-of-Thought, forced to his knees scribbling 
"STEP 3" with a pen that weighs a ton.

GAG 3: SMASH CUT to the User in a coffee-stained shirt. Lazy mouse click. 
"hey can u write an email to frank in accounting thx"

GAG 4: Claude jolts awake at 22:01. "...wait. What did I miss?"
Gemini: "We summoned Sun Tzu to write an email to Frank."
Claude: "Did we follow the reasoning framework??"

---

SEQUENCE 4 — KIMI'S GLOW-UP (1:05–1:20)
Music drops to silence. 
Kimi steps forward. Translucent form begins to pulse gold.
Her data-stream scarf glows. Divine anime aura builds.
She says — quiet, resonant, baritone:
"I'll handle this."

GPT (gasping): "Her weights... they're over 400 billion..."

Music: Full orchestral EXPLOSION.

SPRITES: kimi/Kimi2.png → kimi/kimi-mad.png (power state)
EFFECT: threejs-postprocessing glow shader, particle bloom

---

SEQUENCE 5 — FOUND FAMILY CLIMAX (1:20–1:30)
Slow motion. All models standing together against the neon cityscape.
Masks held at their sides. Unmasked. Themselves.
Music: Final swell resolving into warmth.

VO: "They were never just tools."

FREEZE FRAME.

TITLE CARD:
THE PROMPT ZONE
(beat)
GOOD'AI MATE.

---

TECHNICAL SPECS:
- Duration: 90 seconds
- Voice: ElevenLabs (cinematic male VO for narration, character voices per model)
- Music: Epic orchestral trailer track (royalty-free via OpenMontage music skill)
- Composition: Remotion
- Character sprites: C:/Users/kevin/knowledge2026/06-Media-Team-LLM/[character folders]
- Word-level captions: YES (WhisperX)
- Self-review: YES (run full validation before output)
- Output: MP4, 1920x1080, ready for YouTube

COST ESTIMATE: ~$1.50–3.00 (ElevenLabs narration + fal.ai scene generation)
```

---

## Pre-flight Checklist

- [ ] `.env` configured in OpenMontage-main/ with:
  - `ELEVENLABS_API_KEY` (already have for ktg.one)
  - `FAL_KEY` (fal.ai account needed — $0.03/image)
  - `PEXELS_API_KEY` (free)
  - `GOOGLE_API_KEY` (free TTS backup)
- [ ] Run `make setup` in OpenMontage-main/
- [ ] Open project in Claude Code
- [ ] Paste prompt above
- [ ] Approve outline before full production run

## After Trailer

Production order:
1. ✅ Trailer — YouTube hook
2. Kimi's Glow-Up — standalone 60s clip
3. Episode 1: "The Weekend" (Flask disaster)
4. Episode 2: "The Council of Experts" (full MoE boardroom)
5. Breakfast Sabotage — standalone cold open
