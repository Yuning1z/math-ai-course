# Introduction Draft

Physics-informed neural networks (PINNs) promise a flexible route for solving
partial differential equations by training neural networks against governing
equation residuals, boundary conditions, and available data. This promise is
especially attractive in incompressible fluid dynamics, where the
Navier-Stokes equations generate difficult forward and inverse problems and
where labeled simulation data can be expensive. Yet fluid mechanics also
exposes many of the weaknesses of standard PINNs: boundary layers, corner
singularities, pressure-velocity coupling, secondary vortices, stiffness across
loss terms, and long-time instability. The recent PINN literature therefore
shows a movement away from purely generic neural residual minimization and
toward methods that incorporate numerical-analysis structure.

A first line of work studies why PINNs are hard to optimize. Wang, Yu, and
Perdikaris analyze PINNs through the neural tangent kernel and show that
different components of the training loss can converge at dramatically
different rates, producing stiffness and failure even when the network is
expressive (Wang, Yu, and Perdikaris, 2022). The practical consequence is that
architecture, scaling, sampling, and loss balancing are not secondary
implementation details; they determine whether the PDE, boundary, and data
terms are learned together. Wang, Sankaran, Wang, and Perdikaris turn this
diagnosis into a practical training guide, emphasizing nondimensionalization,
Fourier features, random weight factorization, curriculum strategies, and
reproducible benchmark protocols (Wang, Sankaran, Wang, and Perdikaris, 2023).
PirateNets continue this thread by modifying the network architecture itself,
using residual adaptive networks to make deeper PINNs trainable and accurate
on PDE benchmarks (Wang, Li, Chen, and Perdikaris, 2024).

A second line of work brings classical numerical discretization and solver
ideas directly into PINNs for fluid problems. Roy, Duerr, Bueck, and Sundar
use finite-difference physics-informed neural networks to improve
Navier-Stokes solutions in lid-driven cavity flow, with particular attention
to wall regions and secondary vortices (Roy, Duerr, Bueck, and Sundar, 2024).
Scale-PINN imports the residual-correction principle from iterative numerical
methods into the PINN loss, achieving faster convergence on stiff
fluid-dynamics benchmarks (Chiu et al., 2026). SIMPLE-PINN goes further by
adapting the SIMPLE velocity-pressure coupling idea from computational fluid
dynamics to construct correction losses for incompressible Navier-Stokes
equations (Wei et al., 2026a). FFV-PINN similarly embeds finite-volume
intuition into the training objective by using simplified finite-volume
discretization and residual correction for stable fluid simulation (Wei et
al., 2026b).

Boundary conditions form a third major challenge. Sheikholeslami compares hard
and soft boundary enforcement for fluid-dynamics PINNs and finds that exact
enforcement can satisfy constraints but does not automatically improve
accuracy near difficult boundary structures such as lid-driven cavity corners
(Sheikholeslami, 2025). This reflects a broader lesson: incompressible-flow
PINNs are not judged only by small residuals, but by whether they capture the
correct wall behavior, pressure field, vortical structure, and stability
properties of the fluid solution.

Across these papers, two open problems stand out. First, the field still needs
reliable error certification and fair benchmarking against finite difference,
finite volume, finite element, multigrid, and CFD baselines under matched
accuracy and compute budgets. Second, the field needs a principled separation
between neural approximation error, optimization error, and discretization
error in hybrid PINN-CFD methods. Without this separation, it is hard to know
whether a reported improvement comes from better architecture, better
conditioning, better embedded numerical structure, or problem-specific tuning.

In this paper, we propose to study incompressible-flow PINNs as hybrid
iterative numerical solvers: neural trial functions trained with
solver-informed residual corrections, boundary-aware weighting, and
classical-error diagnostics, with the goal of designing PINN methods whose
accuracy, stability, and computational cost can be compared transparently with
established CFD algorithms.
