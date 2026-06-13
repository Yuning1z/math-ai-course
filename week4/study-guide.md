# Study Guide: The Lax-Milgram Theorem and Weak Elliptic Problems

Topic area: functional analysis, PDE, and numerical analysis.

## Learning Goals

After studying this guide, you should be able to:

- explain why coercivity and continuity are the right assumptions for a weak
  variational problem;
- apply the Lax-Milgram theorem to prove existence and uniqueness of weak
  solutions;
- check the hypotheses in concrete elliptic PDE examples;
- recognize how the theorem connects PDE theory, optimization, and finite
  element methods.

## Concept Explanation

### Intuition First

Many elliptic PDEs are hard to interpret pointwise. A classical solution of

$$
-\Delta u=f
$$

would need second derivatives, but many natural data sets only produce
solutions with one weak derivative. The weak formulation lowers the derivative
count by testing against a function $v$ and integrating by parts:

$$
\int_\Omega \nabla u\cdot \nabla v\,dx
= \int_\Omega f v\,dx.
$$

This has the abstract form

$$
a(u,v)=F(v)\qquad \text{for all }v\in V.
$$

Here $V$ is a Hilbert space, $a(\cdot,\cdot)$ is a bilinear form, and $F$ is a
bounded linear functional. The unknown is not a number but a vector $u$ in an
infinite-dimensional space.

The Lax-Milgram theorem says that this equation has exactly one solution if
two things happen:

1. The form is continuous, so it does not amplify inputs uncontrollably.
2. The form is coercive, so $a(v,v)$ controls the size of $v$.

Coercivity is the crucial stability condition. It says that the energy cannot
be small unless the function itself is small. This prevents flat directions,
such as constants in the pure Neumann Laplacian.

### Formal Statement

Let $V$ be a real Hilbert space with norm $\|\cdot\|_V$. Let
$a:V\times V\to \mathbb{R}$ be bilinear, and let $F\in V'$.

Assume:

1. Continuity: there exists $M>0$ such that

$$
|a(u,v)|\le M\|u\|_V\|v\|_V
\qquad \text{for all }u,v\in V.
$$

2. Coercivity: there exists $\alpha>0$ such that

$$
a(v,v)\ge \alpha \|v\|_V^2
\qquad \text{for all }v\in V.
$$

Then there exists a unique $u\in V$ such that

$$
a(u,v)=F(v)\qquad \text{for all }v\in V.
$$

Moreover,

$$
\|u\|_V\le \frac{1}{\alpha}\|F\|_{V'}.
$$

If $a$ is symmetric, then $u$ is also the unique minimizer of the energy

$$
J(v)=\frac12 a(v,v)-F(v).
$$

### Proof Architecture

For each $u\in V$, the map $v\mapsto a(u,v)$ is a bounded linear functional.
Thus $a$ defines a bounded operator

$$
A:V\to V',\qquad (Au)(v)=a(u,v).
$$

The weak problem is simply

$$
Au=F.
$$

Continuity gives boundedness of $A$. Coercivity gives the lower bound

$$
\|Au\|_{V'}\|u\|_V
\ge |(Au)(u)|
= |a(u,u)|
\ge \alpha \|u\|_V^2,
$$

so

$$
\|Au\|_{V'}\ge \alpha \|u\|_V.
$$

This implies injectivity and stability. A standard Hilbert-space argument,
using the Riesz representation theorem and the closed range theorem, then
shows that the range of $A$ is all of $V'$. Therefore $Au=F$ has a unique
solution for every bounded functional $F$.

## Worked Example 1: Dirichlet Poisson Problem

### Problem

Let $\Omega\subset \mathbb{R}^d$ be a bounded Lipschitz domain and let
$f\in L^2(\Omega)$. Prove that the boundary value problem

$$
\begin{cases}
-\Delta u=f & \text{in }\Omega,\\
u=0 & \text{on }\partial\Omega
\end{cases}
$$

has a unique weak solution $u\in H_0^1(\Omega)$.

### Solution

Set

$$
V=H_0^1(\Omega).
$$

Multiply the PDE by $v\in H_0^1(\Omega)$ and integrate by parts:

$$
\int_\Omega \nabla u\cdot \nabla v\,dx
=\int_\Omega f v\,dx.
$$

So define

$$
a(u,v)=\int_\Omega \nabla u\cdot \nabla v\,dx,
\qquad
F(v)=\int_\Omega f v\,dx.
$$

Continuity follows from Cauchy-Schwarz:

$$
|a(u,v)|
\le \|\nabla u\|_{L^2(\Omega)}\|\nabla v\|_{L^2(\Omega)}
\le \|u\|_{H^1(\Omega)}\|v\|_{H^1(\Omega)}.
$$

The functional $F$ is bounded because

$$
|F(v)|
\le \|f\|_{L^2(\Omega)}\|v\|_{L^2(\Omega)}
\le C_P\|f\|_{L^2(\Omega)}\|\nabla v\|_{L^2(\Omega)}
\le C\|f\|_{L^2(\Omega)}\|v\|_{H^1(\Omega)}.
$$

Here $C_P$ is the Poincare constant.

Coercivity follows from Poincare's inequality:

$$
\|v\|_{H^1(\Omega)}^2
=\|v\|_{L^2(\Omega)}^2+\|\nabla v\|_{L^2(\Omega)}^2
\le (C_P^2+1)\|\nabla v\|_{L^2(\Omega)}^2.
$$

Thus

$$
a(v,v)=\|\nabla v\|_{L^2(\Omega)}^2
\ge \frac{1}{C_P^2+1}\|v\|_{H^1(\Omega)}^2.
$$

The Lax-Milgram theorem gives a unique $u\in H_0^1(\Omega)$ satisfying

$$
\int_\Omega \nabla u\cdot \nabla v\,dx
=\int_\Omega f v\,dx
\qquad \text{for all }v\in H_0^1(\Omega).
$$

It also gives the stability estimate

$$
\|u\|_{H^1(\Omega)}\le C\|f\|_{L^2(\Omega)}.
$$

## Worked Example 2: A One-Dimensional Reaction Problem

### Problem

Use Lax-Milgram to prove existence and uniqueness for

$$
\begin{cases}
-u''+u=x, & 0<x<1,\\
u(0)=u(1)=0.
\end{cases}
$$

Then find the classical solution.

### Solution

Let

$$
V=H_0^1(0,1).
$$

The weak form is

$$
\int_0^1 u'v'\,dx+\int_0^1 uv\,dx
=\int_0^1 x v\,dx
\qquad \text{for all }v\in H_0^1(0,1).
$$

Define

$$
a(u,v)=\int_0^1 u'v'\,dx+\int_0^1 uv\,dx,
\qquad
F(v)=\int_0^1 x v\,dx.
$$

Continuity:

$$
|a(u,v)|
\le \|u'\|_2\|v'\|_2+\|u\|_2\|v\|_2
\le \|u\|_{H^1(0,1)}\|v\|_{H^1(0,1)}.
$$

Coercivity:

$$
a(v,v)=\|v'\|_2^2+\|v\|_2^2
=\|v\|_{H^1(0,1)}^2.
$$

The functional $F$ is bounded:

$$
|F(v)|
\le \|x\|_{L^2(0,1)}\|v\|_{L^2(0,1)}
\le \|x\|_{L^2(0,1)}\|v\|_{H^1(0,1)}.
$$

Therefore Lax-Milgram gives a unique weak solution $u\in H_0^1(0,1)$.

To find the classical solution, solve the ODE

$$
-u''+u=x.
$$

A particular solution is $u_p=x$. The homogeneous equation is

$$
-u''+u=0,
$$

so

$$
u_h=C e^x + D e^{-x}.
$$

Thus

$$
u(x)=C e^x +D e^{-x}+x.
$$

The boundary conditions give

$$
u(0)=C+D=0,
$$

so $D=-C$. Also,

$$
u(1)=C(e-e^{-1})+1=0,
$$

so

$$
C=-\frac{1}{e-e^{-1}}.
$$

Since $e^x-e^{-x}=2\sinh x$, the solution is

$$
u(x)=x-\frac{\sinh x}{\sinh 1}.
$$

Check:

$$
u''(x)=-\frac{\sinh x}{\sinh 1},
$$

so

$$
-u''(x)+u(x)
=\frac{\sinh x}{\sinh 1}
+x-\frac{\sinh x}{\sinh 1}
=x.
$$

Also $u(0)=0$ and $u(1)=1-1=0$. Hence the weak solution is represented by this
classical function.

## Practice Problems with Solutions

### Problem 1

Let $V=H_0^1(0,1)$ and

$$
a(u,v)=\int_0^1 (1+x^2)u'v'\,dx+\int_0^1 uv\,dx.
$$

Show that $a$ satisfies the Lax-Milgram hypotheses.

### Solution

Since

$$
1\le 1+x^2\le 2
\qquad \text{for }0\le x\le 1,
$$

we have

$$
|a(u,v)|
\le 2\|u'\|_2\|v'\|_2+\|u\|_2\|v\|_2
\le 2\|u\|_{H^1}\|v\|_{H^1}
+\|u\|_{H^1}\|v\|_{H^1}.
$$

Thus

$$
|a(u,v)|\le 3\|u\|_{H^1}\|v\|_{H^1}.
$$

For coercivity,

$$
a(v,v)
=\int_0^1(1+x^2)|v'|^2\,dx+\int_0^1 |v|^2\,dx
\ge \|v'\|_2^2+\|v\|_2^2
=\|v\|_{H^1}^2.
$$

So $a$ is continuous and coercive on $H_0^1(0,1)$.

### Problem 2

Let $V=H^1(0,1)$ and

$$
a(u,v)=\int_0^1 u'v'\,dx.
$$

Explain why Lax-Milgram does not apply on $H^1(0,1)$. How can the problem be
fixed?

### Solution

The form is not coercive on $H^1(0,1)$. Take $v(x)=1$. Then $v\ne 0$ in
$H^1(0,1)$, but

$$
a(v,v)=\int_0^1 |v'|^2\,dx=0.
$$

So $a(v,v)$ cannot control $\|v\|_{H^1}^2$.

This is the constant-function nullspace of the Neumann Laplacian. One fix is
to work on the mean-zero subspace

$$
V_0=\left\{v\in H^1(0,1):\int_0^1 v\,dx=0\right\}.
$$

On $V_0$, Poincare's inequality gives

$$
\|v\|_{L^2}\le C\|v'\|_{L^2},
$$

so

$$
\|v\|_{H^1}^2
\le (C^2+1)\|v'\|_{L^2}^2.
$$

Thus $a$ is coercive on $V_0$. For a pure Neumann PDE, one also needs a
compatibility condition on the data, such as $\int_0^1 f\,dx=0$, because the
solution is unique only up to an additive constant unless a normalization is
imposed.

### Problem 3

Let $V=H_0^1(0,1)$ and let $\beta\in\mathbb{R}$. Define the nonsymmetric form

$$
a(u,v)=\int_0^1 u'v'\,dx+\beta\int_0^1 u'v\,dx.
$$

Show that $a$ is continuous and coercive on $V$.

### Solution

Continuity follows from Cauchy-Schwarz and Poincare:

$$
|a(u,v)|
\le \|u'\|_2\|v'\|_2
+|\beta|\|u'\|_2\|v\|_2
\le (1+|\beta|C_P)\|u'\|_2\|v'\|_2.
$$

Since $\|w'\|_2$ is equivalent to the $H_0^1$ norm, $a$ is continuous on $V$.

For coercivity, use $v\in H_0^1(0,1)$:

$$
a(v,v)
=\int_0^1 |v'|^2\,dx+\beta\int_0^1 v'v\,dx.
$$

But

$$
\int_0^1 v'v\,dx
=\frac12\int_0^1 (v^2)'\,dx
=\frac12(v(1)^2-v(0)^2)=0.
$$

Therefore

$$
a(v,v)=\|v'\|_2^2.
$$

By Poincare,

$$
\|v'\|_2^2\ge \alpha \|v\|_{H^1}^2
$$

for some $\alpha>0$. Hence $a$ is coercive. This example also shows that
Lax-Milgram does not require symmetry.

## Connections

### Functional Analysis

Lax-Milgram is an operator invertibility theorem in disguise. It turns the
bilinear form $a$ into an operator $A:V\to V'$ and gives conditions under which
$A$ has a bounded inverse. The Riesz representation theorem is the bridge
between Hilbert-space geometry and weak formulations.

### Partial Differential Equations

Weak elliptic PDE theory depends on the theorem because it gives existence,
uniqueness, and stability before any pointwise regularity is known. Once a weak
solution exists, elliptic regularity can ask whether the solution is actually
in $H^2$, $C^\alpha$, or smoother spaces.

### Finite Element Methods

The same bilinear form appears in Galerkin discretization. If $V_h\subset V$ is
a finite-dimensional finite element space, the discrete problem is

$$
a(u_h,v_h)=F(v_h)\qquad \text{for all }v_h\in V_h.
$$

The continuity and coercivity constants lead directly to Cea's lemma:

$$
\|u-u_h\|_V
\le \frac{M}{\alpha}\inf_{w_h\in V_h}\|u-w_h\|_V.
$$

Thus the numerical error is controlled by the best approximation error in the
chosen finite element space.

### Optimization

When $a$ is symmetric, the weak solution is the minimizer of an energy
functional. This connects elliptic PDEs to convex optimization: coercivity
corresponds to strong convexity, and the weak equation is the first-order
optimality condition.

## Copilot Chat Refinement Record

### Round 1

Prompt used:

> Create a graduate-level study guide on the Lax-Milgram theorem for weak
> elliptic PDE problems.

What the first draft did:

- It stated the theorem and gave a short Poisson example.
- It mentioned Hilbert spaces and weak solutions.

Problems noticed:

- The explanation started formally and did not build intuition.
- The example skipped the boundedness and coercivity estimates.
- There were no practice problems or connections to numerical methods.

### Round 2

Prompt used:

> Revise the guide so it starts with intuition, then gives the formal theorem,
> and add two worked examples with complete estimates.

What improved:

- The guide now explained why weak forms lower derivative requirements.
- The Poisson example included Poincare's inequality.
- A second example was added.

What was still weak:

- The second example was existence-only and did not solve anything explicitly.
- The proof idea of the theorem was too vague.

### Round 3

Prompt used:

> Improve the study guide by adding a proof architecture, replacing the second
> example with a one-dimensional problem that has an explicit solution, and add
> three practice problems with solutions.

What changed:

- The operator viewpoint $A:V\to V'$ was added.
- The second worked example now solves $-u''+u=x$ exactly.
- Practice problems were added, including a failure-of-coercivity example.

Remaining issue:

- The guide still needed stronger connections to finite element methods,
  optimization, and the role of nonsymmetry.

### Round 4

Prompt used:

> Polish the final version: make it graduate-level but readable, state every
> estimate cleanly, include connections to FEM and optimization, and make sure
> the final guide is clearly better than the first draft.

Final improvements:

- The final guide has intuition first, then formal theorem, then proof
  architecture.
- Worked examples now include full verification of Lax-Milgram hypotheses.
- Practice problems include complete solutions.
- The connections section links the theorem to functional analysis, PDE,
  finite element error analysis, and optimization.
