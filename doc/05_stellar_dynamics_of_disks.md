# Module 05: Stellar dynamics of disks

**Difficulty:** Medium. **Time:** about 3 weeks.

## Goal

Understand the kinematics and stability of a stellar disk: the velocity ellipsoid, asymmetric drift, vertical structure, Toomre's stability criterion, density waves and swing amplification. This is the physics from which bars (Module 07) and spiral arms emerge.

## Prerequisites

Modules 03 and 04. The collisionless Boltzmann equation (skim B&T Ch. 4 first).

## Reading

- **B&T Ch. 4:** the collisionless Boltzmann equation, Jeans equations (especially their application to disks and the asymmetric drift).
- **B&T Ch. 5:** local stability of stellar disks (Toomre's $Q$), the WKB density-wave theory of spiral structure, swing amplification.
- **S&G topics:** spiral structure, disk heating, stability, dark halos and disk stability.
- **Papers:** Toomre (1964) on gravitational stability; Julian and Toomre (1966); Toomre (1981) on swing amplification; Lin and Shu (1964).

## Key equations (derive)

**Velocity ellipsoid in the epicycle approximation.** For a nearly circular stellar disk the azimuthal and radial dispersions are tied:

$$\frac{\sigma_\varphi^2}{\sigma_R^2} = \frac{\kappa^2}{4\Omega^2}$$

which gives $1/2$ for a flat rotation curve.

**Asymmetric drift.** From the radial Jeans equation of an axisymmetric disk, with $\nu$ the stellar number density and $v_a\equiv v_c-\bar v_\varphi$,

$$v_a = \frac{\sigma_R^2}{2v_c}\left[\frac{\sigma_\varphi^2}{\sigma_R^2} - 1 - \frac{\partial\ln(\nu\sigma_R^2)}{\partial\ln R}\right]$$

I quote this from memory of B&T's derivation. Derive it yourself and check the sign and form against the book.

**Vertical structure.** For an isothermal self-gravitating sheet:

$$\rho(z) = \rho_0\,\mathrm{sech}^2\!\left(\frac{z}{2z_0}\right), \qquad z_0 = \frac{\sigma_z}{\sqrt{8\pi G\rho_0}}, \qquad \Sigma = 4\rho_0 z_0$$

**Toomre's local stability.** A thin stellar disk is stable to axisymmetric ripples if

$$Q_s = \frac{\sigma_R\,\kappa}{3.36\,G\Sigma} > 1, \qquad Q_g = \frac{c_s\,\kappa}{\pi G\Sigma}\ \text{(gas)}$$

**Density waves (fluid dispersion relation).** For a tightly wound wave of azimuthal number $m$, radial wavenumber $k$, pattern speed $\Omega_p$ and frequency $\omega=m\Omega_p$:

$$(\omega - m\Omega)^2 = \kappa^2 - 2\pi G\Sigma|k| + k^2c_s^2$$

(replace $c_s$ and the reduction factor by the stellar version for stars; see B&T). Lindblad resonances occur where $\Omega\pm\kappa/m=\Omega_p$, and corotation where $\Omega=\Omega_p$.

**Swing amplification** (Toomre 1981): a leading wave in a shearing disk unwinds, and over a limited time it is amplified by a large factor. The relevant dimensionless parameter is

$$X = \frac{k_{\rm crit}\,R}{m}, \qquad k_{\rm crit} = \frac{\kappa^2}{2\pi G\Sigma}$$

with the largest amplification for $X$ of order 1 to 3 and $Q$ not too large, and for a flat rotation curve.

## Hands-on problems

**1. [E] Velocity ellipsoid.** Using a flat rotation curve ($v_0=220$ km/s), show numerically that $\sigma_\varphi^2/\sigma_R^2=1/2$. Then use solar-neighbourhood Hipparcos- or Gaia-type values quoted in the literature ($\sigma_R$ of order 35 to 40 km/s for old stars) to compute the expected $\sigma_\varphi$ and compare with observed values (verify).

**2. [E] Asymmetric drift.** Derive the asymmetric drift formula, then evaluate it for an exponential disk with $\sigma_R^2\propto e^{-R/R_d}$. In this case the bracket simplifies to $-\tfrac12+2R/R_d$ for a flat curve (verify). Plot $v_a$ against $\sigma_R$ and compare with the observed linear relation between $v_a$ and $\sigma^2$ of solar-neighbourhood stars.

**3. [E] Toomre Q for the Milky Way.** For your Module 04 Milky Way model, estimate $\Sigma(R)$, $\kappa(R)$ and $\sigma_R(R)$ and compute $Q(R)$ between 3 and 15 kpc. Where is it smallest? Compare the result with the common remark that the Milky Way's disk is marginally stable ($Q\approx1.5$ to 2).

**4. [M] Vertical equilibrium.** Integrate the Poisson-Jeans system $d^2\Phi/dz^2=4\pi G\rho$ and $\rho=\rho_0\exp(-\Phi/\sigma_z^2)$ numerically, and compare with the sech$^2$ solution. Then add a second, hotter component (a thick disk) and a fixed dark matter contribution, and see how the vertical scale heights change.

**5. [M] Test-particle heating.** Using your Module 03 orbit integrator, evolve 5000 stars on near-circular orbits in a logarithmic potential and perturb them with a rotating $m=2$ spiral potential of the form $\Phi_s=A(R)\cos[2(\varphi-\Omega_pt)-f(R)]$ (a logarithmic spiral). Measure the evolution of $\sigma_R$ and the angular-momentum changes. Locate the Lindblad and corotation radii and show where the heating and the angular-momentum changes concentrate. You are seeing the resonant physics that Module 09 formalizes.

**6. [M] Shearing sheet.** Implement the 2D shearing sheet (local approximation of a differentially rotating disk) with $N=10^4$ to $10^5$ particles using periodic shearing boundary conditions and a particle-mesh or tree force solver (preview of Module 06). Start with $Q=1.3$ to 1.5 and watch transient, trailing, swing-amplified wakes recur. Measure the amplitude of the dominant mode against time. Compare with Julian and Toomre (1966) expectations (qualitatively).

**7. [H] Swing amplification in a linear calculation.** Write the linearized equations for a leading wave in a shearing sheet in the fluid approximation (B&T gives a form you can integrate with a standard ODE solver). Compute the amplification factor as a function of $X$ and $Q$ and reproduce the qualitative figure of Toomre (1981): amplification peaks at moderate $X$ and decreases rapidly with $Q$.

**8. [H] Spiral arms as transient features.** In a global N-body disk (use the code of Module 06 when you have it, or return to this problem later), measure the $m=2$ to 4 amplitude of the disk as a function of radius and time and decide whether the spirals are long-lived waves or recurrent transients. Plot the pattern speed (phase drift) as a function of radius. If it follows $\Omega(R)$ rather than being rigid, the arms are corotating with local material.

## Checks

- $\sigma_\varphi^2/\sigma_R^2=\kappa^2/4\Omega^2$ verified numerically on a simulated near-circular ensemble to better than 5 percent.
- Toomre $Q$ for the Milky Way model in the range 1 to 3 over 3 to 15 kpc, with a plausible minimum.
- The vertical isothermal solution matches sech$^2$ to $10^{-3}$ before you add components.
- Shearing sheet shows transient wakes and Q-dependent amplitude.

## Pitfalls

- Mixing the stellar ($3.36$) and gaseous ($\pi$) forms of $Q$.
- Forgetting that the epicycle approximation assumes small radial excursions.
- Interpreting a single snapshot of a spiral as evidence for a long-lived wave.

## Gate questions

1. What does $Q<1$ mean physically, and what stabilizes a disk at small scales and at large scales?
2. Explain swing amplification as a three-step process: leading wave, shearing, trailing wave.
3. Why is a cold, massive, disk-dominated galaxy prone to forming a bar, and what does a massive halo change?

## Deliverable

`disks/` with the epicycle tools, the Toomre-$Q$ calculator, the shearing-sheet code and tests, and `notebooks/05_disk_dynamics.ipynb`.
