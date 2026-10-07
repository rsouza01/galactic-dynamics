# Module 10: Secular evolution

**Difficulty:** Hard. **Time:** about 3 weeks.

## Goal

Understand how a bar changes its host galaxy over many rotation periods: angular-momentum exchange with the halo, bar growth and slowdown, buckling and the boxy/peanut bulge, radial migration of stars, gas inflow and pseudobulge formation, and the question of bar longevity. Measure each effect in your own simulations.

## Prerequisites

Modules 06, 07, 08, 09.

## Reading

- **B&T:** the sections on bar-halo interaction and dynamical friction, and Ch. 5 on spiral and bar dynamics. Look in the chapters on stability and galaxy interactions in your edition.
- **S&G topics:** secular evolution of disk galaxies, bulges, galaxy interactions.
- **Papers and reviews:**
  - Kormendy and Kennicutt (2004), *Secular evolution and the formation of pseudobulges in disk galaxies* (Annual Review of Astronomy and Astrophysics).
  - Sellwood (2014), *Secular evolution in disk galaxies* (Reviews of Modern Physics).
  - Lynden-Bell and Kalnajs (1972); Tremaine and Weinberg (1984); Weinberg (1985).
  - Debattista and Sellwood (2000); Athanassoula (2002, 2003) on bar slowdown and the role of halos.
  - Combes and Sanders (1981); Raha et al. (1991) on buckling.
  - Sellwood and Binney (2002) on radial mixing at corotation ("churning").
  - Shen and Sellwood (2004) on bar destruction by central mass concentrations.

## Concepts

1. **Angular-momentum exchange.** A bar emits angular momentum at its resonances, mostly to the halo and the outer disk. By Lynden-Bell and Kalnajs the bar's angular momentum, which is *negative* in the sense of its wave energy, drops, so the bar grows stronger and slows down. A live, dense, dynamically *responsive* halo with many resonant particles slows the bar the most. A rigid halo cannot absorb angular momentum at all.
2. **Bar slowdown and the fast-bar problem.** Observed bars appear to be fast ($\mathcal R\lesssim1.4$), while simulations with live halos often produce slow bars. This tension is a central question: halos with dynamical friction should slow bars, so how do bars stay fast? Candidate answers include gas, low halo densities in the bar region, and bar-halo resonant physics beyond the simplest models.
3. **Buckling and the peanut.** A strong bar can undergo a vertical (buckling) instability, producing a boxy/peanut-shaped (X-shaped) bulge viewed edge-on. A second, smoother route is by trapping into vertical resonances (Module 08).
4. **Pseudobulges and gas flows.** Gas loses angular momentum to the bar's torques and flows inward, building a central concentration and nuclear rings, which can feed star formation and, by increasing the central mass, weaken or destroy the bar (though N-body work suggests bars are fairly robust).
5. **Radial migration.** At corotation, a transient spiral or bar can change a star's angular momentum **without heating it** (churning), moving it across the disk with little change in its eccentricity. Heating *without* migration is called blurring. Migration flattens metallicity gradients and affects the thick disk.

## Key relations

For perturbations rotating at $\Omega_p$ the exchange of energy and angular momentum with a star obeys

$$\Delta E=\Omega_p\,\Delta L_z$$

so at corotation a star can change its $L_z$ with no change in $E-\Omega_pL_z$, which is the mechanism behind churning. Combine $\Delta E=\Omega_R\Delta J_R+\Omega_\varphi\Delta L_z$ with $\Delta E=\Omega_p\Delta L_z$ and the resonance condition $m(\Omega_\varphi-\Omega_p)=-l\,\Omega_R$ to find (derive it, and check the sign convention against B&T)

$$\Delta J_R=\frac{l}{m}\,\Delta L_z$$

So at corotation ($l=0$) the radial action does not change (migration without heating), while at the Lindblad resonances ($l=\pm1$, $m=2$) every unit of angular momentum exchanged comes with half a unit of radial action, which heats or cools the stars.

Angular momentum bookkeeping for a closed system:

$$L_{\rm tot}=L_{\rm disk}+L_{\rm halo}+L_{\rm gas}=\text{const},\qquad \frac{dL_{\rm bar}}{dt}=-\tau_{\rm halo}-\tau_{\rm outer\ disk}$$

Bar strength and slowdown are traced by $A_2(t)$ and $\Omega_p(t)$. Buckling is traced by the vertical asymmetry of the bar, for example the mean $z$ of bar particles weighted by $x$, or the $m=2$ Fourier coefficient of the vertical position.

## Hands-on problems

**1. [E] Angular momentum bookkeeping.** In one of your Module 07 bar-forming simulations compute $L_z(t)$ separately for the disk (inside $R_d\times$ some radius), the outer disk and the halo. Plot the relative changes. Check the total is conserved to the precision of your integrator and identify which components lose and which gain.

**2. [E] Rigid versus live halo.** Run the same disk with (a) a rigid analytic halo and (b) a live halo. Compare the evolution of $\Omega_p(t)$ and $A_2(t)$. Quantify how much more the live halo slows the bar. Explain.

**3. [M] Bar slowdown versus halo properties.** Run a small suite varying the halo central density (through concentration or mass) and the halo's velocity dispersion (or spin). Measure $\Omega_p(t)$, $A_2(t)$ and $\mathcal R(t)$. Which parameters lead to the strongest slowdown? Compare with Athanassoula (2003) qualitatively.

**4. [M] Where the angular momentum goes.** For the live-halo run, find the halo particles with the largest $\Delta L_z$ and compute their actions and frequencies (from `AGAMA`, or by frequency analysis). Plot $\Delta L_z$ against the ratio $\Omega_\varphi/\Omega_p$ and mark the resonances. This reproduces the resonance structure predicted by Tremaine and Weinberg.

**5. [M] Buckling.** In a suitable run (a thin, strong bar), measure the vertical structure of the bar versus time: the vertical asymmetry coefficient, the vertical dispersion and the thickness of the bar relative to the disk. Identify the buckling epoch, the drop in $A_2$ at that time, and the boxy/peanut shape in an edge-on projection at the end. Compare the strength of the final peanut for two different disk vertical thicknesses.

**6. [M] Edge-on peanut diagnostics.** Rotate the final snapshot to edge-on with the bar at 45 degrees to the line of sight and at 90 degrees (side-on). Compute the vertical density contours and the $B/P$ strength (for example, the Fourier amplitude of the surface density in $z$-height as a function of $x$). Find the radius where the X-shape extends and relate it to the vertical resonance radius from Module 08.

**7. [M] Radial migration.** Select the disk star particles of a simulation with a recurring transient spiral or a bar. For each particle, compute the change in angular momentum $\Delta L_z$ and the change in the radial action $\Delta J_R$ (or the epicycle amplitude) between two snapshots a few rotation periods apart. Separate the churning contribution (large $\Delta L_z$, small $\Delta J_R$) from blurring (increase in $\Delta J_R$). Plot the final radius against the initial radius and find the fraction of stars that moved by more than $R_d$.

**8. [M] Metallicity gradients.** Assign to each star an initial metallicity from a linear radial gradient (for example $-0.07$ dex/kpc, check the observed value). After migration, recompute the gradient at the final radii. How much is it flattened, and how does the scatter at a given radius grow?

**9. [H] Gas and pseudobulge.** Add a simple gas component to your simulation, either with an N-body code that has hydrodynamics or by an approximate sticky-particle scheme (an isothermal gas with a prescribed cooling and no star formation). Track the central mass versus time as the gas flows in. Does the bar weaken? Compare the central stellar and gas mass profiles before and after. Measure the ratio of the pseudobulge to the total mass and compare with literature estimates (Kormendy and Kennicutt 2004).

**10. [H] Bar robustness.** Following Shen and Sellwood (2004), insert a central mass concentration into a bar's disk (for example grow a central Plummer point mass to 1 to 5 percent of the disk mass) and measure what happens to the bar strength and pattern speed. What central mass is needed to destroy a strong bar, if any?

**11. [H] Fast-bar problem.** Try to find a simulation setup (halo density, gas fraction, bar strength) that yields a bar that stays fast ($\mathcal R<1.4$) for 5 Gyr or more. Report the outcome and a clear, honest statement of what is and is not achieved. This is an open research question; a negative result is a result.

## Checks

- Total angular momentum conserved to $10^{-3}$ relative; the disk bar region loses and the halo and outer disk gain.
- The live halo slows the bar more than the rigid halo does.
- Buckling visible as a dip in $A_2$ and a peanut in the final edge-on image in the thin-disk run.
- Churning and blurring decomposed for at least one run, with the fraction of strongly migrating stars reported.
- $\Delta E=\Omega_p\Delta L_z$ for resonant particles confirmed.

## Pitfalls

- Numerical heating from too few halo particles, which spuriously modifies the slowdown. Always run a convergence test in $N$ (Module 06).
- Time-averaging $\Omega_p$ over too short a window. A bar's pattern speed measured from its phase is noisy and requires smoothing.
- Interpreting the unstable evolution of a non-equilibrium initial condition as secular evolution.

## Gate questions

1. Why does a bar's angular momentum decrease as its amplitude grows? (Think of negative-energy waves.)
2. What is the difference between churning and blurring in terms of actions?
3. Why does the answer to "do bars slow down in real galaxies?" depend on the central density of the dark halo?

## Deliverable

`secular/` (angular-momentum bookkeeping, migration decomposition, buckling diagnostics), a suite of simulations with HDF5 snapshots and configuration YAMLs under `runs/`, and `notebooks/10_secular.ipynb` with the plots above.
