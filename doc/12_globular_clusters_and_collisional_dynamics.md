# Module 12: Globular clusters and collisional dynamics

**Difficulty:** Hard. **Time:** about 3 weeks.

## Goal

Understand the physics of a system where two-body relaxation matters: relaxation time, King models, mass segregation, evaporation and tidal truncation, core collapse and its support by binaries. Build and run a direct N-body model of a cluster, and connect clusters to the Galaxy through their orbits and tidal tails.

## Prerequisites

Modules 03, 06 and (for the last problems) 08 and 09.

## Reading

- **B&T Ch. 6:** two-body relaxation, the relaxation time, evaporation and ejection, the Fokker-Planck approach, gravothermal instability and core collapse, mass segregation. Also **B&T Ch. 4** on the King model as a distribution function.
- **S&G topics:** globular clusters, the Galaxy's globular cluster system, dynamical friction on clusters.
- **Books:** Spitzer (1987), *Dynamical Evolution of Globular Clusters*; Heggie and Hut (2003), *The Gravitational Million-Body Problem*; Aarseth (2003) for the N-body methods.
- **Papers:** King (1966); Henon (1961, 1971) on the Monte Carlo method and energy generation; Lynden-Bell and Wood (1968) on gravothermal instability; Meylan and Heggie (1997), review; Baumgardt and Hilker (2018) on masses and structural properties of Milky Way globular clusters; Vasiliev and Baumgardt (2021) for Gaia-based cluster orbits; Pearson, Price-Whelan and Johnston (2017) on the Galactic bar and the Palomar 5 stream.

## Concepts

1. **Relaxation.** Distant encounters with many stars produce a random walk in velocity. The characteristic time is $t_{\rm relax}$ (Module 01). Over a time $t_{\rm rh}$ a typical star's orbit changes significantly.
2. **Mass segregation and equipartition.** Heavy stars lose energy to light ones and sink to the center, light stars move outward. If the heavy stars are too massive or too numerous, equipartition cannot be reached (Spitzer's instability).
3. **Evaporation and tidal truncation.** Stars with energy above the escape energy leave. In a tidal field the cluster is truncated at the Jacobi radius. Escape happens through the Lagrange points and produces tidal tails.
4. **Gravothermal instability.** Self-gravitating systems have negative specific heat: the core loses energy to the halo, contracts, becomes hotter and loses energy faster, and collapses on a timescale of order 15 half-mass relaxation times (single-mass isolated systems; verify). Energy production by binaries (formed in the dense core) stops the collapse. Henon's principle: the rate of energy generation in the core is set by the relaxation of the half-mass region, not by the details of the heat source.
5. **Observed structure.** Core, half-light and tidal radii, concentration, and the "core-collapsed" clusters, found through central surface brightness cusps.

## Key equations

Local relaxation time, with local density $\rho$ and one-dimensional dispersion $\sigma$:

$$t_{\rm relax}=\frac{0.34\,\sigma^3}{G^2\,m\,\rho\,\ln\Lambda},\qquad \ln\Lambda\approx\ln(0.11N)$$

Half-mass relaxation time (Module 01):

$$t_{\rm rh}=0.138\,\frac{N^{1/2}r_h^{3/2}}{m^{1/2}G^{1/2}\ln\Lambda}$$

**King (1966) models.** With $\Psi=(\Phi_t-\Phi)/\sigma^2$ the dimensionless relative potential and $\rho_1$ a normalization,

$$\rho(\Psi)=\rho_1\left[e^{\Psi}\,\mathrm{erf}\sqrt\Psi-\sqrt{\frac{4\Psi}{\pi}}\left(1+\frac{2\Psi}{3}\right)\right],\qquad \frac{d^2\Psi}{dx^2}+\frac2x\frac{d\Psi}{dx}=-\frac{9\rho(\Psi)}{\rho(W_0)}$$

with $x=r/r_0$ in units of the King radius $r_0=\sqrt{9\sigma^2/4\pi G\rho_0}$, boundary conditions $\Psi(0)=W_0$ and $\Psi'(0)=0$, integrated outward until $\Psi=0$, which defines the tidal radius $r_t$. The concentration is $c=\log_{10}(r_t/r_0)$. Verify the factor in the right-hand side by deriving the equation from the Poisson equation.

**Jacobi (tidal) radius** of a cluster of mass $M_c$ on a circular orbit of angular speed $\Omega$ in the host galaxy:

$$r_J=\left(\frac{GM_c}{3\Omega^2}\right)^{1/3}\ \text{(point-mass host)},\qquad r_J=\left(\frac{GM_c}{2\Omega^2}\right)^{1/3}\ \text{(isothermal host, flat rotation curve)}$$

**Plummer model virial parameters** for N-body units ($G=M=1$, $E=-1/4$): scale radius $b=3\pi/16\approx0.589$, half-mass radius $1.305\,b$.

**Core radius in simulations.** Use the density-weighted center and core radius of Casertano and Hut (1985): a local density from each star's six nearest neighbours is used as a weight.

## Hands-on problems

**1. [E] King models.** Integrate the King equation for $W_0=3,5,7,9,12$. Plot $\rho(r)$ and the projected surface density. Compute $c$, $r_t/r_0$, and the ratio of the half-mass radius to $r_0$. As a sanity check, $W_0\approx7$ gives $c\approx1.5$ (verify against King's tables), and the concentration increases with $W_0$. Compare with a Plummer profile of the same half-mass radius: where do they differ most?

**2. [E] Cluster relaxation numbers.** Using the Harris catalogue (Module 01) and Baumgardt and Hilker's (2018) mass table, compute $t_{\rm rh}$ for the Milky Way clusters and mark the core-collapsed ones from the catalogue. Is there a clear difference in $t_{\rm rh}$ between collapsed and non-collapsed clusters?

**3. [M] Direct N-body with a collapsed core.** Using your Hermite integrator with block time steps (Module 06) or an external direct-summation code (NBODY6-family, PeTar, AMUSE), evolve equal-mass Plummer models with $N=1000,2000,4000$ (more if you have a GPU). Track the Lagrangian radii and the core radius as functions of time in units of $t_{\rm rh}$. The curves for different $N$ should nearly coincide when time is expressed in $t_{\rm rh}$. Identify the core collapse time. Is it close to $15\,t_{\rm rh}$ for the single-mass case? What happens after core collapse (binary formation, re-expansion, gravothermal oscillations at large enough $N$)?

**4. [M] Energy conservation with close encounters.** Show the energy error in your direct code versus time and softening. Then add regularization or a smaller time-step parameter for binaries (or use `KS` regularization in an established code). How does the energy error in the collapsed phase depend on this?

**5. [M] Mass segregation.** Evolve a cluster with a mass spectrum (a Kroupa or Salpeter IMF, minimum to maximum mass ratio 20 to 50). Plot the mean stellar mass as a function of radius at several times and the time to segregate. Check the expectation that heavier stars segregate on a timescale of order $(\langle m\rangle/m)\,t_{\rm rh}$. Does your cluster approach energy equipartition? Report the velocity dispersion as a function of mass.

**6. [M] The Jacobi radius.** For a cluster of mass $2\times10^5\,M_\odot$ on a circular orbit at 10 kpc in a flat-rotation-curve galaxy with $v_c=220$ km/s, compute $r_J$ from both formulas. You should find a value close to 90 pc. Compare with the size of the real cluster: what is the ratio $r_h/r_J$? Which regime (tidally limited or isolated) are clusters in?

**7. [M] Evaporation in a tidal field.** Add an external tidal field (a point-mass or isothermal host in the circular-orbit tidal approximation, or the full galaxy potential from Module 02) to your cluster simulation. Count the stars with energy above the escape energy as a function of time, and measure the mass-loss rate. Check that the dissolution time scales roughly as $N^{3/4}$ at fixed other parameters (Baumgardt 2001; verify).

**8. [M] King fit to a real cluster.** For a well-observed nearby cluster, extract a radial number-density profile from Gaia catalogue star counts (with a magnitude cut and a field-star background), or use a published surface-brightness profile. Fit a King model (free $W_0$, $r_0$ and a constant background) with `emcee` and compare with the Harris catalogue values.

**9. [H] Tidal tails and the Galactic bar.** Generate a stream from a Palomar 5-like cluster with a particle-spray method (for example the Fardal et al. 2015 recipe in `gala`) or a direct N-body run in the MW potential from Module 04. Compare the streams in a purely axisymmetric potential and in the potential with the Module 02 bar at different pattern speeds. Do you see density gaps introduced by the bar (Pearson et al. 2017)? Quantify the gap contrast as a function of $\Omega_p$ and bar strength.

**10. [H] A Monte Carlo (Henon) code.** Implement Henon's Monte Carlo method for a single-mass cluster in a spherical potential: represent the cluster by shells with $(E,L)$ per star, order them by radius, and at each step pair neighbours and deflect their velocities according to the local relaxation rate with a time step proportional to the local relaxation time. Reproduce a core collapse time of the order of $15\,t_{\rm rh}$ and compare your run with the direct N-body run of problem 3. Discuss the strengths and the limits of the method (no dynamics of binaries without extra physics).

**11. [H] Dynamical friction on clusters.** Using the Chandrasekhar formula and your Module 09 tools, compute the infall time of massive clusters from several galactocentric radii in the Milky Way's bulge and inner halo. Which clusters could have sunk to the center within a Hubble time? What is the contribution to the nuclear star cluster? (Tremaine, Ostriker and Spitzer 1975.)

**12. [H] Clusters in the bar.** Using the orbit classification of Module 08, problem 10, select inner-Galaxy clusters on bar-supporting or chaotic orbits. For one of them, run a small N-body model (or a semi-analytic mass-loss model) on the actual orbit in the barred potential and compare its mass loss with the axisymmetric case. Discuss the effect of tidal shocks at pericenters through the bulge and the disk.

## Checks

- King models: $c\approx1.5$ for $W_0\approx7$ and monotonic increase with $W_0$ (within the tables).
- N-body: scaled evolution coincides across $N$ in units of $t_{\rm rh}$; core collapse of a single-mass cluster at about 15 $t_{\rm rh}$ (loose agreement: about 10 to 20).
- Jacobi radius about 90 pc for the example.
- Mass segregation timescale of order $t_{\rm rh}/(m/\langle m\rangle)$.

## Pitfalls

- Using $N$-body units and physical units interchangeably. Keep a conversion function in `units.py`.
- Softening in a cluster simulation: it removes the close encounters that drive the physics. Use no softening (or a very small one) with proper integrators.
- Estimating the core radius from a noisy density without the Casertano and Hut weighting.
- Taking the Chandrasekhar dynamical friction at face value for clusters orbiting in a cored region: it fails.

## Gate questions

1. Why do collisional systems have negative specific heat, and what stops the resulting collapse?
2. How does the mass spectrum change the core-collapse time?
3. Why do tidal tails form at the Lagrange points, and what imprints would a rotating bar leave on them?

## Deliverable

`clusters/` with the King solver, the Lagrangian radii and core-radius estimators, a direct-summation Hermite code with tests, the Monte Carlo code and notebooks `12_clusters.ipynb`, with the collapse, segregation and tidal tail experiments.
