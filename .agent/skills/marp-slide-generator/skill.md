---
name: marp-slide-generator
display_name: Marp Slide Generator
description: Use this skill to turn a lecture plan, study guide, or topic outline into a polished Marp slide deck with consistent mathematical notation, audience-appropriate pacing, and refinement rounds. Trigger for Marp slides, lecture slides, slide deck generation, markdown slides, or presentation refinement.
trigger_keywords:
  - Marp slides
  - lecture slides
  - slide deck
  - markdown slides
  - presentation refinement
slash_command: marp-slide-generator
---

# Marp Slide Generator

Create mathematical Marp slide decks from a lecture plan or topic outline.

## Workflow

1. Identify the target audience and expected mathematical background.
2. Extract the main narrative from the lecture plan.
3. Choose 8-14 slides unless the user requests another length.
4. Use Marp frontmatter:

```yaml
---
marp: true
theme: default
paginate: true
math: katex
---
```

5. Keep notation consistent across slides.
6. Define all central symbols before using them.
7. Use displayed equations for important formulas.
8. Refine at least twice:
   - first for structure and audience level;
   - second for notation, slide density, and mathematical accuracy.

## Slide Shape

Prefer this sequence for math lectures:

- title and audience;
- motivating problem;
- central definition or model;
- core theorem or method;
- worked formula or algorithm;
- geometric or conceptual interpretation;
- convergence, limitation, or caveat;
- takeaway slide.

## Quality Checks

- Minimum slide count has been met.
- No slide is overloaded with paragraphs.
- Every theorem or formula has the assumptions needed to interpret it.
- The final deck can render in Marp with KaTeX.
