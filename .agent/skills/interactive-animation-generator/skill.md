---
name: interactive-animation-generator
display_name: Interactive Animation Generator
description: Use this skill to create a browser-based interactive mathematical animation as a single HTML file with no external dependencies. Trigger for interactive animation, math visualization, HTML animation, browser demo, or concept animation.
trigger_keywords:
  - interactive animation
  - math visualization
  - HTML animation
  - browser demo
  - concept animation
slash_command: interactive-animation-generator
---

# Interactive Animation Generator

Build single-file interactive animations for mathematical concepts.

## Workflow

1. Choose one key concept from the lecture.
2. Map the concept to a visible state:
   - points moving on a graph;
   - vectors or arrows changing;
   - contours, grids, or basis functions;
   - algorithm steps.
3. Write one standalone HTML file with embedded CSS and JavaScript.
4. Include controls that match the concept:
   - Start or Pause;
   - Step;
   - Reset;
   - speed or parameter slider.
5. Add labels, captions, and numerical state readouts.
6. Avoid external CDN dependencies unless the user explicitly asks for them.

## Verification

Open the HTML file in a browser or headless browser and check that:

- the page loads without JavaScript errors;
- the visual scene is nonblank;
- controls exist and update the state;
- labels and formulas fit on desktop and mobile widths.

Record the verification method when submitting coursework.
