#%% Cell 1: Solve a 1D Dirichlet Poisson problem by P1 finite elements
from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import numpy as np
import matplotlib.pyplot as plt

try:
    BASE = Path(__file__).resolve().parent
except NameError:
    BASE = Path.cwd() / "capstone"

FIG = BASE / "figures"
FIG.mkdir(parents=True, exist_ok=True)


def exact_solution(x):
    return np.sin(np.pi * x)


def exact_derivative(x):
    return np.pi * np.cos(np.pi * x)


def forcing(x):
    return (np.pi**2) * np.sin(np.pi * x)


def assemble_p1_fem(n_elements):
    """Assemble P1 FEM matrices for -u''=f on (0,1), u(0)=u(1)=0."""
    h = 1.0 / n_elements
    n_unknowns = n_elements - 1
    K = np.zeros((n_unknowns, n_unknowns))
    M = np.zeros((n_unknowns, n_unknowns))
    F = np.zeros(n_unknowns)

    local_K = np.array([[1.0, -1.0], [-1.0, 1.0]]) / h
    local_M = h * np.array([[2.0, 1.0], [1.0, 2.0]]) / 6.0

    gauss_ref = np.array([0.5 - 1.0 / (2.0 * np.sqrt(3.0)), 0.5 + 1.0 / (2.0 * np.sqrt(3.0))])
    gauss_w = np.array([0.5, 0.5])

    for element in range(n_elements):
        x_left = element * h
        global_nodes = [element, element + 1]

        for a in range(2):
            ia = global_nodes[a] - 1
            if 0 <= ia < n_unknowns:
                for b in range(2):
                    ib = global_nodes[b] - 1
                    if 0 <= ib < n_unknowns:
                        K[ia, ib] += local_K[a, b]
                        M[ia, ib] += local_M[a, b]

        for xi, w in zip(gauss_ref, gauss_w):
            xq = x_left + h * xi
            phi = np.array([1.0 - xi, xi])
            for a in range(2):
                ia = global_nodes[a] - 1
                if 0 <= ia < n_unknowns:
                    F[ia] += h * w * forcing(xq) * phi[a]

    return K, M, F


def nodal_vector_to_full(c):
    return np.concatenate(([0.0], c, [0.0]))


def p1_fem_errors(n_elements, coeffs):
    """Compute true quadrature-based L2 and H1-seminorm errors for P1 FEM."""
    full = nodal_vector_to_full(coeffs)
    h = 1.0 / n_elements
    gauss_ref = np.array([0.5 - 1.0 / (2.0 * np.sqrt(3.0)), 0.5 + 1.0 / (2.0 * np.sqrt(3.0))])
    gauss_w = np.array([0.5, 0.5])
    l2_sq = 0.0
    h1_sq = 0.0

    for element in range(n_elements):
        x_left = element * h
        uh_left = full[element]
        uh_right = full[element + 1]
        duh = (uh_right - uh_left) / h

        for xi, w in zip(gauss_ref, gauss_w):
            xq = x_left + h * xi
            uh = (1.0 - xi) * uh_left + xi * uh_right
            l2_sq += h * w * (uh - exact_solution(xq)) ** 2
            h1_sq += h * w * (duh - exact_derivative(xq)) ** 2

    return np.sqrt(l2_sq), np.sqrt(h1_sq)


n_elements = 80
K, M, F = assemble_p1_fem(n_elements)
c = np.linalg.solve(K, F)
nodes = np.linspace(0.0, 1.0, n_elements + 1)
u_nodes = nodal_vector_to_full(c)
u_exact_nodes = exact_solution(nodes)

l2_error, h1_error = p1_fem_errors(n_elements, c)

print("Cell 1: P1 finite elements approximate the weak Dirichlet Poisson solution.")
print(f"Elements: {n_elements}")
print(f"Quadrature L2 error: {l2_error:.3e}")
print(f"Quadrature H1 seminorm error: {h1_error:.3e}")

plt.figure(figsize=(7, 4))
plt.plot(nodes, u_exact_nodes, label="exact $\\sin(\\pi x)$", linewidth=2)
plt.plot(nodes, u_nodes, "o--", markersize=3, label="P1 FEM solution")
plt.xlabel("x")
plt.ylabel("u")
plt.title("P1 FEM for $-u''=\\pi^2\\sin(\\pi x)$ with $u=0$")
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "poisson_solution.png", dpi=160)
plt.close()

#%% Cell 2: Convergence study in L2 and H1 seminorms
def fem_errors(n_elements):
    K, M, F = assemble_p1_fem(n_elements)
    c = np.linalg.solve(K, F)
    return p1_fem_errors(n_elements, c)


element_counts = np.array([10, 20, 40, 80, 160, 320])
hs = 1.0 / element_counts
l2_errors = []
h1_errors = []

for n in element_counts:
    l2, h1 = fem_errors(n)
    l2_errors.append(l2)
    h1_errors.append(h1)

l2_errors = np.array(l2_errors)
h1_errors = np.array(h1_errors)
l2_rate = np.polyfit(np.log(hs), np.log(l2_errors), 1)[0]
h1_rate = np.polyfit(np.log(hs), np.log(h1_errors), 1)[0]

print("\nCell 2: P1 Galerkin refinement shows the expected FEM rates.")
print("Element counts:", element_counts)
print("L2 errors:", l2_errors)
print("H1 seminorm errors:", h1_errors)
print(f"Estimated L2 convergence rate: {l2_rate:.2f}")
print(f"Estimated H1 convergence rate: {h1_rate:.2f}")

plt.figure(figsize=(7, 4))
plt.loglog(hs, l2_errors, "o-", label=f"L2 error, slope {l2_rate:.2f}")
plt.loglog(hs, h1_errors, "s-", label=f"H1 error, slope {h1_rate:.2f}")
plt.gca().invert_xaxis()
plt.xlabel("mesh size h")
plt.ylabel("error")
plt.title("P1 finite element convergence")
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "poisson_convergence.png", dpi=160)
plt.close()

#%% Cell 3: Discrete Poincare constant from the generalized eigenproblem
element_counts = np.array([10, 20, 40, 80, 160])
lambda1s = []
constants = []

for n in element_counts:
    K, M, _ = assemble_p1_fem(n)
    generalized = np.linalg.solve(M, K)
    eigs = np.sort(np.real(np.linalg.eigvals(generalized)))
    lambda1 = eigs[0]
    lambda1s.append(lambda1)
    constants.append(1.0 / np.sqrt(lambda1))

lambda1s = np.array(lambda1s)
constants = np.array(constants)

print("\nCell 3: FEM coercivity is visible in the first generalized eigenvalue.")
print("First generalized eigenvalues Kx=lambda Mx:", lambda1s)
print("Discrete Poincare constants:", constants)
print(f"Continuous Poincare constant on (0,1): {1 / np.pi:.6f}")

plt.figure(figsize=(7, 4))
plt.plot(element_counts, constants, "o-", label="P1 FEM constant")
plt.axhline(1 / np.pi, color="black", linestyle="--", label="$1/\\pi$")
plt.xlabel("number of elements")
plt.ylabel("$1 / \\sqrt{\\lambda_1}$")
plt.title("Poincare constant from the FEM generalized eigenproblem")
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "poincare_constant.png", dpi=160)
plt.close()

#%% Cell 4: Energy minimization viewpoint and steepest descent
n_elements = 80
K, M, F = assemble_p1_fem(n_elements)
c_star = np.linalg.solve(K, F)


def energy(c):
    return 0.5 * (c @ K @ c) - F @ c


c_iter = np.zeros_like(F)
energies = []
errors = []

for _ in range(1200):
    residual = F - K @ c_iter
    energies.append(energy(c_iter))
    errors.append(np.sqrt((c_iter - c_star) @ K @ (c_iter - c_star)))
    step = (residual @ residual) / (residual @ K @ residual)
    c_iter = c_iter + step * residual

eig_K = np.linalg.eigvalsh(K)

print("\nCell 4: steepest descent minimizes the FEM energy functional.")
print(f"Condition number of FEM stiffness matrix: {eig_K[-1] / eig_K[0]:.1f}")
print(f"Initial energy: {energies[0]:.6e}")
print(f"Final energy: {energies[-1]:.6e}")
print(f"Energy-norm distance to Galerkin solve: {errors[-1]:.3e}")

plt.figure(figsize=(7, 4))
plt.semilogy(errors)
plt.xlabel("steepest descent iteration")
plt.ylabel("$\\|c_k-c_*\\|_K$")
plt.title("Energy minimization converges to the Galerkin solution")
plt.tight_layout()
plt.savefig(FIG / "energy_descent.png", dpi=160)
plt.close()
