# Week 5 Lecture Plan

## Topic

Conjugate Gradient as Energy Minimization

## Target Audience

Graduate students in numerical analysis, scientific computing, or applied
mathematics. The audience is assumed to know basic linear algebra, inner
products, orthogonality, and the idea of iterative methods, but not the full
Krylov-subspace theory of conjugate gradient.

## Lecture Goal

By the end of the lecture, students should understand why conjugate gradient
works especially well for symmetric positive definite linear systems and how
its algebraic iteration is equivalent to minimizing a quadratic energy over a
growing Krylov subspace.

## Key Points to Cover

1. **The problem class:** solve $Ax=b$ where $A=A^T$ and $A$ is positive
   definite; explain why this structure gives a geometry.
2. **Energy viewpoint:** show that solving $Ax=b$ is equivalent to minimizing
   $\phi(x)=\frac12 x^T A x-b^T x$.
3. **Residual and gradient:** connect the residual $r_k=b-Ax_k$ to the negative
   gradient of the energy.
4. **Steepest descent limitation:** explain why ordinary residual directions can
   zigzag on elongated quadratic contours.
5. **Conjugate directions:** define $A$-orthogonality, $p_i^T A p_j=0$, and show
   why it avoids redoing previous work.
6. **Krylov subspace structure:** state that $x_k$ minimizes the energy over
   $x_0+\mathcal{K}_k(A,r_0)$, where
   $\mathcal{K}_k(A,r_0)=\operatorname{span}\{r_0,Ar_0,\ldots,A^{k-1}r_0\}$.
7. **Convergence intuition:** relate CG speed to eigenvalue clustering and the
   condition number $\kappa(A)$, motivating preconditioning.

## Planned Flow

Start with the quadratic picture because it gives the audience an immediate
geometric object. Then derive the algorithmic quantities from that picture:
gradient, residual, step length, and conjugate directions. Finish with the
Krylov minimization statement and a short discussion of why preconditioning is
the natural next topic.

## Copilot Chat Slide Refinement Record

### Draft Prompt

> Using this lecture plan as context, create a graduate-level Marp slide deck on
> conjugate gradient as energy minimization.

Result: the first deck had the right theme but was too broad. It included
implementation details before the energy interpretation and did not define the
$A$-norm.

### Refinement Round 1

> Revise the slides so the structure follows the lecture plan: energy first,
> residual-as-gradient second, steepest descent failure third, then conjugate
> directions and Krylov minimization. Use consistent notation $A$, $b$, $x_k$,
> $r_k$, and $p_k$.

Result: the structure improved and notation became consistent. However, the
slides were still too text-heavy and did not clearly state the CG update
formulas.

### Refinement Round 2

> Polish the deck for graduate numerical analysis students: reduce text per
> slide, add the standard CG update formulas, define the $A$-norm, and include a
> final slide connecting convergence to condition number and preconditioning.

Result: the final deck became presentation-ready, with short slides, consistent
notation, the minimization theorem, and the correct level of detail for the
target audience.
