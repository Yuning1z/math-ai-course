# Week 5 Process Notes

## Slide Generation Skill Test

Prompt pattern tested:

```text
/marp-slide-generator Generate graduate-level Marp slides from week5/lecture-plan.md.
```

Result recorded: the final slide deck in `week5/slides.md` follows the lecture
plan, uses consistent notation, defines the $A$-norm, and has 12 slides.

## Video Generation Workflow Notes

Comment-driven Copilot workflow used for the Remotion project:

1. Add comments describing the composition: title card, energy surface,
   residual-as-gradient, conjugate directions, Krylov subspace, convergence.
2. Ask Copilot Chat to fill in React/Remotion components matching those
   comments.
3. Add narration comments and generate `week5/narration-script.md`.
4. Add an `edge-tts` script that converts the narration to audio when
   `edge-tts` is installed.
5. Add a Remotion render script that can produce `week5/remotion/out/cg-energy.mp4`
   after dependencies are installed.

Rendered assets:

- `week5/remotion/public/narration.mp3`
- `week5/remotion/public/narration.vtt`
- `week5/remotion/out/cg-energy.mp4`

Verification commands used:

```text
npm install --ignore-scripts
PYTHONPATH=/tmp/week5-edge-tts PATH=/tmp/week5-edge-tts/bin:$PATH npm run generate:narration
npm run render
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 week5/remotion/out/cg-energy.mp4
```

The rendered MP4 duration is about 120 seconds.

## Animation Verification

The animation file is `week5/animation.html`.

Verification target:

```text
Open the file in a browser and confirm that Start, Reset, speed control, and
step-by-step CG movement work.
```

Automated smoke check performed locally:

```text
google-chrome --headless --disable-gpu --no-sandbox --dump-dom week5/animation.html
```

The browser load succeeded and showed the generated SVG scene, controls, and
initial CG state.

## Lecture Generator Skill Test

Test prompt on a different topic from the Week 5 lecture:

```text
/lecture-generator Build a short graduate lecture package on the Banach fixed point theorem.
```

Expected behavior: the coordinator skill should call for a lecture plan, Marp
slide deck, Remotion narration/video workflow, and interactive animation prompt
using the three process skills.
