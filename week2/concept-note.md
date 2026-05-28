# Lagrange Multipliers

## Definition

Lagrange multipliers give a method for finding local extrema of a differentiable
function subject to differentiable equality constraints. If
$f:\mathbb{R}^n\to\mathbb{R}$ is optimized subject to
$g(x)=c$, and if $\nabla g(x^\ast)\ne 0$ at a constrained local extremum
$x^\ast$, then there is a scalar $\lambda$ such that

$$
\nabla f(x^\ast)=\lambda \nabla g(x^\ast),
\qquad
g(x^\ast)=c.
$$

Geometrically, this means the level surface of the objective is tangent to the
constraint surface at the optimum.

## Example

Find the rectangle with maximum area among all rectangles with perimeter 20.
Let $x$ and $y$ be the side lengths. The objective and constraint are

$$
f(x,y)=xy,
\qquad
g(x,y)=2x+2y-20=0.
$$

The Lagrange multiplier equations are

$$
\nabla f=\lambda \nabla g,
\qquad
(y,x)=\lambda(2,2).
$$

Thus

$$
y=2\lambda,
\qquad
x=2\lambda,
$$

so $x=y$. Substituting into the constraint gives

$$
2x+2x=20,
\qquad
x=5.
$$

Therefore $y=5$ as well, and the maximum area is

$$
A=xy=5\cdot 5=25.
$$

Lagrange multipliers matter because they turn constrained optimization into a
system of equations that can often be solved directly.
