---
name: remotion-video-generator
display_name: Remotion Video Generator
description: Use this skill to create a Remotion lecture video project from slides or a lecture plan, including a narration script, comment-driven React composition, and edge-tts narration workflow. Trigger for Remotion videos, narrated lecture videos, edge-tts narration, or comment-driven video generation.
trigger_keywords:
  - Remotion video
  - narrated lecture
  - edge-tts
  - video generation
  - comment-driven video
slash_command: remotion-video-generator
---

# Remotion Video Generator

Create a reproducible Remotion project for a short narrated math lecture.

## Workflow

1. Read the lecture plan or final slides.
2. Break the lecture into scenes: title, motivation, definitions, main method,
   example or visualization, convergence or caveat, closing.
3. Write a narration script in plain language.
4. Create a Remotion project with:
   - `package.json`;
   - `remotion.config.ts`;
   - `src/index.ts`;
   - `src/Root.tsx`;
   - a main composition component;
   - an `edge-tts` narration generation script.
5. Use comments in the composition to describe intended visual behavior before
   writing React/Remotion code.
6. Keep visuals mathematical: formulas, arrows, diagrams, contours, timelines,
   or algorithm states.
7. Include scripts for:
   - generating narration audio;
   - opening Remotion Studio;
   - rendering an MP4.

## edge-tts Pattern

Use an audio generation script that reads a narration markdown file, removes
Markdown headings and math markup where needed, then calls:

```bash
edge-tts --voice en-US-JennyNeural --text "..." --write-media narration.mp3 --write-subtitles narration.vtt
```

If `edge-tts` is not installed, report the install command instead of silently
failing.

## Quality Checks

- The video project is self-contained inside the assignment folder.
- The narration script matches the scenes.
- The render script has a clear output path.
- Missing dependencies are documented honestly.
