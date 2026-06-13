---
marp: true
theme: default
paginate: true
math: katex
---

# Conjugate Gradient

## As Energy Minimization

Graduate Numerical Analysis

---

## The Problem

Solve

$$
Ax=b
$$

where

- $A=A^T$,
- $x,b\in\mathbb{R}^n$,
- $A$ is positive definite: $x^T A x>0$ for $x\ne 0$.

This structure turns a linear system into a geometric problem.

---

## The Energy Function

Define

$$
\phi(x)=\frac12 x^T A x-b^T x.
$$

Since $A$ is symmetric positive definite, $\phi$ is strictly convex.

Its gradient is

$$
\nabla \phi(x)=Ax-b.
$$

So the minimizer satisfies $Ax=b$.

---

## Residual as Negative Gradient

At iterate $x_k$, define the residual

$$
r_k=b-Ax_k.
$$

Then

$$
r_k=-\nabla \phi(x_k).
$$

Solving the linear system means driving the gradient of the quadratic energy to
zero.

---

## Why Steepest Descent Zigzags

Steepest descent moves along $r_k$.

For elongated quadratic contours, the residual direction changes sharply from
step to step.

The method repeatedly corrects error components it has already partly fixed.

CG improves this by choosing directions that are independent in the geometry of
$A$.

---

## The $A$-Inner Product

For SPD $A$, define

$$
\langle u,v\rangle_A=u^TAv,
\qquad
\|u\|_A=\sqrt{u^T A u}.
$$

Two directions are conjugate if

$$
p_i^T A p_j=0
\qquad (i\ne j).
$$

This is orthogonality in the energy geometry.

---

## Core CG Update

Starting from $x_0$, set

$$
r_0=b-Ax_0,\qquad p_0=r_0.
$$

Then iterate:

$$
\alpha_k=\frac{r_k^T r_k}{p_k^T A p_k},
\qquad
x_{k+1}=x_k+\alpha_k p_k,
$$

$$
r_{k+1}=r_k-\alpha_k A p_k.
$$

---

## Updating the Direction

Choose the next direction by

$$
\beta_k=\frac{r_{k+1}^T r_{k+1}}{r_k^T r_k},
\qquad
p_{k+1}=r_{k+1}+\beta_k p_k.
$$

The new direction keeps useful gradient information while preserving
$A$-conjugacy with previous directions.

---

## Krylov Subspaces

The $k$th Krylov subspace is

$$
\mathcal{K}_k(A,r_0)
=\operatorname{span}\{r_0,Ar_0,\ldots,A^{k-1}r_0\}.
$$

CG searches in the affine space

$$
x_0+\mathcal{K}_k(A,r_0).
$$

Each iteration adds one new matrix-vector level of information.

---

## The Minimization Property

CG produces $x_k$ such that

$$
x_k
=\arg\min_{x\in x_0+\mathcal{K}_k(A,r_0)}
\|x-x_\ast\|_A,
$$

where $x_\ast=A^{-1}b$.

Equivalently, $x_k$ minimizes the quadratic energy over the current Krylov
subspace.

---

## Convergence Intuition

The classical bound is

$$
\frac{\|x_k-x_\ast\|_A}{\|x_0-x_\ast\|_A}
\le
2\left(
\frac{\sqrt{\kappa(A)}-1}{\sqrt{\kappa(A)}+1}
\right)^k.
$$

Smaller condition numbers mean faster worst-case convergence.

Eigenvalue clustering can make convergence much faster than the bound suggests.

---

## Why Preconditioning Comes Next

Preconditioning replaces

$$
Ax=b
$$

with an equivalent system that has better spectral geometry.

The goal is not just a smaller condition number, but a matrix whose eigenvalues
are easier for Krylov polynomials to approximate.

---

## Takeaways

- CG solves SPD systems by minimizing a quadratic energy.
- The residual is the negative gradient.
- Conjugate directions are orthogonal in the $A$-inner product.
- Each iterate is optimal over a Krylov subspace.
- Convergence is governed by spectral geometry, motivating preconditioning.
