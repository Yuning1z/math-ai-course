# Capstone Study Guide: Sobolev Spaces, Weak Derivatives, and Energy Methods

Topic area: functional analysis, partial differential equations, and numerical
analysis.

This guide develops the basic graduate-level toolkit behind weak formulations
of elliptic boundary value problems. The central example is the Dirichlet
Poisson problem

$$
\begin{cases}
-\Delta u=f & \text{in }\Omega,\\
u=0 & \text{on }\partial\Omega,
\end{cases}
$$

but the real subject is broader: why Sobolev spaces are the natural habitat for
PDE solutions, how weak derivatives lower differentiability requirements, why
coercivity gives well-posedness, and how the same structure appears in
finite-dimensional numerical methods.

## 1. Learning Goals

After working through this guide, you should be able to:

- define weak derivatives and Sobolev spaces precisely;
- explain why weak formulations are not just formal integrations by parts;
- prove basic boundedness and coercivity estimates for elliptic bilinear
  forms;
- apply the Lax-Milgram theorem to Dirichlet, reaction-diffusion, and mixed
  boundary problems;
- interpret weak solutions as minimizers of energy functionals;
- derive Galerkin approximations and understand their stability;
- connect Sobolev theory to finite elements, optimization, and spectral
  theory.

## 2. Intuition First

Classical calculus teaches us to solve differential equations by looking for
functions with enough pointwise derivatives. For the equation

$$
-u''=f \quad \text{on }(0,1),
$$

a classical solution should have two derivatives. This is a strong
requirement. If $f$ has jumps, or if the domain has corners, or if the problem
comes from measured data, the actual solution may not be twice differentiable
in the classical sense. Nevertheless, the equation often still has a perfectly
meaningful physical interpretation: the solution has finite energy, the flux
balances against test functions, and the boundary condition holds in an
appropriate averaged sense.

The weak viewpoint begins with a simple idea. Instead of differentiating the
unknown twice, multiply the equation by a smooth test function $v$ and
integrate by parts:

$$
\int_\Omega (-\Delta u)v\,dx
=\int_\Omega \nabla u\cdot \nabla v\,dx
-\int_{\partial\Omega}\frac{\partial u}{\partial n}v\,dS.
$$

For zero Dirichlet test functions, the boundary term disappears. The equation
becomes

$$
\int_\Omega \nabla u\cdot \nabla v\,dx
=\int_\Omega f v\,dx.
$$

Now the unknown only needs one square-integrable derivative. This is the entry
point to Sobolev spaces.

The slogan is:

> Weak formulations move derivatives from the unknown onto test functions, so
> the correct solution space is determined by energy rather than pointwise
> differentiability.

For Poisson's equation, the energy is

$$
E(v)=\frac12\int_\Omega |\nabla v|^2\,dx-\int_\Omega f v\,dx.
$$

The solution is the function that minimizes this energy among all admissible
functions with the boundary condition. The first variation of the energy gives
the weak equation. This variational structure explains why Hilbert spaces,
inner products, and coercive bilinear forms appear so naturally.

## 3. Formal Definitions

### 3.1 Test Functions and Distributions

Let $\Omega\subset\mathbb R^d$ be open. The space $C_c^\infty(\Omega)$
consists of smooth functions with compact support in $\Omega$. These functions
are used as probes. A distribution is a continuous linear functional on
$C_c^\infty(\Omega)$.

If $u\in L^1_{\mathrm{loc}}(\Omega)$, then $u$ defines a distribution by

$$
\varphi\mapsto \int_\Omega u\varphi\,dx.
$$

The distributional derivative $D_i u$ is defined by

$$
\langle D_i u,\varphi\rangle
=-\int_\Omega u\,D_i\varphi\,dx
\qquad \text{for all }\varphi\in C_c^\infty(\Omega).
$$

This formula is not a theorem; it is the definition. It extends the classical
integration-by-parts identity to functions that may not have pointwise
derivatives.

### 3.2 Weak Derivatives

Let $u\in L^1_{\mathrm{loc}}(\Omega)$. A function $g_i\in
L^1_{\mathrm{loc}}(\Omega)$ is called the weak $i$th partial derivative of $u$
if

$$
\int_\Omega g_i\varphi\,dx
=-\int_\Omega u\,D_i\varphi\,dx
\qquad \text{for all }\varphi\in C_c^\infty(\Omega).
$$

When such $g_i$ exists, we write $D_i u=g_i$ weakly. Weak derivatives are
unique up to equality almost everywhere. Classical derivatives are weak
derivatives when they exist and are locally integrable.

### 3.3 Sobolev Spaces

For an integer $k\ge 0$ and $1\le p\le\infty$, define

$$
W^{k,p}(\Omega)
=\{u\in L^p(\Omega): D^\alpha u\in L^p(\Omega)
\text{ for all }|\alpha|\le k\}.
$$

The norm is

$$
\|u\|_{W^{k,p}}
=\left(\sum_{|\alpha|\le k}\|D^\alpha u\|_{L^p}^p\right)^{1/p}
$$

for $1\le p<\infty$, with the usual modification for $p=\infty$.

The Hilbert case is especially important:

$$
H^k(\Omega)=W^{k,2}(\Omega).
$$

For $H^1(\Omega)$,

$$
\|u\|_{H^1(\Omega)}^2
=\|u\|_{L^2(\Omega)}^2+\|\nabla u\|_{L^2(\Omega)}^2.
$$

The space $H_0^1(\Omega)$ is the closure of $C_c^\infty(\Omega)$ in the
$H^1$ norm. Intuitively, it consists of $H^1$ functions whose trace on the
boundary is zero. The trace theorem makes this precise on sufficiently regular
domains, such as bounded Lipschitz domains.

### 3.4 Weak Form of the Dirichlet Poisson Problem

Let $f\in L^2(\Omega)$. A weak solution of

$$
-\Delta u=f,\qquad u|_{\partial\Omega}=0
$$

is a function $u\in H_0^1(\Omega)$ such that

$$
\int_\Omega \nabla u\cdot\nabla v\,dx
=\int_\Omega f v\,dx
\qquad\text{for all }v\in H_0^1(\Omega).
$$

This is meaningful because $\nabla u,\nabla v\in L^2(\Omega)$ and $fv\in
L^1(\Omega)$ by Cauchy-Schwarz.

## 4. The Main Theorem: Lax-Milgram

Let $V$ be a real Hilbert space. Let $a:V\times V\to\mathbb R$ be bilinear and
let $F\in V'$ be a bounded linear functional. Assume:

1. Continuity: there exists $M>0$ such that

$$
|a(u,v)|\le M\|u\|_V\|v\|_V
\qquad\text{for all }u,v\in V.
$$

2. Coercivity: there exists $\alpha>0$ such that

$$
a(v,v)\ge \alpha\|v\|_V^2
\qquad\text{for all }v\in V.
$$

Then there exists a unique $u\in V$ satisfying

$$
a(u,v)=F(v)\qquad\text{for all }v\in V.
$$

Moreover,

$$
\|u\|_V\le \frac{1}{\alpha}\|F\|_{V'}.
$$

The theorem is the infinite-dimensional analog of solving a positive definite
linear system. Continuity says the matrix entries are controlled; coercivity
says there are no zero-energy directions. In finite dimensions, coercivity is
positive definiteness. In infinite dimensions, it is the assumption that
prevents minimizing sequences from escaping.

When $a$ is symmetric, the solution is also the unique minimizer of

$$
J(v)=\frac12 a(v,v)-F(v).
$$

This gives the bridge to optimization and numerical energy methods.

### 4.1 Why the Assumptions Are Not Cosmetic

It is tempting to treat the hypotheses of Lax-Milgram as a checklist, but each
one encodes a different mathematical protection.

The Hilbert-space assumption gives an inner product and therefore a Riesz
representation theorem. This matters because the weak equation

$$
a(u,v)=F(v)
$$

is an equation in the dual space. For each fixed $u$, the map
$v\mapsto a(u,v)$ is a functional. The theorem says that every bounded
functional $F$ is hit by exactly one such map. In a Hilbert space, duality is
concrete enough that one can use geometric tools such as orthogonality and
projection.

Continuity of $a$ is the boundedness assumption. Without it, the expression
$a(u,v)$ may be too sensitive to small perturbations of $u$ or $v$. In PDE
language, continuity is usually proved by Holder or Cauchy-Schwarz
inequalities. In matrix language, it says the associated operator has finite
operator norm.

Coercivity is the stability assumption. It rules out directions in which the
energy is flat. For the Dirichlet Laplacian, Poincare's inequality turns

$$
\|\nabla v\|_{L^2}^2
$$

into control of the full $H^1$ norm. For the pure Neumann Laplacian, constants
have zero gradient, so coercivity fails unless one removes constants by passing
to a quotient space or a mean-zero subspace. This is why coercivity is more
than positivity. A bilinear form can be nonnegative and still fail to control
the norm.

Boundedness of $F$ is also essential. The weak formulation asks that
$v\mapsto F(v)$ act continuously on the chosen test space. If the right-hand
side is too singular for the space, the equation may not even be meaningful.
This is why $f\in L^2(\Omega)$ is sufficient for $H_0^1$ test functions, and
why the broader condition $f\in H^{-1}(\Omega)$ is the natural endpoint.

### 4.2 Proof Architecture of Lax-Milgram

Here is the proof idea in a form that is useful for PDE work. Define an
operator

$$
A:V\to V',\qquad (Au)(v)=a(u,v).
$$

The weak problem is simply $Au=F$. Continuity of $a$ implies $A$ is bounded:

$$
\|Au\|_{V'}
=\sup_{\|v\|_V=1}|a(u,v)|
\le M\|u\|_V.
$$

Coercivity gives a lower bound:

$$
\|Au\|_{V'}\|u\|_V
\ge |(Au)(u)|
=|a(u,u)|
\ge \alpha\|u\|_V^2.
$$

If $u\ne 0$, divide by $\|u\|_V$ and obtain

$$
\|Au\|_{V'}\ge \alpha\|u\|_V.
$$

This lower bound implies injectivity and stability. It also implies the range
of $A$ is closed. To show surjectivity, one uses a Hilbert-space argument: if
the range were not all of $V'$, then there would be a nonzero object
orthogonal to the range. Using the Riesz representation theorem to identify
$V'$ with $V$, this orthogonality would contradict coercivity. Thus $A$ maps
$V$ onto $V'$ and has a bounded inverse.

This proof explains why the theorem feels like linear algebra. A coercive
bilinear form behaves like a positive definite matrix even in infinite
dimensions. The difference is that in infinite dimensions one must prove that
the range is closed and that no functional is missed.

### 4.3 Trace, Density, and Boundary Conditions

The notation $H_0^1(\Omega)$ hides a subtle point. A Sobolev function is an
equivalence class of functions defined almost everywhere, so its pointwise
boundary values may not make sense. The zero boundary condition in
$H_0^1(\Omega)$ is not initially a pointwise statement. It means the function
can be approximated in $H^1$ by smooth compactly supported functions.

On bounded Lipschitz domains, the trace theorem gives a continuous linear map

$$
\gamma:H^1(\Omega)\to H^{1/2}(\partial\Omega)
$$

that agrees with the classical boundary restriction for smooth functions. In
that setting,

$$
H_0^1(\Omega)=\{u\in H^1(\Omega):\gamma u=0\}.
$$

This theorem is why it is legitimate to say that a weak solution in
$H_0^1(\Omega)$ has zero boundary value. It also explains why domain
regularity appears in PDE statements. If the boundary is too rough, trace and
density results require more care.

Density is equally important. The weak derivative is defined using smooth
compactly supported test functions, but the weak formulation for Poisson uses
all $v\in H_0^1(\Omega)$. The passage from smooth tests to all energy tests is
justified by density and continuity. First prove the identity for smooth
functions, then extend it to the closure.

### 4.4 Regularity Is a Separate Question

Lax-Milgram gives existence and uniqueness in the energy space. It does not
automatically say the solution is classical. For the Dirichlet Poisson problem,
the theorem gives $u\in H_0^1(\Omega)$. Under additional assumptions, one may
prove more. For example, if $\Omega$ is smooth enough and $f\in L^2(\Omega)$,
elliptic regularity can imply $u\in H^2(\Omega)$ with an estimate

$$
\|u\|_{H^2(\Omega)}\le C\|f\|_{L^2(\Omega)}.
$$

But this can fail on nonsmooth domains. Corners can create singularities even
when the data are smooth. This distinction is important in numerical analysis:
finite element convergence rates often depend on how much Sobolev regularity
the exact solution has. A method may be stable for all $H_0^1$ solutions but
converge faster only for solutions in $H^2$ or higher.

### 4.5 The Energy Norm

For a coercive symmetric bilinear form, it is often useful to define the energy
norm

$$
\|v\|_a=\sqrt{a(v,v)}.
$$

Continuity and coercivity imply this norm is equivalent to the original
$V$ norm:

$$
\sqrt{\alpha}\|v\|_V\le \|v\|_a\le \sqrt{M}\|v\|_V.
$$

The energy norm is not just a technical convenience. It measures the error in
the geometry chosen by the PDE. For Poisson's equation, the energy norm is the
$L^2$ norm of the gradient, so two functions are close in energy when their
fluxes or slopes are close. In Galerkin methods, orthogonality and best
approximation are often cleanest in this norm.

## 5. Worked Examples

### Example 1: A Function with a Weak Derivative

**Problem.** Let $u(x)=|x|$ on $(-1,1)$. Find its weak derivative.

**Solution.** Classically, $u'(x)=1$ for $x>0$ and $u'(x)=-1$ for $x<0$, while
the derivative is undefined at $x=0$. Since one point has measure zero, the
candidate weak derivative is

$$
g(x)=\begin{cases}
-1, & x<0,\\
1, & x>0.
\end{cases}
$$

Let $\varphi\in C_c^\infty(-1,1)$. Then

$$
\int_{-1}^1 |x|\varphi'(x)\,dx
=\int_{-1}^0 (-x)\varphi'(x)\,dx+\int_0^1 x\varphi'(x)\,dx.
$$

Integrating by parts on the two intervals gives

$$
\int_{-1}^0 (-x)\varphi'(x)\,dx
=-\big[x\varphi(x)\big]_{-1}^0+\int_{-1}^0\varphi(x)\,dx
=\int_{-1}^0\varphi(x)\,dx,
$$

because $\varphi$ is compactly supported. Also

$$
\int_0^1 x\varphi'(x)\,dx
=\big[x\varphi(x)\big]_0^1-\int_0^1\varphi(x)\,dx
=-\int_0^1\varphi(x)\,dx.
$$

Therefore

$$
\int_{-1}^1 |x|\varphi'(x)\,dx
=\int_{-1}^0\varphi\,dx-\int_0^1\varphi\,dx.
$$

Thus

$$
-\int_{-1}^1 |x|\varphi'(x)\,dx
=\int_{-1}^1 g(x)\varphi(x)\,dx.
$$

So $u$ has weak derivative $g=\operatorname{sign}(x)$ almost everywhere.
This example shows that a corner is allowed in $H^1$.

### Example 2: Dirichlet Poisson Problem

**Problem.** Let $\Omega\subset\mathbb R^d$ be a bounded Lipschitz domain and
$f\in L^2(\Omega)$. Prove that the weak Dirichlet Poisson problem has a unique
solution in $H_0^1(\Omega)$.

**Solution.** Set $V=H_0^1(\Omega)$ and define

$$
a(u,v)=\int_\Omega \nabla u\cdot\nabla v\,dx,\qquad
F(v)=\int_\Omega f v\,dx.
$$

Continuity follows from Cauchy-Schwarz:

$$
|a(u,v)|\le \|\nabla u\|_2\|\nabla v\|_2
\le \|u\|_{H^1}\|v\|_{H^1}.
$$

The functional is bounded because

$$
|F(v)|\le \|f\|_2\|v\|_2\le C_P\|f\|_2\|\nabla v\|_2
\le C\|f\|_2\|v\|_{H^1}.
$$

Here $C_P$ is the Poincare constant. Coercivity uses the same inequality:

$$
\|v\|_{H^1}^2
=\|v\|_2^2+\|\nabla v\|_2^2
\le (C_P^2+1)\|\nabla v\|_2^2.
$$

Thus

$$
a(v,v)=\|\nabla v\|_2^2
\ge \frac{1}{C_P^2+1}\|v\|_{H^1}^2.
$$

Lax-Milgram gives a unique $u\in H_0^1(\Omega)$ such that

$$
\int_\Omega\nabla u\cdot\nabla v\,dx
=\int_\Omega fv\,dx
\qquad\text{for all }v\in H_0^1(\Omega).
$$

It also gives the stability estimate

$$
\|u\|_{H^1}\le C\|f\|_{L^2}.
$$

### Example 3: Reaction-Diffusion with a Positive Potential

**Problem.** Let $q\in L^\infty(\Omega)$ and assume $q(x)\ge q_0>0$ almost
everywhere. Prove well-posedness for

$$
-\Delta u+q(x)u=f,\qquad u|_{\partial\Omega}=0.
$$

**Solution.** Again take $V=H_0^1(\Omega)$ and define

$$
a(u,v)=\int_\Omega \nabla u\cdot\nabla v\,dx+\int_\Omega q uv\,dx.
$$

Continuity follows from

$$
|a(u,v)|
\le \|\nabla u\|_2\|\nabla v\|_2+\|q\|_\infty\|u\|_2\|v\|_2
\le (1+\|q\|_\infty)\|u\|_{H^1}\|v\|_{H^1}.
$$

Coercivity is even more direct:

$$
a(v,v)=\|\nabla v\|_2^2+\int_\Omega qv^2\,dx
\ge \|\nabla v\|_2^2+q_0\|v\|_2^2.
$$

Therefore

$$
a(v,v)\ge \min(1,q_0)\|v\|_{H^1}^2.
$$

The right-hand side $F(v)=\int_\Omega fv\,dx$ is bounded as in Example 2.
Lax-Milgram gives a unique weak solution. The positive zeroth-order term
improves coercivity because it controls both the function and its gradient.

### Example 4: Why Pure Neumann Poisson Is Not Coercive on $H^1$

**Problem.** Consider

$$
-\Delta u=f,\qquad \frac{\partial u}{\partial n}=0 \text{ on }\partial\Omega.
$$

Explain why the natural bilinear form is not coercive on $H^1(\Omega)$.

**Solution.** The natural weak form uses

$$
a(u,v)=\int_\Omega \nabla u\cdot\nabla v\,dx.
$$

If $v$ is constant, then $\nabla v=0$ and hence

$$
a(v,v)=0.
$$

But a nonzero constant has positive $H^1$ norm:

$$
\|v\|_{H^1}^2=\|v\|_2^2>0.
$$

So no $\alpha>0$ can satisfy

$$
a(v,v)\ge \alpha\|v\|_{H^1}^2
$$

for all $v\in H^1(\Omega)$. The issue is not a technicality. Neumann Poisson
solutions are only unique up to constants, and a compatibility condition

$$
\int_\Omega f\,dx=0
$$

is needed. Coercivity is recovered on the quotient space
$H^1(\Omega)/\mathbb R$ or on the subspace of mean-zero functions.

### Example 5: Galerkin Approximation and Ce'a's Lemma

**Problem.** Let $V_h\subset V$ be a finite-dimensional subspace. Suppose
$u\in V$ solves

$$
a(u,v)=F(v)\qquad\text{for all }v\in V,
$$

and $u_h\in V_h$ solves

$$
a(u_h,v_h)=F(v_h)\qquad\text{for all }v_h\in V_h.
$$

Assume $a$ is continuous with constant $M$ and coercive with constant
$\alpha$. Prove

$$
\|u-u_h\|_V\le \frac{M}{\alpha}
\inf_{w_h\in V_h}\|u-w_h\|_V.
$$

**Solution.** Subtract the continuous and discrete equations. For all
$v_h\in V_h$,

$$
a(u-u_h,v_h)=0.
$$

This is Galerkin orthogonality. Fix any $w_h\in V_h$. Since $w_h-u_h\in V_h$,

$$
a(u-u_h,w_h-u_h)=0.
$$

Then

$$
a(u-u_h,u-u_h)
=a(u-u_h,u-w_h)+a(u-u_h,w_h-u_h)
=a(u-u_h,u-w_h).
$$

By coercivity and continuity,

$$
\alpha\|u-u_h\|_V^2
\le a(u-u_h,u-u_h)
=a(u-u_h,u-w_h)
\le M\|u-u_h\|_V\|u-w_h\|_V.
$$

If $u=u_h$, the estimate is trivial. Otherwise divide by
$\|u-u_h\|_V$:

$$
\|u-u_h\|_V\le \frac{M}{\alpha}\|u-w_h\|_V.
$$

Since $w_h$ was arbitrary, take the infimum over $V_h$. This theorem says the
Galerkin solution is, up to the conditioning constant $M/\alpha$, as good as
the best approximation available in the finite-dimensional space.

## 6. Common Mistakes

1. **Confusing weak and classical derivatives.** A weak derivative is defined
   by integration against all test functions. It need not exist pointwise.

2. **Forgetting the boundary condition hidden in $H_0^1$.** The zero boundary
   condition is not imposed pointwise in the interior equation; it is built
   into the space.

3. **Using Poincare without checking the space.** Poincare's inequality holds
   on $H_0^1(\Omega)$ and on mean-zero subspaces, but not on all of
   $H^1(\Omega)$.

4. **Calling every positive form coercive.** Coercivity must control the full
   norm of the space. Nonnegative energy may still have flat directions.

5. **Skipping boundedness of the right-hand side.** Lax-Milgram requires
   $F\in V'$. Checking the PDE residual is not enough.

6. **Assuming weak solutions are always smooth.** Regularity is a separate
   theorem. It depends on the domain, coefficients, boundary data, and right
   side.

## 7. Practice Problems with Solutions

### Problem 1

Show that if $u\in C^1(\Omega)$, then its classical derivative is also its weak
derivative.

**Solution.** For $\varphi\in C_c^\infty(\Omega)$, integration by parts gives

$$
\int_\Omega D_i u\,\varphi\,dx
=-\int_\Omega u\,D_i\varphi\,dx,
$$

because $\varphi$ vanishes near the boundary of its support. Thus the
classical derivative satisfies the defining identity for the weak derivative.

### Problem 2

Let $u(x)=x_+=\max(x,0)$ on $(-1,1)$. Find $u'$ weakly.

**Solution.** The candidate derivative is $0$ for $x<0$ and $1$ for $x>0$.
Splitting the integral at $0$,

$$
\int_{-1}^1 x_+\varphi'\,dx=\int_0^1 x\varphi'\,dx
=-\int_0^1\varphi\,dx.
$$

Hence

$$
-\int_{-1}^1x_+\varphi'\,dx
=\int_0^1\varphi\,dx,
$$

so $u'=\mathbf 1_{(0,1)}$ weakly.

### Problem 3

Prove that $F(v)=\int_0^1 xv(x)\,dx$ is bounded on $H_0^1(0,1)$.

**Solution.** By Cauchy-Schwarz,

$$
|F(v)|\le \|x\|_{L^2(0,1)}\|v\|_{L^2(0,1)}.
$$

Since $v\in H_0^1(0,1)$, Poincare gives $\|v\|_2\le C\|v'\|_2$. Therefore

$$
|F(v)|\le C\|x\|_2\|v\|_{H^1}.
$$

Thus $F\in (H_0^1)'$.

### Problem 4

For $V=H_0^1(0,1)$, show that

$$
a(u,v)=\int_0^1 u'v'\,dx+\int_0^1 uv\,dx
$$

is coercive.

**Solution.** For $v\in V$,

$$
a(v,v)=\|v'\|_2^2+\|v\|_2^2=\|v\|_{H^1}^2.
$$

Thus coercivity holds with $\alpha=1$ in the standard $H^1$ norm.

### Problem 5

Let $a(u,v)=\int_0^1 u'v'\,dx$ on $H^1(0,1)$. Is $a$ coercive?

**Solution.** No. If $v(x)=1$, then $a(v,v)=0$, but
$\|v\|_{H^1}=\|1\|_{L^2}=1$. Hence no positive coercivity constant can exist.

### Problem 6

Derive the weak form of

$$
-u''+3u=f,\qquad u(0)=u(1)=0.
$$

**Solution.** Multiply by $v\in H_0^1(0,1)$ and integrate by parts:

$$
\int_0^1 u'v'\,dx+3\int_0^1 uv\,dx
=\int_0^1 fv\,dx.
$$

The weak solution is $u\in H_0^1(0,1)$ satisfying this identity for all
$v\in H_0^1(0,1)$.

### Problem 7

Assume $q\in L^\infty(\Omega)$ and $q(x)\ge 0$. Is

$$
a(u,v)=\int_\Omega \nabla u\cdot\nabla v\,dx+\int_\Omega quv\,dx
$$

coercive on $H_0^1(\Omega)$?

**Solution.** Yes. Since $q\ge 0$,

$$
a(v,v)\ge \|\nabla v\|_2^2.
$$

On $H_0^1(\Omega)$, Poincare implies $\|\nabla v\|_2^2$ controls the full
$H^1$ norm up to a constant. Therefore $a$ is coercive.

### Problem 8

Why does $f\in H^{-1}(\Omega)$ suffice for the Dirichlet Poisson problem?

**Solution.** The weak problem only needs the right-hand side to be a bounded
linear functional on $H_0^1(\Omega)$. By definition, $H^{-1}(\Omega)$ is the
dual of $H_0^1(\Omega)$, so $f(v)$ is meaningful and bounded for all test
functions $v\in H_0^1(\Omega)$. Lax-Milgram then applies.

### Problem 9

Let $u_h$ be the Galerkin approximation in $V_h$. Prove Galerkin
orthogonality.

**Solution.** The continuous solution satisfies $a(u,v_h)=F(v_h)$ for every
$v_h\in V_h$ because $V_h\subset V$. The discrete solution satisfies
$a(u_h,v_h)=F(v_h)$ for every $v_h\in V_h$. Subtracting gives

$$
a(u-u_h,v_h)=0\qquad\text{for all }v_h\in V_h.
$$

### Problem 10

Suppose $a$ is symmetric and coercive. Show that the weak solution minimizes
$J(v)=\frac12a(v,v)-F(v)$.

**Solution.** Let $u$ solve $a(u,w)=F(w)$ for all $w\in V$. For any $v=u+w$,

$$
J(u+w)-J(u)
=\frac12a(w,w)+a(u,w)-F(w).
$$

Since $a(u,w)=F(w)$, this becomes

$$
J(u+w)-J(u)=\frac12a(w,w)\ge \frac{\alpha}{2}\|w\|_V^2\ge 0.
$$

Thus $u$ is the unique minimizer.

## 8. Connections

### Functional Analysis

Sobolev weak formulations are Hilbert-space operator equations. The map
$u\mapsto a(u,\cdot)$ is an operator from $V$ to $V'$. Lax-Milgram is a
bounded-inverse theorem for coercive operators. This connects PDE theory to
Riesz representation, dual spaces, closed range arguments, and spectral
properties of self-adjoint operators.

### Numerical Analysis

Finite element methods are finite-dimensional shadows of the weak problem.
Galerkin methods choose a subspace $V_h\subset V$ and solve the same weak
equation there. Coercivity gives stability, continuity gives boundedness, and
approximation theory gives convergence rates. This is why Ce'a's lemma is one
of the central theorems of finite element analysis.

### Optimization

When the bilinear form is symmetric, the PDE is the Euler-Lagrange equation of
a convex energy. Solving the PDE is equivalent to minimizing a quadratic
functional. Gradient descent, conjugate gradients, and multigrid can all be
understood as optimization algorithms for this energy.

### Probability and Stochastic Processes

Dirichlet energy also appears in Markov processes. Harmonic functions minimize
energy, and the Laplacian is the generator of Brownian motion. Weak solutions
connect to hitting probabilities, Green's functions, and Dirichlet forms.

### Geometry

On manifolds, the Laplacian becomes the Laplace-Beltrami operator and Sobolev
spaces are defined using charts or covariant derivatives. The same weak
formulation survives, but the geometry changes the measure, gradient, and
boundary terms.

## 9. How to Study This Topic

The best way to learn weak PDE theory is to keep two pictures active at the
same time. The first picture is analytic: define the correct space, prove
boundedness, prove coercivity, and apply Lax-Milgram. The second picture is
computational: discretize the energy and watch a positive definite matrix
appear. If the discrete matrix has a small eigenvalue, the numerical problem
will be poorly conditioned; if the continuous form lacks coercivity, the PDE is
not well posed without additional constraints.

Whenever you meet a new elliptic problem, ask four questions:

1. What is the natural energy space?
2. What is the bilinear form?
3. Which inequality supplies coercivity?
4. What finite-dimensional approximation would inherit the same structure?

Those four questions are the spine of this subject.
