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

Classical derivatives are sometimes too restrictive.

Sobolev spaces let us work with functions that may have corners or rough
features, while still controlling their derivatives in an integral sense.

---

## From Smoothness to Energy

Instead of asking whether derivatives exist at every point, Sobolev spaces ask
whether derivatives are integrable.

For many PDE models, the natural quantity is an energy such as:

$$
\int_\Omega |\nabla u|^2\,dx
$$

---

## The Space \(H^1(\Omega)\)

For a domain $\Omega \subset \mathbb{R}^n$, the space $H^1(\Omega)$ contains
functions whose values and first weak derivatives are square-integrable:

$$
H^1(\Omega)
= \{u \in L^2(\Omega) : D_i u \in L^2(\Omega),\ i=1,\dots,n\}
$$

---

## Weak Derivatives

A function $v$ is the weak derivative of $u$ in the $i$th direction if:

$$
\int_\Omega u\,D_i\varphi\,dx
= -\int_\Omega v\,\varphi\,dx
$$

for every smooth compactly supported test function $\varphi$.

---

## General Sobolev Spaces

Sobolev spaces are usually written as $W^{k,p}(\Omega)$.

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

## Summary

- Sobolev spaces measure functions and weak derivatives together.
- Weak derivatives extend classical derivatives through integration by parts.
- $H^1(\Omega)$ is central for finite-energy PDE solutions.
- The notation $W^{k,p}(\Omega)$ records differentiability and integrability.
