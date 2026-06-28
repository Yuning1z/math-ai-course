# Capstone Reflection

## 1. How did your workflow change during this course?

Before this course, my usual workflow for a math topic was linear: read notes,
copy definitions, solve a few examples, and only later try to organize the
topic into a coherent guide. The AI-assisted workflow made the process more
iterative. For this capstone, I started from the Week 4 Math Tutor skill,
expanded the output contract, and used it as a checklist while building the
Sobolev-space study guide. The before/after difference is concrete: instead of
writing isolated notes on weak derivatives and Lax-Milgram, I built a guide
with definitions, examples, practice problems, numerical experiments, and
connections all in one pass.

Another change is that I now document the process more carefully. In Week 6,
for example, I had to record exact Zotero and NotebookLM queries rather than
just keep the answers. That habit carried into the capstone: the refined skill
is not only a prompt, but a reusable workflow that says what a good graduate
math explanation should contain.

## 2. What could the AI tools not do well?

The tools were weakest when they had to verify external state or hidden
configuration. During Week 6, Zotero MCP was installed correctly, but the
first checks failed because the local API was not visible from the sandboxed
environment. I had to distinguish between "Zotero is not running" and "the
tool is looking at the wrong localhost." Similarly, NotebookLM required manual
Google login and PDF upload; AI could guide and document the workflow, but it
could not replace the browser authentication step.

For the math content, AI also needed guardrails. A generic study guide prompt
tends to produce plausible explanations but may skip assumptions such as
bounded Lipschitz domain, the role of $H_0^1$, or the exact norm controlled by
coercivity. I had to refine the skill so it explicitly tracks spaces, norms,
boundary conditions, and theorem hypotheses.

## 3. Which single skill or agent feature had the biggest impact?

The most useful feature was the ability to turn a successful workflow into a
skill. The Week 4 Math Tutor skill started as a general tutoring prompt, but
the capstone forced me to make it more precise: it now requires proof
standards, capstone-scale examples, practice problems, and computational
illustrations. That changed the AI from a one-shot answer generator into a
repeatable study-guide builder.

The impact was largest because the same skill controlled both the mathematical
writing and the computation design. For example, the Python file does not just
solve a finite element problem; it reports errors, convergence rates,
Poincare constants, and energy descent, each tied back to the theory in the
guide.

## 4. What would you build or automate next?

Next I would build a "PDE problem lab" skill that takes a boundary value
problem and automatically produces four linked artifacts: a weak formulation,
a well-posedness proof checklist, a finite-dimensional discretization, and a
small numerical experiment. This would be useful because many graduate PDE and
numerical analysis problems follow the same pattern, but the details change
enough that careless automation can be misleading.

I would also add validation steps to that skill. For example, it should check
whether Poincare's inequality is valid in the chosen function space, whether a
Neumann problem needs a compatibility condition, and whether the stiffness
matrix has a nullspace. Those checks would directly address the places where
AI tools tend to sound confident while silently skipping the condition that
actually matters.
