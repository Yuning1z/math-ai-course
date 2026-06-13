---
marp: true
theme: default
paginate: true
math: katex
---

# Fourier Series

**Week 3**

Representing functions by sine and cosine waves

---

## Big Idea

Fourier series express a periodic function as a sum of basic waves.

Instead of studying $f(x)$ directly, we study its frequency components.

$$
f(x) \sim \frac{a_0}{2}
+ \sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx)
$$

---

## Why This Is Useful

Many mathematical models separate naturally into frequencies.

For example, the heat equation smooths high-frequency oscillations faster than
low-frequency oscillations.

Fourier series turn some differential equations into simpler algebraic
relationships between modes.

---

## Setting

Work on the interval $[-\pi,\pi]$ and extend $f$ periodically.

The basic building blocks are

$$
1,\quad \cos x,\quad \sin x,\quad \cos 2x,\quad \sin 2x,\ldots
$$

Each term captures oscillation at a different frequency.

---

## Orthogonality

The sine and cosine functions are orthogonal on $[-\pi,\pi]$.

For example, when $m\ne n$,

$$
\int_{-\pi}^{\pi}\cos(mx)\cos(nx)\,dx = 0
$$

and similarly for the sine terms.

Orthogonality lets us isolate one coefficient at a time.

---

## Coefficient Formulas

For a suitable function $f$ on $[-\pi,\pi]$,

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\,dx
$$

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)\,dx
$$

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)\,dx
$$

---

## Symmetry Shortcut

Symmetry can simplify the computation.

- If $f$ is even, all sine coefficients vanish: $b_n=0$.
- If $f$ is odd, all cosine coefficients vanish: $a_0=a_n=0$.

This works because odd integrands integrate to zero on symmetric intervals.

---

## Example: $f(x)=x$

The function $f(x)=x$ is odd on $[-\pi,\pi]$.

So

$$
a_0=0,\qquad a_n=0
$$

Only sine terms remain:

$$
x \sim \sum_{n=1}^{\infty} b_n\sin(nx)
$$

---

## Computing $b_n$

$$
b_n
= \frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
$$

Since $x\sin(nx)$ is even,

$$
b_n
= \frac{2}{\pi}\int_0^\pi x\sin(nx)\,dx
= \frac{2(-1)^{n+1}}{n}
$$

Therefore,

$$
x \sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx)
$$

---

## Convergence

Fourier series do not always converge pointwise to $f(x)$ everywhere.

Under common piecewise smoothness assumptions:

- at a point of continuity, the series converges to $f(x)$;
- at a jump, it converges to the midpoint of the one-sided limits.

This explains the overshoot near jumps known as the Gibbs phenomenon.

---

## Parseval's Identity

Fourier coefficients also measure energy.

For square-integrable $f$,

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}|f(x)|^2\,dx
= \frac{a_0^2}{2}
+ \sum_{n=1}^{\infty}(a_n^2+b_n^2)
$$

The total energy equals the sum of the energies in each frequency mode.

---

## Takeaways

- Fourier series decompose periodic functions into sine and cosine modes.
- Orthogonality gives the coefficient formulas.
- Symmetry often makes computations much shorter.
- Convergence is subtle at discontinuities.
- Frequency viewpoints are powerful in differential equations and signal
  analysis.
