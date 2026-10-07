# Module 06: N-body simulations and numerical Python

**Difficulty:** Medium to hard. **Time:** about 3 weeks.

## Goal

Build and validate your own N-body machinery (direct summation, a tree code, a high-order integrator), generate initial conditions for spheres and disks, write the analysis pipeline that every later module reuses, and know when to hand the work to an optimized external code.

## Prerequisites

Modules 02, 03 and 05.

## Reading

- **B&T:** the sections on numerical orbit integration (Ch. 3), and the parts of the book that discuss how N-body methods relate to the collisionless Boltzmann equation. Check your table of contents for any section on numerical methods.
- **S&G topic:** computer simulations of galaxies.
- **Papers and reviews:** Dehnen and Read (2011), *N-body simulations of gravitational dynamics*; Barnes and Hut (1986), the tree algorithm; Makino and Aarseth (1992), the Hermite scheme with block time steps; Hernquist (1993), initial conditions for disk galaxies; Athanassoula, Fady, Lambert and Bosma (2000), on numerical effects in disk simulations.
- **Book:** Aarseth, *Gravitational N-Body Simulations* (for the direct-summation tradition).

## Concepts

1. **Why N-body works.** A system of $N$ particles samples the collisionless Boltzmann flow. Each particle is a Monte Carlo sample of phase space, not a star.
2. **Softening.** Replace $1/r^2$ by a softened force with length $\varepsilon$ to suppress two-body relaxation and singularities in collisionless simulations. In cluster simulations (Module 12), you want to keep the true point-mass force and handle close encounters carefully.
3. **Integrators.** Leapfrog (second order, symplectic, with a fixed or time-symmetric variable step), Hermite (fourth order, uses the jerk), and block individual time steps.
4. **Force solvers.** Direct summation ($O(N^2)$), Barnes-Hut tree ($O(N\log N)$), particle-mesh or FFT ($O(N+M\log M)$), and fast multipole.
5. **Diagnostics.** Energy, linear and angular momentum, virial ratio, Lagrangian radii, force error, convergence in $N$.

## Key formulas

Softened (Plummer) acceleration on particle $i$:

$$\mathbf a_i = -G\sum_{j\ne i}\frac{m_j\,(\mathbf r_i-\mathbf r_j)}{\left(|\mathbf r_i-\mathbf r_j|^2+\varepsilon^2\right)^{3/2}}$$

Barnes-Hut opening criterion: treat a cell of size $s$ at distance $d$ as a single mass if $s/d<\theta$, with $\theta\sim0.5$ to $0.7$. The force error grows with $\theta$.

**Plummer initial conditions** (Aarseth, Henon and Wielen algorithm), for total mass $M$ and scale $b$:

1. Draw $X_1\in(0,1)$ and set $r=b\,/\sqrt{X_1^{-2/3}-1}$ (inversion of $M(<r)$). Place the particle at a random direction.
2. Draw $q\in(0,1)$ and $Y\in(0,0.1)$ until $Y<q^2(1-q^2)^{7/2}$ (rejection sampling, the maximum of the function is about 0.092). Set $v=q\,v_{\rm esc}$ with $v_{\rm esc}=\sqrt2\,(1+r^2/b^2)^{-1/4}\sqrt{GM/b}$, with a random direction.
3. Rescale to the center of mass frame.

**Disk initial conditions** (outline): exponential surface density, rotation speed from the potential, radial dispersion from a chosen Toomre $Q$, azimuthal dispersion from the epicycle ratio, vertical dispersion from the isothermal sheet. Hernquist (1993) gives the recipe. Better: use a distribution-function-based generator (`AGAMA`'s DF models and samplers, `GalIC`, `DICE`) which produces a more self-consistent equilibrium. Check by evolving the model in isolation first.

## A minimal direct-summation kernel

```python
import numpy as np

def acc_direct(pos, mass, eps, G=4.30091e-6):
    # pos: (N, 3) in kpc, mass: (N,) in Msun -> acc in (km/s)^2 / kpc
    dx = pos[None, :, :] - pos[:, None, :]            # (N, N, 3): r_j - r_i
    r2 = (dx**2).sum(-1) + eps**2
    inv_r3 = r2**-1.5
    np.fill_diagonal(inv_r3, 0.0)
    return G * (dx * (mass[None, :, None] * inv_r3[:, :, None])).sum(1)
```

This needs $O(N^2)$ memory, so it is only good up to $N\sim10^4$. Process in blocks or move to Numba:

```python
from numba import njit, prange

@njit(parallel=True, fastmath=True)
def acc_numba(pos, mass, eps2, G):
    n = pos.shape[0]
    acc = np.zeros_like(pos)
    for i in prange(n):
        ax = ay = az = 0.0
        for j in range(n):
            if j == i:
                continue
            dx = pos[j, 0] - pos[i, 0]
            dy = pos[j, 1] - pos[i, 1]
            dz = pos[j, 2] - pos[i, 2]
            r2 = dx*dx + dy*dy + dz*dz + eps2
            f = mass[j] / (r2 * np.sqrt(r2))
            ax += f*dx; ay += f*dy; az += f*dz
        acc[i, 0] = G*ax; acc[i, 1] = G*ay; acc[i, 2] = G*az
    return acc
```

## Hands-on problems

**1. [E] Direct summation + leapfrog.** Implement the code above with kick-drift-kick leapfrog. Test on two bodies (Kepler orbit) and on a three-body figure-eight orbit. Energy, momentum and angular momentum must be conserved to the expected accuracy.

**2. [E] Plummer sphere in equilibrium.** Generate $N=10^3,10^4$ Plummer spheres with the algorithm above. Check the virial ratio $2K/|W|\approx1$ and that the half-mass radius is $1.305\,b$. Then evolve for 20 crossing times with softening $\varepsilon=0.05\,b$, and plot Lagrangian radii (10, 25, 50, 75, 90 percent) against time. They should stay constant apart from noise. Quantify the relative energy drift.

**3. [M] Softening study.** For $N=10^4$, vary $\varepsilon$ over a factor of 30 and measure (a) energy conservation, (b) the evolution of the core radius, and (c) the force error against the exact analytic Plummer force. Plot error against $\varepsilon$. Find the scaling of the optimum with $N$ and compare with Dehnen (2001) and Athanassoula et al. (2000).

**4. [M] Performance.** Time the NumPy version, the Numba version (with and without `parallel=True`) and, if you have a GPU, a JAX version for $N=10^3$ to $10^5$. Plot time against $N$ and fit the exponent. Report the number of pair interactions per second.

**5. [M] A Barnes-Hut tree.** Write an octree in Numba (arrays of child indices, centers of mass and sizes). Compute forces with opening angles $\theta=0.3,0.5,0.7,1.0$ for a $10^5$ particle Plummer model. Plot the RMS relative force error against $\theta$ and the time against $\theta$. Compare with a published package (`pytreegrav`, NEMO's `gyrfalcON`, or another tree code; verify it is maintained) for speed and accuracy.

**6. [M] Hermite integrator.** Implement the fourth-order Hermite scheme with a shared time step first, then with individual block time steps (powers of two) for $N=1000$. Compare accuracy and cost with leapfrog for a Plummer cluster with a few binaries added.

**7. [M] Snapshot I/O and reproducibility.** Define a snapshot format (HDF5 with units in the header, a git hash, the random seed, and the configuration YAML). Write `nbody/io.py` with read/write functions and a test that round-trips a snapshot exactly.

**8. [H] Isolated disk plus halo.** Create a disk plus live Hernquist or NFW halo model of Milky Way scale (halo mass about $10^{12}M_\odot$ truncated, disk mass about $5\times10^{10}M_\odot$, scale length 2.6 kpc, thickness 0.3 kpc, Toomre $Q$ about 1.5 at 2.5 scale lengths). Use `AGAMA` or `GalIC` for the equilibrium, or implement Hernquist (1993) yourself. Run with $N\ge2\times10^5$ (a tree code external to Python is recommended; use your own code only for smaller tests) and check that the model is stable for a few dynamical times if $Q$ is large and no bar can form (try $Q=3$ and a massive halo as a control).

**9. [H] Analysis pipeline.** Write `nbody/analysis.py` to compute, for a snapshot: the radial profiles of density, rotation speed and dispersions; the Fourier amplitudes $A_m(R)=\left|\sum_j m_j e^{im\varphi_j}\right|/\sum_j m_j$ in annuli, the $m=2$ phase and the bar angle; the angular-momentum profile and the total angular momentum of the disk and of the halo separately. You will use this heavily in Modules 07 and 10.

**10. [H] Convergence in $N$.** Evolve the same model with $N=5\times10^4,10^5,2\times10^5,4\times10^5$ and show how the quantity of interest (for example, the time to bar formation, or the final bar length) varies. Report the error from particle noise.

## Checks

- Plummer: virial ratio $1\pm0.02$, half-mass radius $1.305\,b$ to 3 percent, relative energy drift below $10^{-4}$ over 20 crossing times in leapfrog with a suitable step.
- Tree force error of about 1 percent or lower at $\theta\approx0.5$ (typical of the algorithm; depends on order of the multipole expansion).
- Snapshot round-trip exactness.
- The isolated stable disk keeps its radial profiles within a few percent for several dynamical times.

## Pitfalls

- Using adaptive time steps without time-symmetry, which breaks the symplectic structure of leapfrog and degrades energy conservation.
- Starting a disk in a non-equilibrium state, then attributing the transient to physics.
- Softening too small, giving artificial two-body relaxation that heats the disk and causes spurious bar and halo evolution (Module 10).
- Python loops over particles. Vectorize or use Numba.
- Float32 for long runs: round-off will dominate the energy error.

## Gate questions

1. What does an N-body particle represent in a galaxy simulation, and in a globular cluster simulation? Why does that change how you choose the softening?
2. Why is leapfrog with a fixed time step usually preferred to a higher-order non-symplectic scheme for galaxy simulations?
3. What is the main source of noise in an N-body bar simulation, and how would you diagnose it?

## Deliverable

`nbody/` with direct, tree and Hermite integrators, initial-condition generators, snapshot I/O and analysis tools, tests, and `notebooks/06_nbody.ipynb` with the Plummer, softening, performance and tree-accuracy plots.
