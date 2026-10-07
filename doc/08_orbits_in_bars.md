# Module 08: Orbits in bars

**Difficulty:** Hard. **Time:** about 3 weeks.

## Goal

Understand the orbital skeleton of a rotating bar: the Jacobi integral, Lagrange points, the families of periodic orbits (x1, x2, x3, x4), their stability, chaos, and the 3D orbits that build boxy/peanut bulges. Write a periodic-orbit finder and make Poincare sections of a rotating bar.

## Prerequisites

Modules 03, 05, 07.

## Reading

- **B&T Ch. 3:** orbits in planar non-axisymmetric rotating potentials (the rotating frame, the Jacobi integral, Lagrange points, periodic orbit families, resonances). Read the section on orbits in rotating bars twice.
- **S&G topics:** orbits in bars; rings and resonances.
- **Papers:**
  - Contopoulos and Papayannopoulos (1980), *Orbits in weak and strong bars*.
  - Sanders and Huntley (1976) and Athanassoula et al. (1983) on gas flow in bars.
  - Pfenniger and Friedli (1991) and Combes et al. (1990) on 3D orbits and the peanut shape.
  - Dehnen (2000), the Hercules stream and the outer Lindblad resonance.
  - Contopoulos, *Order and Chaos in Dynamical Astronomy*, as a reference book.

## Key equations (derive)

In a frame rotating at $\Omega_p$, the Hamiltonian is the **Jacobi integral**, conserved for a time-independent rotating bar:

$$E_J = \tfrac12|\mathbf v|^2 + \Phi(\mathbf x) - \tfrac12\Omega_p^2(x^2+y^2) = E - \Omega_pL_z$$

Equations of motion in the rotating frame (the bar along the $x$-axis):

$$\ddot x = -\frac{\partial\Phi}{\partial x} + 2\Omega_p\dot y + \Omega_p^2x,\qquad \ddot y = -\frac{\partial\Phi}{\partial y} - 2\Omega_p\dot x + \Omega_p^2y$$

Effective potential $\Phi_{\rm eff}=\Phi-\tfrac12\Omega_p^2R^2$. Its stationary points are the Lagrange points: $L_1$ and $L_2$ on the bar's major axis near corotation (saddle points), $L_3$ at the center, and $L_4$, $L_5$ on the minor axis near corotation. The zero-velocity curve at fixed $E_J$ bounds the allowed region.

**Resonance condition** for a closed orbit in the epicycle approximation in the rotating frame, with $m=2$ for a bar:

$$m(\Omega-\Omega_p)=\pm l\,\kappa\quad\Rightarrow\quad \Omega-\Omega_p=\pm\frac{l}{m}\kappa$$

Important cases: corotation ($\Omega=\Omega_p$), the inner and outer Lindblad resonances ($\Omega\mp\kappa/2=\Omega_p$, from $m=2$, $l=1$) and the 4:1 ultra-harmonic resonance ($\Omega-\kappa/4=\Omega_p$, from the $m=4$ harmonic of the bar) near the end of the bar.

**Orbit families** (from Contopoulos and Papayannopoulos):

| Family | Shape | Sense | Where and stability |
| --- | --- | --- | --- |
| x1 | elongated along the bar | prograde | the backbone, stable over most of the bar |
| x2 | elongated perpendicular to the bar | prograde | inside the ILR, stable, appears only if an ILR exists |
| x3 | perpendicular, near the ILR | prograde | unstable |
| x4 | perpendicular | retrograde | stable |

**Periodic orbit finder by shooting.** Fix $E_J$. Start on the $x$-axis with $y=0$, $\dot x=0$ and a given $x_0$, so that $\dot y_0$ follows from $E_J$. Integrate until the next perpendicular crossing of the $x$-axis and require $\dot x=0$ there (a closed orbit crosses perpendicularly twice per period by symmetry). Solve for $x_0$ with Newton or Brent. Stability follows from the eigenvalues of the monodromy matrix, obtained by integrating the variational equations. A periodic orbit is linearly stable if the trace of the reduced $2\times2$ matrix has magnitude less than 2.

## A model to use throughout

Use the Dehnen bar from Module 02 on top of your Milky Way rotation curve, with $\Omega_p=40$ km/s/kpc, $R_b=3.5$ to 5 kpc, and the strength $\alpha=0.01,0.05,0.1$ as a weak, intermediate and strong bar. Also keep the logarithmic bar $\Phi_L$ with $q_y=0.8$ as a simple secondary model.

## Hands-on problems

**1. [E] Rotating-frame integration.** Integrate orbits in the rotating frame and, separately, in the inertial frame with a time-dependent bar potential. Show that they give the same orbit after transformation, and that $E_J$ is conserved to $10^{-9}$ relative with DOP853 and $E$ is not.

**2. [E] Lagrange points and zero-velocity curves.** Find $L_1$ to $L_5$ numerically with a root finder on $\nabla\Phi_{\rm eff}$. Contour $\Phi_{\rm eff}$ and plot the zero-velocity curves for a few values of $E_J$. At what $E_J$ does the curve open at $L_1$ and $L_2$, letting stars escape the bar region?

**3. [M] Periodic orbits and the characteristic diagram.** Implement the shooting method. For a range of $E_J$ find the x1 family and, if an ILR exists, x2 and x3. Plot the orbits, and plot the *characteristic diagram* (the intercept $x_0$ against $E_J$) which shows all families on one figure. Check the diagram's branching at the ILR.

**4. [M] Stability.** Add the monodromy matrix computation. Mark the stable and unstable segments of each family on the characteristic diagram. Verify that x3 is unstable and see where x1 loses stability (around the 4:1 resonance and near corotation).

**5. [M] Poincare sections.** For each bar strength and for $E_J$ spanning the range from inside the ILR to beyond corotation, construct the section $y=0$, $\dot y>0$ in $(x,\dot x)$. Identify the x1 island, resonant islands, regular tori and the chaotic sea. Where does chaos appear first? How does the stochastic region grow with $\alpha$? Overlay the stable periodic orbits from problem 4 at their $x_0$.

**6. [M] Epicycle prediction.** For a weak bar, compute the frequencies of near-circular orbits and verify the resonance locations from $\Omega\pm\kappa/2=\Omega_p$. Compare the predicted ILR and OLR radii with the points where the characteristic diagram changes character.

**7. [M] Orbits that support the bar.** Classify orbits in the bar region by how they are shaped relative to the bar axis: bar-supporting (x1 and its relatives), orbits perpendicular to it, and chaotic. Estimate what fraction of phase space at each $E_J$ supports the bar. Why can a strong bar not be self-consistent if this fraction is too small?

**8. [H] 3D orbits and the peanut.** Extend the bar to 3D with a vertically thin density and compute the vertical frequency $\nu$ along the x1 family. Find the radius where $\nu:(\Omega-\Omega_p)$ is $2:1$ (a vertical resonance). Integrate orbits near this resonance and look for the characteristic "banana" and "brezel" shapes in side projection that make an X-shaped bulge. Compare with the secular buckling story of Module 10.

**9. [H] The Hercules stream.** Following Dehnen (2000), integrate backward in time a grid of $(U,V)$ velocities at the solar position in your MW + bar model (with the bar grown adiabatically from zero to full strength over several rotation periods, as in the paper), weight each by an axisymmetric distribution function (a Schwarzschild or quasi-isothermal one) and compute the resulting local velocity distribution. Reproduce the bimodality of the distribution in $(U,V)$ for a bar with its OLR near the Sun. Then change $\Omega_p$ and the bar angle and see how the feature moves. Note the competing interpretations (OLR versus corotation versus spiral arms) in the recent literature.

**10. [H] Globular clusters in the bar.** Using the Gaia-based proper motions and distances catalogue of Milky Way globular clusters (Vasiliev and Baumgardt 2021; verify the data location), integrate the orbits of the inner-Galaxy clusters in your MW + bar model for a few Gyr. Classify each as bar-trapped, box-like, chaotic, or not affected by the bar, by looking at the frequency ratio and at the Lyapunov exponent estimator from Module 03. Which clusters' orbits change qualitatively between an axisymmetric and a barred potential?

## Checks

- Jacobi integral conserved to $10^{-9}$ relative; energy drifts.
- Lagrange point positions: $L_1$ and $L_2$ near corotation along the major axis, $L_4$ and $L_5$ near corotation along the minor axis.
- Closed orbits found by shooting have closure error below $10^{-10}$.
- x3 unstable and x1, x2, x4 stable over their main ranges in a weak bar.
- Hercules-like bimodality appears for a bar with OLR near the Sun.

## Pitfalls

- Wrong sign of the Coriolis term in the rotating frame. Check with a free particle.
- Forgetting that in the rotating frame the energy is not conserved, only $E_J$.
- Interpreting a single orbit's looks as evidence of the family. Use the monodromy or frequency analysis.
- Treating sticky chaotic orbits near islands as regular: they may look regular for hundreds of orbital periods.

## Gate questions

1. Why is the Jacobi integral conserved while the energy and angular momentum are not?
2. Why can stars not be trapped around $L_1$ and $L_2$ inside corotation indefinitely, and what do they do near these points?
3. What dynamical features of the x1 and x2 families explain the observed shapes of gas dust lanes and nuclear rings?

## Deliverable

`bars/periodic_orbits.py` (shooting, monodromy, characteristic diagram), `orbits/poincare_rotating.py`, `notebooks/08_orbits_in_bars.ipynb` with the characteristic diagram, the Poincare sections for three bar strengths, and the Hercules stream and globular-cluster experiments.
