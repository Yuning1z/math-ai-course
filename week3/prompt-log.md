# Week 3 Prompt Log

Topic chosen: Fourier series.

This topic is different from Week 1, which covered Sobolev spaces.

Prompting tool recorded for this assignment: Copilot Chat in Ask mode.

## Prompt Entry 1

### Exact prompt sent

Create a Marp slide deck explaining Fourier series for an undergraduate math class.

### Summary of the output

The output produced a short Marp deck with a title slide, a definition of Fourier
series, a slide about sine and cosine waves, a formula for coefficients, and a
brief closing slide about applications.

### Specific problems noticed

- The deck was too generic: it said Fourier series "break functions into waves"
  but did not clearly state the interval, assumptions, or coefficient formulas.
- The mathematical notation was inconsistent, sometimes using $f(x)$ and
  sometimes using $g(t)$ without explanation.
- It had no concrete worked example, so the audience would see the formulas but
  not how they are used.

### Critique before the next prompt

The first version was a reasonable outline, but it read more like a quick
definition sheet than a teachable slide deck. The next prompt needs to ask for a
specific audience, a specific structure, consistent notation, and an example.

## Prompt Entry 2

### Exact prompt sent

Revise the Fourier series Marp deck for a 10-minute undergraduate presentation on functions on [-pi, pi]; use consistent notation f(x), include the real sine-cosine coefficient formulas, and add one worked example.

### What I was trying to fix

I wanted to fix the vague scope, inconsistent notation, missing coefficient
definitions, and lack of an example.

### Summary of the output

The revised output gave a clearer 10-slide deck. It stated the real Fourier
series on $[-\pi,\pi]$, included formulas for $a_0$, $a_n$, and $b_n$, and added
an example for $f(x)=x$. It also included an applications slide.

### What improved

- The notation became consistent: the deck used $f(x)$ throughout.
- The coefficient formulas were now explicit.
- The example made the abstract formula more concrete.

### What is still wrong

- The convergence slide was too casual and implied the Fourier series always
  equals the function at every point.
- The example for $f(x)=x$ skipped the symmetry argument and jumped directly to
  the final answer.
- There was still no slide explaining why orthogonality makes the coefficient
  formulas work.

### Critique before the next prompt

The second version became more mathematically useful, but it risked teaching a
false statement about pointwise convergence. It also needed a conceptual bridge:
students should see that the formulas come from orthogonality, not magic.

## Prompt Entry 3

### Exact prompt sent

Revise the deck again: add a slide explaining orthogonality of sine and cosine on [-pi, pi], make the convergence statement precise at jump discontinuities, and expand the f(x)=x example by showing why only sine terms remain.

### What I was trying to fix

I wanted to correct the overstatement about convergence, explain the role of
orthogonality, and make the example easier to follow.

### Summary of the output

The output added an orthogonality slide, rewrote the convergence slide to say
that the Fourier series converges to the midpoint of the left and right limits
at a jump, and expanded the $f(x)=x$ example by noting that $x$ is odd and
therefore has no cosine terms.

### What actually changed in the output

- Orthogonality was named as the reason coefficients can be isolated.
- The convergence statement became more accurate and mentioned midpoint values
  at jumps.
- The example now explained why $a_0=a_n=0$ for an odd function.

### What is still wrong

- The deck was text-heavy in several places, especially the orthogonality and
  convergence slides.
- The application slide listed many uses but did not connect Fourier series to a
  single motivating mathematical problem.
- Parseval's identity was included but not explained enough to justify its
  presence.

### Critique before the next prompt

The third version fixed the major mathematical correctness issue. The next
revision should make the deck more presentation-ready by reducing text, giving a
stronger narrative, and using Parseval's identity only if it is explained as an
energy statement.

## Prompt Entry 4

### Exact prompt sent

Polish the Fourier series Marp deck for final submission: keep it to about 11 slides, reduce text per slide, add a short heat-equation motivation, include Parseval's identity as an energy interpretation, and keep all LaTeX compatible with Marp KaTeX.

### What I was trying to fix

I wanted the final deck to be cleaner, less crowded, and more coherent. I also
wanted to connect the topic to a real mathematical motivation while keeping the
LaTeX simple enough for Marp.

### Summary of the output

The final output produced a 12-slide Marp deck with YAML front matter, a clear
progression from motivation to formulas to example, a concise convergence slide,
a Parseval slide with an energy interpretation, and a heat equation slide.

### What actually changed in the output

- The slide count became reasonable for a short class presentation.
- Long paragraphs were replaced by shorter bullets and displayed equations.
- The heat equation was used as a focused application instead of a long list.
- Parseval's identity was framed as conservation of $L^2$ energy across
  frequency components.

### Remaining issues

- The deck still does not prove Dirichlet's convergence theorem; it only states
  the practical version needed for the presentation.
- The worked example focuses on $f(x)=x$, so students see an odd-function case
  but not a case with both sine and cosine terms.

### Final decision

This fourth version is the best output because it is mathematically accurate
for an undergraduate overview, short enough to present, and formatted as a valid
Marp deck.

## Marp Render Verification

I copied the best output into `week3/slides.md` and rendered it with the local
Marp CLI from the installed VS Code Marp extension:

```bash
node /home/agizz/.vscode/extensions/marp-team.marp-vscode-3.5.1/node_modules/@marp-team/marp-cli/marp-cli.js week3/slides.md --pdf --browser chrome --browser-path /usr/bin/google-chrome -o /tmp/week3-slides.pdf
```

The render succeeded. `pdfinfo /tmp/week3-slides.pdf` reported `Pages: 12`.
