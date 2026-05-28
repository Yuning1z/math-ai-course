# %%
"""
Fourier series exploration for an odd square wave on [-pi, pi].

This file uses interactive Python cells to compare a discontinuous target
function with finite Fourier sine-series approximations. The final cell
computes how the L2 error changes as the highest retained Fourier mode
increases.
"""

import numpy as np
import matplotlib.pyplot as plt


def square_wave(x: np.ndarray) -> np.ndarray:
    """Return the odd square wave that is 1 on (0, pi) and -1 on (-pi, 0)."""
    values = np.where(np.sin(x) >= 0, 1.0, -1.0)
    values[np.isclose(np.sin(x), 0.0, atol=1e-12)] = 0.0
    return values


x = np.linspace(-np.pi, np.pi, 2000)
target_values = square_wave(x)

# %%
# Compute the nth partial sum of the Fourier series for the square wave.
# Only odd sine modes have nonzero coefficients for this target function.


def fourier_partial_sum(x: np.ndarray, n: int) -> np.ndarray:
    """Approximate the odd square wave using all odd Fourier modes up to n."""
    partial_sum = np.zeros_like(x, dtype=float)

    for harmonic in range(1, n + 1, 2):
        partial_sum += np.sin(harmonic * x) / harmonic

    return (4 / np.pi) * partial_sum


one_term_approximation = fourier_partial_sum(x, 1)

# %%
# Plot several partial sums against the target function to visualize
# convergence and the Gibbs overshoot near jump discontinuities.

term_counts_to_plot = [1, 3, 5, 10]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x, target_values, color="black", linewidth=2.5, label="target square wave")

for n in term_counts_to_plot:
    ax.plot(x, fourier_partial_sum(x, n), linewidth=1.5, label=f"n = {n}")

ax.set_title("Fourier partial sums for an odd square wave")
ax.set_xlabel("x")
ax.set_ylabel("function value")
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()

# %%
# Plot the L2 error between the nth partial sum and the target function.
# The integral is approximated numerically with the trapezoidal rule.


def l2_error(x: np.ndarray, n: int) -> float:
    """Compute ||S_n - f||_2 over [-pi, pi] using numerical quadrature."""
    error_values = fourier_partial_sum(x, n) - square_wave(x)
    integral = np.trapezoid(error_values**2, x)
    return float(np.sqrt(integral))


term_counts = np.arange(1, 101)
errors = np.array([l2_error(x, n) for n in term_counts])

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(term_counts, errors, color="tab:blue", linewidth=2)
ax.set_title("L2 error of Fourier partial sums")
ax.set_xlabel("highest Fourier mode n")
ax.set_ylabel(r"$\|S_n - f\|_{L^2}$")
ax.grid(True, alpha=0.3)
plt.show()
