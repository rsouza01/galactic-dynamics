# Module 11: Collisionless equilibria and elliptical galaxies

**Difficulty:** Hard. **Time:** about 3 weeks.

## Goal

Build equilibrium models of spheroidal systems from distribution functions, use Jeans equations to interpret kinematics, understand why ellipticals have the shapes and profiles they do (violent relaxation, mergers, radial-orbit instability, black-hole scouring), and implement Schwarzschild's orbit-superposition method.

## Prerequisites

Modules 02, 03, 06.

## Reading

- **B&T Ch. 4:** the collisionless Boltzmann equation, Jeans theorems, Jeans equations, distribution functions for spherical systems (Eddington inversion, anisotropic models, Osipkov-Merritt), the virial theorem, tensor virial theorem. Also the chapters on stability and galaxy formation and interactions in your edition (violent relaxation, radial-orbit instability, mergers).
- **S&G topics:** elliptical galaxies (photometry, kinematics, shapes, the fundamental plane, stellar populations), galaxy mergers.
- **Papers and reviews:**
  - Schwarzschild (1979) and later triaxial extensions (Schwarzschild 1993).
  - Hernquist (1990) for the analytic isotropic model, and Dehnen (1993) and Tremaine et al. (1994) for the $\gamma$-family.
  - Lynden-Bell (1967), violent relaxation; van Albada (1982), cold collapse.
  - Merritt and Aguilar (1985), the radial-orbit instability.
  - Toomre and Toomre (1972) and Barnes (1992), mergers.
  - Cappellari (2016), *Structure and kinematics of early-type galaxies from integral-field spectroscopy* (Annual Review of Astronomy and Astrophysics); Emsellem et al. (2007, 2011) for fast and slow rotators.
  - Milosavljevic and Merritt (2001) on binary black holes and core formation.

## Key equations (derive)

**Sersic profile**, with $b_n$ chosen so that $R_e$ encloses half the light:

$$I(R)=I_e\exp\left\{-b_n\left[\left(\frac{R}{R_e}\right)^{1/n}-1\right]\right\},\qquad b_n\approx2n-\tfrac13+\frac{4}{405n}$$

$n=4$ is the de Vaucouleurs profile ($b_4\approx7.67$), $n=1$ the exponential.

**Eddington inversion** for an isotropic spherical system, in terms of the relative potential $\Psi=-\Phi$ and relative energy $\mathcal E=-E$:

$$f(\mathcal E)=\frac{1}{\sqrt8\,\pi^2}\,\frac{d}{d\mathcal E}\int_0^{\mathcal E}\frac{d\rho}{d\Psi}\frac{d\Psi}{\sqrt{\mathcal E-\Psi}}$$

**Isotropic Hernquist model** (Hernquist 1990), with $q=\sqrt{a\mathcal E/GM}$:

$$f(\mathcal E)=\frac{M}{4\pi^3(2GMa)^{3/2}}\,\frac{3\sin^{-1}q+q\sqrt{1-q^2}\,(1-2q^2)(8q^4-8q^2-3)}{(1-q^2)^{5/2}}$$

I quote this from memory. **Verify the normalization numerically** (problem 2) before using it.

**Spherical Jeans equation** with anisotropy $\beta=1-(\sigma_\theta^2+\sigma_\varphi^2)/2\sigma_r^2$:

$$\frac{d(\nu\sigma_r^2)}{dr}+\frac{2\beta}{r}\nu\sigma_r^2=-\nu\frac{d\Phi}{dr}\quad\Rightarrow\quad M(<r)=-\frac{\sigma_r^2r}{G}\left[\frac{d\ln\nu}{d\ln r}+\frac{d\ln\sigma_r^2}{d\ln r}+2\beta\right]$$

**Osipkov-Merritt models** have $f=f(Q)$ with $Q=E-L^2/(2r_a^2)$ and anisotropy $\beta(r)=r^2/(r^2+r_a^2)$: isotropic in the center, radial in the outskirts.

**Line-of-sight dispersion** from the Jeans solution, with surface brightness $I(R)$:

$$I(R)\,\sigma_{\rm los}^2(R)=2\int_R^\infty\left(1-\beta\frac{R^2}{r^2}\right)\frac{\nu\,\sigma_r^2\,r\,dr}{\sqrt{r^2-R^2}}$$

**Tensor virial theorem.** $2K_{ij}+W_{ij}=0$ relates the shape of a system to its rotation and anisotropy (Binney 1978). A flattened elliptical can be flattened by rotation or by anisotropic velocity dispersion.

**Rotation parameter** (Emsellem et al. 2007), a luminosity-weighted measure of rotational support within $R_e$:

$$\lambda_R=\frac{\sum_iF_iR_i|V_i|}{\sum_iF_iR_i\sqrt{V_i^2+\sigma_i^2}}$$

**Wolf et al. (2010) mass estimator** for dispersion-supported systems: the mass within the 3D half-light radius is $M_{1/2}\approx3\,\sigma_{\rm los}^2\,r_{1/2}/G$, where $r_{1/2}\approx\tfrac43R_e$. Check the numerical factor against the paper.

**Schwarzschild's method.** In a given potential, integrate a large library of orbits, record for each the time it spends in each spatial and kinematic cell, then find non-negative orbit weights $w_k$ such that $\sum_kw_kc_{k,j}$ reproduces the observed density and kinematic moments in each cell $j$, solved with non-negative least squares (`scipy.optimize.nnls`) with regularization.

## Hands-on problems

**1. [E] Sersic profiles.** Implement $I(R)$, solve for $b_n$ by root finding the condition $\Gamma(2n)=2\gamma(2n,b_n)$ and compare with the asymptotic formula for $n=0.5$ to $10$. Compute the total luminosity and the fraction inside $R_e$. Plot the profiles for $n=1,2,4,8$ on a $R^{1/4}$ and on a log-log scale.

**2. [E] DF normalization.** Check that the Hernquist $f(\mathcal E)$ reproduces the density: compute $\rho(r)=4\pi\int_0^{\sqrt{2\Psi(r)}}f\!\left(\Psi(r)-\tfrac12v^2\right)v^2\,dv$ numerically and compare with $\rho_H(r)$ to $10^{-6}$. Then implement the general Eddington inversion numerically and verify it for the Hernquist and for a Dehnen model with $\gamma=0.5$ and $1.5$.

**3. [M] Jeans versus sampling.** Sample $10^6$ particles from the Hernquist DF (rejection sampling in $(r,v)$ using the Eddington $f$). Measure $\sigma_r(r)$ and $\sigma_{\rm los}(R)$ from the sample, and compare with the Jeans solution for $\beta=0$. Repeat with a constant-$\beta$ model and with an Osipkov-Merritt model ($r_a=a$), computing the Jeans solution and the sampled data. Check at 1 percent.

**4. [M] Mass estimators and anisotropy.** From a mock sample of 500 stars from an anisotropic model, estimate the mass with the Wolf et al. formula and with a Jeans fit. How large is the error when the model is radially or tangentially anisotropic ($\beta=\pm0.5$)? This is the mass-anisotropy degeneracy.

**5. [M] N-body equilibrium and the radial-orbit instability.** Sample an isotropic Hernquist sphere with $N=2\times10^5$ and evolve it with your Module 06 tree code for 20 dynamical times. Check the density profile is stable and the axis ratios (from the inertia tensor in shells) stay near 1. Then sample Osipkov-Merritt models with decreasing $r_a$ and show that very radial models are unstable (the radial-orbit instability) and evolve into triaxial or bar-like systems (Merritt and Aguilar 1985). Find the approximate critical $r_a/a$ and compare with the common criterion $2K_r/K_t\gtrsim1.7$ (verify).

**6. [M] Cold collapse and violent relaxation.** Start a homogeneous sphere with zero initial velocity. Evolve it until it virializes. Measure the final density profile (close to $r^{-4}$ in the outskirts, with a steep center), the fraction of mass ejected, the final velocity anisotropy profile $\beta(r)$ (radial outside), the axis ratios (cold collapses are often prolate or triaxial because of radial-orbit instability), and the Sersic index of the projected profile. Check the sensitivity to $N$ and to softening.

**7. [M] Mergers and cores.** Merge two identical $\gamma=1.5$ Dehnen spheres on a parabolic orbit. Measure the remnant's shape, $\beta(r)$ and projected profile. Repeat with a supermassive black hole particle (0.5 percent of the galaxy mass) at the center of each galaxy: they form a binary and eject stars, scouring a core (Milosavljevic and Merritt 2001). Measure the mass deficit and compare with the black hole mass. Use small softening and be careful about numerical effects.

**8. [H] Schwarzschild's method.** Write a Schwarzschild solver for a spherical system first.
   - Compute an orbit library in the Hernquist potential on a grid of $(E,L)$, with the time-averaged contribution of each orbit to the radial density and to the line-of-sight velocity moments.
   - Generate mock kinematic data with a known $\beta(r)$ from your Problem 3 sample.
   - Fit with `nnls` plus regularization. Recover $\beta(r)$ and the enclosed mass, with an estimate of the uncertainty by repeating with different noise realizations and different potential normalizations.
   *Check:* for the isotropic mock you should recover $\beta\approx0$ and the mass within a few percent; examine what goes wrong with too few orbits or with the wrong potential.

**9. [H] Triaxial orbit families.** In a triaxial logarithmic potential (axis ratios $q_y=0.9$, $q_z=0.7$, small core) classify a large library of orbits into box, short-axis tube, long-axis tube and chaotic orbits (using $L$ component sign changes and frequency analysis from Module 09). Plot the fractions against energy. Show that a strong central cusp or a central mass makes chaos dominant and destroys the triaxiality of the self-consistent solution (Merritt and Fridman 1996).

**10. [H] Fast versus slow rotators.** Take the remnants of your simulated mergers (or, if you have the compute, mergers of disk galaxies with a live halo), project them along random lines of sight, bin into Voronoi cells, and compute $\lambda_R(R_e)$ and the ellipticity $\epsilon$. Plot them in the $\lambda_R$ versus $\epsilon$ diagram and compare with the observed ATLAS3D distribution (Cappellari 2016 for the empirical boundary between fast and slow rotators; verify). Which merger configurations produce fast rotators?

## Checks

- Sersic $b_4=7.67$, with the asymptotic formula close for large $n$.
- Hernquist DF reproduces $\rho$ to $10^{-6}$ (so the normalization quoted above is right or you have fixed it).
- Jeans and sampled $\sigma_{\rm los}$ agree to 1 to 2 percent for the three anisotropy cases.
- Isotropic Hernquist stable for 20 $t_{\rm dyn}$; a strongly radial model shows triaxial growth.
- Schwarzschild recovers the enclosed mass of the isotropic mock to a few percent.

## Pitfalls

- Mass-anisotropy degeneracy: wrong anisotropy produces wrong mass from line-of-sight dispersions alone.
- Sampling an isotropic DF with the wrong normalization yields the right shape but the wrong total mass.
- Treating a non-equilibrium remnant as a relaxed galaxy: check virial ratio and time-dependence.
- A Schwarzschild library that is too sparse produces spurious "preference" for particular orbits.

## Gate questions

1. State Jeans' theorem and explain why it lets you build $f$ from integrals of motion.
2. What is violent relaxation and why can't it be described by a standard (two-body) relaxation time?
3. Why do cuspy centers and massive black holes tend to make triaxial galaxies rounder?

## Deliverable

`spheroids/` with Sersic, DF inversion, Jeans solvers, sampling and Schwarzschild tools, and `notebooks/11_ellipticals.ipynb` with the tests above.
