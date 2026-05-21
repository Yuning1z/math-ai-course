---
marp: true
theme: default
paginate: true
math: katex
---

# Sobolev Spaces

**MATH 797 - Week 1**

---

## Why Sobolev Spaces?

Classical differentiability is often too restrictive for real PDE solutions.

Sobolev spaces keep the useful idea of derivatives, but measure them through
integral norms rather than pointwise smoothness.

---

## Smoothness as a Norm

A Sobolev norm measures a function together with its weak derivatives.

For example, the $H^1$ norm controls both $u$ and its gradient:

$$
\|u\|_{H^1(\Omega)}^2
= \int_\Omega |u|^2\,dx + \int_\Omega |\nabla u|^2\,dx
$$

---

## The Space $H^1(\Omega)$

For a domain $\Omega \subset \mathbb{R}^n$, the space $H^1(\Omega)$ contains
functions whose values and first weak derivatives are square-integrable:

$$
H^1(\Omega)
= \{u \in L^2(\Omega) : D_i u \in L^2(\Omega),\ i=1,\dots,n\}
$$

---

## Weak Derivatives

A function $v$ is the weak derivative of $u$ in the $i$th direction when the
integration-by-parts identity holds:

$$
\int_\Omega u\,D_i\varphi\,dx
= -\int_\Omega v\,\varphi\,dx
$$

for every smooth compactly supported test function $\varphi$.

---

## General Sobolev Spaces

The notation $W^{k,p}(\Omega)$ records two pieces of information:

- $k$ counts the number of weak derivatives
- $p$ sets the integrability scale
- $H^k(\Omega)$ means $W^{k,2}(\Omega)$

$$
\|u\|_{W^{k,p}}
= \left(\sum_{|\alpha|\le k}\|D^\alpha u\|_{L^p}^p\right)^{1/p}
$$

---

## Why They Matter

Sobolev spaces are the natural language for:

- weak solutions of PDEs
- finite element methods
- variational problems
- boundary traces and regularity theory

They balance roughness with enough structure for analysis.

---

## Example Intuition

A function can fail to be classically differentiable at a point and still
belong to a Sobolev space.

The space cares about averaged behavior, not perfect pointwise smoothness.

$$
\int_\Omega |\nabla u|^2\,dx < \infty
$$

---

## Summary

- Sobolev spaces measure functions and weak derivatives together.
- Weak derivatives extend classical derivatives through integration by parts.
- $H^1(\Omega)$ is central for finite-energy PDE solutions.
- The notation $W^{k,p}(\Omega)$ records differentiability and integrability.
