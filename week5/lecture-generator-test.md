# Lecture Generator Test

## Test Prompt

```text
/lecture-generator Build a short graduate lecture package on the Banach fixed point theorem.
```

## Confirmed Skill Behavior

The `lecture-generator` skill is appropriate for this prompt because it asks for
a full lecture package on a topic different from the Week 5 lecture. The
coordinator should route the work through:

- `marp-slide-generator` for the slide deck;
- `remotion-video-generator` for narration and Remotion structure;
- `interactive-animation-generator` for a browser animation.

## Sample Coordinated Output Summary

Topic: Banach Fixed Point Theorem

Audience: graduate analysis or applied mathematics students.

Core lecture plan:

1. Motivate contraction mappings by iterative solution of nonlinear equations.
2. Define complete metric spaces and contractions.
3. State Banach's fixed point theorem with constants.
4. Prove convergence by showing the iterates form a Cauchy sequence.
5. Derive the a priori and a posteriori error estimates.
6. Connect the theorem to Picard iteration for ODEs and nonlinear PDE methods.
7. Build an animation of iterates moving toward a fixed point on the real line.

This confirms that the coordinator skill generalizes beyond the conjugate
gradient lecture topic.
