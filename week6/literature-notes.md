# Week 6 Literature Notes

Research topic: physics-informed neural networks for incompressible and
Navier-Stokes fluid simulation.

Source set: recent PINN papers saved locally under `/home/agizz/Desktop/PINN`
and `/home/agizz/Downloads`, with the final citation library saved in
`week6/references.bib`.

## Zotero MCP Query

### Exact query sent

Using the Zotero MCP, list all papers in my library on physics-informed neural
networks for incompressible/Navier-Stokes fluid simulation as a numbered list
with year, title, and one-sentence description.

### Saved response

Here are 6 relevant entries I found in your Zotero library:

1. **2022, "When and why PINNs fail to train: A neural tangent kernel
   perspective."** This paper analyzes PINN training failure modes through the
   neural tangent kernel framework.

2. **2024, "Finite difference physics-informed neural networks enable improved
   solution accuracy of the Navier-Stokes equations."** This work improves
   Navier-Stokes PINN accuracy by incorporating finite-difference-inspired
   structure.

3. **2025, "Physics-informed neural networks with hard and soft boundary
   conditions for problems in fluid dynamics."** This thesis studies PINNs with
   hard and soft boundary-condition enforcement for fluid-dynamics problems.

4. **2026, "Scale-PINN: Learning Efficient Physics-Informed Neural Networks
   Through Sequential Correction."** This paper proposes a sequential-correction
   strategy to make PINNs more efficient and scalable.

5. **2026, "Bridging Computational Fluid Dynamics Algorithm and
   Physics-Informed Learning: SIMPLE-PINN for Incompressible Navier-Stokes
   Equations."** This paper combines CFD algorithmic ideas with PINNs to solve
   incompressible Navier-Stokes equations.

6. **2026, "FFV-PINN: A Fast Physics-Informed Neural Network with Simplified
   Finite Volume Discretization and Residual Correction."** This work develops
   a faster PINN variant using simplified finite-volume discretization and
   residual correction.

## NotebookLM Query

### Exact query sent

Using my NotebookLM library of recent PINN papers for incompressible and
Navier-Stokes fluid simulation, identify the 3 main research themes across the
uploaded papers and the main open questions in the area.

### Saved response

#### Theme 1: Hybridizing PINNs with Traditional Numerical Methods

A major trend across recent research is the integration of classical
computational fluid dynamics (CFD) algorithms into the PINN framework to
improve physical consistency, convergence speed, and the ability to solve
high-Reynolds-number flows.

- **Finite Difference and Domain Decomposition:** Finite difference-based PINNs
  replace automatic differentiation with finite difference methods to
  discretize derivative terms. Combined with domain decomposition methods, this
  approach successfully generates accurate secondary vortices in lid-driven
  cavity flows at Re = 1000 without needing labeled data.

- **Iterative Residual Correction:** Inspired by iterative numerical solvers,
  the Scale-PINN framework directly incorporates sequential
  residual-correction mechanisms into the PINN loss formulation. This smooths
  the PDE residual landscape, cutting training times for Navier-Stokes
  simulations, such as reducing training from hours to sub-2 minutes for a
  Re = 3200 cavity flow, while maintaining high accuracy.

- **Finite Volume Method and Velocity-Pressure Coupling:** To enforce the
  divergence-free condition and conservation laws, researchers have integrated
  finite volume methods into PINNs. SIMPLE-PINN derives velocity and pressure
  correction loss terms inspired by the classical SIMPLE algorithm, while
  FFV-PINN uses simplified finite volume discretization for the convection term
  plus residual correction loss. These methods enable data-free solutions for
  highly nonlinear cavity flows up to Re = 10000. For complex or irregular
  geometries, hybrid methods often use automatic differentiation near wall
  boundary points while using finite volume methods in the interior domain.

#### Theme 2: Architectural Innovations and Scaling for Deep PINNs

Standard multilayer perceptron architectures often exhibit training pathologies
when scaling to deeper networks, largely due to poor initialization of network
derivatives that destabilizes PDE residual minimization.

- **PirateNets:** Physics-Informed Residual Adaptive Networks use adaptive
  residual connections so the network can be initialized as a shallow network
  and progressively deepen during training. This architecture integrates
  physical inductive biases and yields high accuracy on complex fluid
  benchmarks without suffering from the instabilities of deep MLPs.

- **Feature Embeddings and Weight Factorization:** Random Fourier feature
  embeddings are used to mitigate spectral bias, where the network struggles
  to learn high-frequency functions. Random weight factorization and modified
  MLPs also enhance the network's ability to represent the sharp gradients
  found in fluid flows.

#### Theme 3: Advanced Training Strategies, Loss Balancing, and Boundary Enforcement

The highly non-convex loss landscape of fluid PDEs often leads to unbalanced
back-propagated gradients and premature convergence to erroneous solutions.

- **Neural Tangent Kernel Weighting:** NTK analysis shows a discrepancy in the
  convergence rates of different loss components. Adaptive gradient descent
  algorithms using NTK eigenvalues can calibrate the weights of PDE, boundary,
  and initial-condition losses to stabilize training.

- **Causal and Curriculum Training:** Standard PINNs can violate temporal
  causality by minimizing PDE residuals simultaneously across time. Causal
  training assigns sequential temporal weights so the network learns flow
  evolution chronologically. Curriculum training gradually increases problem
  complexity, such as starting with low Reynolds number and progressively
  increasing it, preventing the model from getting trapped in local minima.

- **Hard vs. Soft Boundary Conditions:** Standard PINNs use soft boundary
  conditions by adding boundary residuals as penalties in the loss function,
  which can struggle near corner singularities. Hard boundary constraints use
  specialized trial functions or exact periodic layers so boundaries are
  satisfied to machine precision, improving results independently of the loss
  optimization process.

### Main open questions

1. **Resolving fine-scale multiscale structures.** Modern PINNs can simulate
   high-Reynolds-number flows up to Re = 10000 or 20000, but they still
   struggle to accurately capture localized turbulent vortex structures such
   as higher-order corner eddies in cavity flows. Adaptive refinement,
   multigrid ideas, and weighting of small-scale solutions remain open targets.

2. **Training time for unsteady flows.** Even rapid frameworks such as
   FFV-PINN and Scale-PINN can remain slower than traditional CFD for long-term
   transient flow simulations. Adaptive time stepping or operator splitting
   ideas such as PISO may be needed to improve temporal efficiency.

3. **Higher-order discretizations in hybrid models.** Current FVM-PINN hybrid
   models rely on simplified or lower-order discretization schemes to balance
   complexity. Extending these methods to higher-order finite volume
   interpolation without overwhelming computational cost remains a critical
   next step.

4. **Optimal collocation point distribution.** Despite empirical successes,
   there is still little rigorous theory for determining the number and
   distribution of collocation points needed to prevent overfitting while
   enforcing physical constraints globally across the domain.
