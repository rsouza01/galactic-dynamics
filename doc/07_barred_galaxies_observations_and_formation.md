# Module 07: Barred galaxies, observations and formation

**Difficulty:** Medium. **Time:** about 2 weeks.

## Goal

Know what a bar is observationally, how to measure its length, strength and pattern speed, and why disks form bars. You will measure all of these on your own N-body models, including the Tremaine-Weinberg method on mock data.

## Prerequisites

Modules 05 and 06 (you need an N-body disk plus analysis pipeline).

## Reading

- **B&T Ch. 5:** global instabilities of stellar disks, the bar instability; and Ch. 3, the section on orbits in planar non-axisymmetric potentials (read ahead for Module 08).
- **S&G topics:** bars, rings and spirals in disk galaxies, the Milky Way bar and bulge.
- **Papers:**
  - Ostriker and Peebles (1973), the halo stabilization argument.
  - Efstathiou, Lake and Negroponte (1982), the empirical stability criterion.
  - Toomre (1981), swing amplification and the bar mode as a feedback loop.
  - Sellwood and Wilkinson (1993), *Dynamics of barred galaxies* (a review).
  - Sellwood (2014), *Secular evolution in disk galaxies* (Reviews of Modern Physics).
  - Tremaine and Weinberg (1984), the pattern-speed method.
  - Debattista and Sellwood (2000), on fast and slow bars.
  - Gerhard (2011), pattern speeds in the Milky Way; Portail et al. (2017) and Bland-Hawthorn and Gerhard (2016), on the Galactic bar's properties.

## Concepts

1. **Observed facts (approximate, verify).** A large fraction of disk galaxies host bars: roughly 30 percent in the optical and 60 to 70 percent in the near-infrared at low redshift, with a lower fraction at high redshift. Bars have nearly flat surface brightness profiles along their major axis and sharp ends. The Milky Way bar has a half-length of about 5 kpc, an angle of order 25 to 30 degrees to the Sun-center line, and a pattern speed of order 35 to 45 km/s/kpc. It sits inside a boxy or peanut-shaped bulge.
2. **Sub-structures.** Dust lanes on the leading edge of the bar, nuclear rings, inner and outer rings, ansae, and boxy/peanut bulges seen edge-on.
3. **Measured quantities.** Bar length $R_{\rm bar}$; strength (ellipticity, the $m=2$ Fourier amplitude $A_2/A_0$, or the torque parameter $Q_b$); pattern speed $\Omega_p$ and the dimensionless ratio $\mathcal R=R_{\rm CR}/R_{\rm bar}$. Bars with $1.0\lesssim\mathcal R\lesssim1.4$ are called *fast* and bars with $\mathcal R\gtrsim1.4$ *slow*. Bars cannot extend beyond corotation.
4. **Formation.** Cold, massive, disk-dominated systems are unstable to a global $m=2$ mode. Mechanism (Toomre 1981): a feedback loop in which waves swing-amplify, travel inward, reflect at the center (or at an ILR) and re-emerge. A massive, concentrated halo, a hot disk or a central mass concentration suppress or delay it. Bars can also be triggered by tidal interactions.

## Key equations

Fourier amplitudes of the surface density in annuli (you coded this in Module 06):

$$A_m(R)=\frac{\left|\sum_j m_j e^{im\varphi_j}\right|}{\sum_j m_j}$$

Torque-based bar strength (Combes and Sanders 1981): with tangential force $F_T$ and mean radial force $\langle F_R\rangle$ at radius $R$,

$$Q_T(R)=\frac{\left|F_T\right|_{\max}(R)}{\langle F_R\rangle(R)},\qquad Q_b=\max_R Q_T(R)$$

Stability criteria (quoted from the literature, **check them**):

- Ostriker and Peebles: a disk with $t=T_{\rm rot}/|W|\gtrsim0.14$ tends to be bar-unstable, where $T_{\rm rot}$ is the rotational kinetic energy and $W$ the potential energy.
- Efstathiou, Lake and Negroponte: bar-unstable for $\epsilon_m\equiv v_{\max}/\sqrt{GM_d/R_d}\lesssim1.1$, where $M_d$ is the disk mass, $R_d$ its scale length, and $v_{\max}$ the peak circular speed of the whole model.

Tremaine-Weinberg: for a pattern rotating rigidly at $\Omega_p$ with a tracer obeying the continuity equation, along slits parallel to the line of nodes

$$\Omega_p\sin i=\frac{\int V_{\rm los}\,\Sigma\,dx}{\int x\,\Sigma\,dx}$$

where $x$ is the sky coordinate along the slit and $i$ the inclination. **Derive** it from the continuity equation, noting the assumptions: a well-defined single pattern speed, a tracer that obeys the continuity equation (which gas does not always do, because of star formation and chemistry), and a precise knowledge of the position angle of the line of nodes and the center.

## Hands-on problems

**1. [E] Analytic bar diagnostics.** Using a projected ellipsoidal density with isophote ellipticity increasing outward (or a Ferrers bar from Module 02), compute $A_2(R)$, its phase, and the isophote ellipticity. The bar angle (phase) should be constant along the bar and $A_2$ should peak near its end.

**2. [E] Bar length definitions.** Implement three estimates: (a) the radius of maximum $A_2$, (b) the radius where the phase deviates by 5 to 10 degrees from its mean value in the bar, (c) the radius of maximum ellipticity. Apply them to your analytic bar and later to simulation snapshots. Compare the three: which is systematically larger or smaller?

**3. [M] Torque strength.** Compute $Q_T(R)$ and $Q_b$ from the Dehnen bar of Module 02 on top of your Module 04 Milky Way model, as a function of the dimensionless strength $\alpha$. Find the relation between $Q_b$ and $\alpha$.

**4. [M] Bar formation experiments.** Using your Module 06 disk and halo models, run a suite varying the halo-to-disk mass ratio and the disk's Toomre $Q$ (for example $Q=1.2,1.5,2,3$). For each model record when (if at all) $A_2$ exceeds, say, 0.2 and the bar's final strength. Plot the outcome in the plane ($\epsilon_m$, $Q$). Compare with the Efstathiou criterion.

**5. [M] Bar growth rate.** For the bar-forming runs, plot $\ln A_2(R_{\rm peak})$ against time. Identify the linear growth phase, measure its e-folding time, and find the saturation and any later dip (buckling, Module 10).

**6. [M] Tremaine-Weinberg on mock data.** From a simulation snapshot with a known pattern speed, project it at inclination 30, 45 and 60 degrees, with the bar at 20, 45 and 70 degrees to the line of nodes. Bin the surface density and the density-weighted velocity into slit pixels, apply the formula, and compare with the true pattern speed. Then add (i) noise, (ii) an error of 1, 3 and 5 degrees in the position angle of the line of nodes, (iii) an offset in the center. *Expected:* the method is extremely sensitive to the position angle error (a small error produces a large spurious contribution because the $\int V\Sigma$ and $\int x\Sigma$ integrals are both small).

**7. [H] Pattern speed from the phase.** Measure $\Omega_p(t)=d\varphi_{\rm bar}/dt$ in your simulation from the phase of the $m=2$ Fourier component, smoothed in time and radius. Compare it with the TW measurement above. Compute the dimensionless ratio $\mathcal R=R_{\rm CR}/R_{\rm bar}$ with $R_{\rm CR}$ from $\Omega(R_{\rm CR})=\Omega_p$ and classify the bar as fast or slow.

**8. [H] The Milky Way bar's resonances.** Using your Milky Way model, a pattern speed in the range 35 to 45 km/s/kpc, and a flat rotation curve, compute the corotation radius and the inner and outer Lindblad resonance radii (solve $\Omega-\kappa/2=\Omega_p$ and $\Omega+\kappa/2=\Omega_p$). A useful analytic limit: for a flat rotation curve with $v_0=230$ km/s and $\Omega_p=40$ km/s/kpc, $R_{\rm CR}=v_0/\Omega_p\approx5.75$ kpc and $R_{\rm OLR}=(1+1/\sqrt2)R_{\rm CR}\approx9.8$ kpc. Where is the Sun relative to these? (This sets up the Hercules stream problem of Modules 08 and 09.)

## Checks

- Analytic bar: constant phase along the bar, $A_2$ maximum near its end.
- Bar formation matches the Efstathiou criterion roughly (some scatter is expected).
- TW recovers the true pattern speed to better than 10 percent with perfect inputs, and degrades with a small position-angle error.
- Flat-curve resonance radii as above.

## Pitfalls

- Defining the bar length by different criteria in different places. Always report which you used.
- Measuring the pattern speed from a noisy phase without smoothing.
- Reading the bar's growth in an N-body run as universal: it depends on the softening, particle number and the stability of your initial conditions (Module 06).

## Gate questions

1. Why can a bar not extend past corotation?
2. How does a massive, centrally concentrated halo change the bar instability, and what does Ostriker and Peebles' argument fail to capture?
3. Why does the Tremaine-Weinberg method give wrong answers for a gas tracer in the presence of star formation?

## Deliverable

`bars/` with Fourier analysis, bar length and strength estimators, a TW implementation and a periodic-pattern-speed estimator; `notebooks/07_bars.ipynb` with the formation suite, the TW test and the resonance calculation.
