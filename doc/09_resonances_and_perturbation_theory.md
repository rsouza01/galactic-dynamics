# Module 09: Resonances and perturbation theory

**Difficulty:** Hard. **Time:** about 3 weeks.

## Goal

Treat the dynamics of bars, spirals and dynamical friction as **resonant** phenomena. Learn angle-action variables, the pendulum model of a resonance, the overlap criterion for chaos, Lynden-Bell and Kalnajs's result that angular momentum is exchanged only at resonances, and Chandrasekhar's dynamical friction. Build frequency-analysis tools.

## Prerequisites

Modules 03 and 08. Goldstein's chapters on Hamilton-Jacobi theory, action-angle variables and canonical perturbation theory. If those are not behind you yet, do them first.

## Reading

- **B&T Ch. 3:** angle-action variables, slowly varying potentials and adiabatic invariants, perturbation theory and resonances.
- **B&T Ch. 5:** Lindblad resonances in disks.
- **B&T kinetic-theory chapter:** dynamical friction and the Chandrasekhar formula (I recall it as Sec. 8.1 in the 2nd edition; check your table of contents).
- **S&G topics:** resonances in galaxies, dynamical friction, galaxy interactions.
- **Papers:**
  - Lynden-Bell and Kalnajs (1972), *On the generating mechanism of spiral structure*.
  - Tremaine and Weinberg (1984), *Dynamical friction in spherical systems*; Weinberg (1985).
  - Chirikov (1979), *A universal instability of many-dimensional oscillator systems*.
  - Laskar (1990, 1993) and Papaphilippou and Laskar (1996) for frequency analysis.
  - Lichtenberg and Lieberman, *Regular and Chaotic Dynamics*, as a reference.

## Key equations (derive each)

**Angle-action variables.** For an integrable $H_0(\mathbf J)$, orbits are $\boldsymbol\theta=\boldsymbol\Omega t+\boldsymbol\theta_0$ with frequencies $\boldsymbol\Omega=\partial H_0/\partial\mathbf J$. A rotating perturbation of azimuthal number $m$ and pattern speed $\Omega_p$ is expanded as

$$H_1=\sum_{\mathbf l}H_{\mathbf l}(\mathbf J)\cos\!\left(\mathbf l\cdot\boldsymbol\theta-m\Omega_pt\right)$$

**Resonance condition:**

$$\mathbf l\cdot\boldsymbol\Omega(\mathbf J)=m\Omega_p$$

In the planar case ($\mathbf l=(l,m)$) this includes corotation ($l=0$), the Lindblad resonances ($l=\pm1$ with $m=2$) and the 4:1 ultra-harmonic resonance, which belongs to the $m=4$ harmonic of the bar ($l=\pm1$ with $m=4$). Sign conventions for $l$ vary between texts, so fix one.

**Pendulum model.** Near a resonance, define the slow angle $\psi=\mathbf l\cdot\boldsymbol\theta-m\Omega_pt$ and expand about the resonant action:

$$H_{\rm res}=\tfrac12G\,(\Delta J)^2+V\cos\psi,\qquad \Delta J_{\max}=2\sqrt{|V/G|}$$

where $G=\sum_{ij}l_il_j\,\partial^2H_0/\partial J_i\partial J_j$ is the effective inverse mass. $\Delta J_{\max}$ is the half-width of the libration region (the separatrix).

**Chirikov overlap criterion.** Large-scale chaos appears when the resonance widths of neighbouring resonances overlap: the separation of the resonances in action space is smaller than the sum of their half-widths.

**Standard map**, a model of resonance overlap, with kick strength $K$:

$$p_{n+1}=p_n+K\sin\theta_n,\qquad\theta_{n+1}=\theta_n+p_{n+1}\pmod{2\pi}$$

Global chaos sets in near $K_c\approx0.97$.

**Lynden-Bell and Kalnajs.** A perturbation rotating at $\Omega_p$ with azimuthal number $m$ exchanges energy and angular momentum with stars in the ratio set by the Jacobi integral, $\Delta E=\Omega_p\Delta L_z$, and, for a steady perturbation, exchange occurs **only at resonances**.

**Chandrasekhar dynamical friction.** A body of mass $M$ moving at speed $v$ through a Maxwellian background of density $\rho$ and one-dimensional dispersion $\sigma$ feels

$$\frac{d\mathbf v}{dt}=-\frac{4\pi G^2M\rho\ln\Lambda}{v^2}\left[\mathrm{erf}(X)-\frac{2X}{\sqrt\pi}e^{-X^2}\right]\frac{\mathbf v}{v},\qquad X=\frac{v}{\sqrt2\,\sigma}$$

For a satellite on a circular orbit in a singular isothermal sphere ($X=1$ at all radii), the infall time from radius $r_i$ is

$$t_{\rm fric}=\frac{1.17}{\ln\Lambda}\frac{r_i^2v_c}{GM}$$

**Frequency analysis.** Take a complex time series $z(t)=x+ip_x$ for an orbit over a total time $T$, multiply by a Hanning window, and locate the peak of the Fourier transform. Refine its position by iterating a maximization of the windowed transform (Laskar's NAFF). The frequency error scales like $T^{-4}$ with the Hanning window. Compare the frequencies from two halves of the integration. Their difference measures chaotic diffusion.

## Hands-on problems

**1. [E] The pendulum.** Plot the phase portrait of $H=\tfrac12G\,\Delta J^2+V\cos\psi$ with separatrix. Check numerically that the libration region has half-width $2\sqrt{|V/G|}$ in action. Compute the small-oscillation frequency $\sqrt{|GV|}$ and compare it with a numerical period.

**2. [E] The standard map.** Plot the phase space for $K=0.5,0.97,1.5,3$. Estimate the largest Lyapunov exponent as a function of $K$ and locate the transition to global chaos. Identify the last invariant curve (the golden-ratio torus) as it breaks near $K_c$.

**3. [M] Resonance lines in action space.** For a flat-rotation-curve axisymmetric potential, use `galpy`'s Staeckel approximation (or `AGAMA`) to compute $\Omega_R(J_R,L_z)$ and $\Omega_\varphi(J_R,L_z)$ on a grid. Plot the curves $\Omega_\varphi-\Omega_R/2=\Omega_p$ (ILR), $\Omega_\varphi=\Omega_p$ (CR) and $\Omega_\varphi+\Omega_R/2=\Omega_p$ (OLR) in the $(L_z,J_R)$ plane for $\Omega_p=40$ km/s/kpc. Check that at $J_R\to0$ they reproduce the radii from Module 07.

**4. [M] Forced epicycle oscillator.** Derive the linear response of a radial epicycle $\ddot x+\kappa^2x=F\cos[m(\Omega-\Omega_p)t]$. Show the amplitude diverges at the Lindblad resonance condition. Then make the forcing amplitude grow slowly with time and show the response stays finite, with angular momentum change $\Delta L\propto F^2$ for resonant particles.

**5. [M] Frequency maps.** Implement NAFF (or use `scipy.signal` plus refinement) and compute $\Omega_R$ and $\Omega_\varphi$ for a grid of initial conditions on a line of fixed $E_J$ in your Module 08 bar. Plot the frequency ratio against initial $x_0$. Flat plateaus mark resonant islands, noisy regions mark chaos. Compute the diffusion index $|\Omega^{(1)}-\Omega^{(2)}|/\Omega$ from two halves of the integration and map it. Compare with the Poincare section.

**6. [M] Resonant capture by a growing bar.** Start $10^4$ test particles on circular orbits in the Milky Way potential. Grow the Dehnen bar slowly over 2 Gyr. Plot $\Delta L_z$ against initial $L_z$. You should see structure concentrated near corotation and the Lindblad resonances. Verify $\Delta E=\Omega_p\Delta L_z$ for the resonant particles to a few $10^{-3}$. Where do the stars gain and lose angular momentum, and what does it do to the bar's own angular momentum? (This is the essence of Module 10.)

**7. [M] Dynamical friction coefficient.** Show with the Chandrasekhar formula that $\mathrm{erf}(1)-2e^{-1}/\sqrt\pi\approx0.428$ and use it to derive the coefficient 1.17 in the infall time above. Then integrate the equation of motion of a satellite numerically in an isothermal halo and recover 1.17 to a few percent.

**8. [H] Satellite in a live halo.** Using your Module 06 code, put a point-mass or Plummer satellite (mass ratio 0.01 to 0.1) on a circular orbit in a live Hernquist or NFW halo ($N\ge5\times10^5$). Compare the measured orbital decay with Chandrasekhar's formula with a fitted Coulomb logarithm. Explore: (a) how $\ln\Lambda$ must be set, (b) what happens at low satellite mass (numerical noise), (c) what happens in a cored halo (the satellite stalls).

**9. [H] Resonant structure of the torque.** Create a test-particle spherical halo with an isotropic distribution function (for example a Hernquist halo) in a rotating bar potential of fixed $\Omega_p$ and amplitude. Measure each particle's final $\Delta L_z$ after a few Gyr and, using the frequencies from problem 5 or actions from `AGAMA`, identify the resonance $(l_1,l_2,l_3)$ nearest to each particle. Plot which resonances carry the torque. This is the analog of Tremaine and Weinberg's calculation, done numerically.

## Checks

- Pendulum half-width $2\sqrt{|V/G|}$ to 1 percent.
- Standard map $K_c\approx0.97$.
- Frequency analysis recovers the known epicycle frequencies of near-circular orbits to better than $10^{-6}$.
- $\Delta E=\Omega_p\Delta L_z$ for resonant test particles to about $10^{-3}$.
- Dynamical friction coefficient 1.17.

## Pitfalls

- Frequency analysis on short time series, or without a window: the precision degrades.
- Treating chaotic orbits as having well-defined frequencies.
- Using Chandrasekhar's formula with a constant $\ln\Lambda$ without checking the regime. It is an approximation to a global, resonant process.
- Confusing the pattern speed $\Omega_p$ with the orbital frequency of a star in the *inertial* frame.

## Gate questions

1. Why does a *steady* perturbation exchange angular momentum with stars only at resonances?
2. In what sense is dynamical friction a resonant process, and why does a cored halo fail to produce it for a satellite near the core?
3. Explain the Chirikov overlap criterion and how it predicts where chaos appears in your bar's Poincare sections.

## Deliverable

`orbits/frequency_analysis.py`, `orbits/standard_map.py`, `orbits/dynamical_friction.py`, and `notebooks/09_resonances.ipynb` with the frequency maps, the capture experiment and the dynamical friction test.
