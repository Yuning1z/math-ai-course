---
name: lecture-generator
display_name: Lecture Generator
description: Coordinate lecture package creation for math topics: lecture plan, Marp slides, Remotion narrated video workflow, and interactive HTML animation. Use this skill when the user asks for a full lecture package, Week 5 style assignment, or slash command /lecture-generator.
trigger_keywords:
  - lecture generator
  - lecture package
  - full lecture
  - Week 5 lecture
  - teaching package
slash_command: lecture-generator
coordinated_skills:
  - marp-slide-generator
  - remotion-video-generator
  - interactive-animation-generator
---

# Lecture Generator

Coordinate a complete math lecture package.

## Inputs

Accept a topic, audience level, and any constraints. If the audience is missing,
choose a reasonable level and state it. For graduate math topics, prefer precise
notation and theorem-level structure; for undergraduate topics, prefer more
examples and visual intuition.

## Coordinated Workflow

1. **Lecture plan**
   - Create a one-page plan with topic, target audience, lecture goal, and 5-7
     key points.
   - Use the plan as the source of truth for later artifacts.

2. **Slides**
   - Follow the Marp Slide Generator skill.
   - Generate a Marp deck with at least 8 slides.
   - Refine for structure, notation, and audience level.

3. **Narrated video**
   - Follow the Remotion Video Generator skill.
   - Create a narration script.
   - Create a Remotion project with comment-driven composition code.
   - Add an `edge-tts` audio generation script and render command.

4. **Interactive animation**
   - Follow the Interactive Animation Generator skill.
   - Build one standalone HTML animation for the most visual concept in the
     lecture.
   - Verify the file opens in a browser or headless browser.

5. **Submission notes**
   - Record refinement rounds, dependency limitations, and test prompts.
   - Keep generated files organized under the requested week folder.

## Test Prompt Used

The skill was tested conceptually with a different topic from the Week 5
lecture:

```text
/lecture-generator Build a short graduate lecture package on the Banach fixed point theorem.
```

Expected output: a lecture plan, Marp slide deck, Remotion narration/video
workflow, and interactive animation prompt focused on contraction maps rather
than conjugate gradient.
