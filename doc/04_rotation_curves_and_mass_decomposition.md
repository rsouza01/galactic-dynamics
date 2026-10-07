# Module 04: Rotation curves and mass decomposition

**Difficulty:** Medium. **Time:** about 2 weeks.

## Goal

Turn an observed rotation curve into a mass model, with honest uncertainties, and understand the degeneracies between the stellar disk, the bulge, the gas and the dark halo. Apply it to the Milky Way and to external spirals.

## Prerequisites

Modules 02 and 03. Basic Bayesian fitting (you will reuse the `emcee` habits from the moons study).

## Reading

- **B&T Ch. 1** (observed rotation curves) and **Ch. 2** (disk potentials, circular speed).
- **S&G topics:** rotation curves of spirals, dark matter evidence, the mass of the Milky Way, Tully-Fisher relation.
- **Papers:** Lelli, McGaugh and Schombert (2016) for the SPARC rotation-curve database; Navarro, Frenk and White (1996) for the halo profile; McGaugh, Lelli and Schombert (2016) on the radial acceleration relation. Eilers et al. (2019) for the Milky Way's outer rotation curve.

## Key equations

Circular speed from the potential, and the decomposition into components that add in quadrature:

$$v_c^2(R) = R\frac{\partial\Phi}{\partial R}\Big|_{z=0}, \qquad v_{\rm obs}^2 = v_{\rm gas}^2 + \Upsilon_d\, v_{\rm disk}^2 + \Upsilon_b\, v_{\rm bulge}^2 + v_{\rm halo}^2$$

with $\Upsilon$ the stellar mass-to-light ratios. Two halo models other than NFW:

- Pseudo-isothermal: $\rho = \rho_0/[1+(r/r_c)^2]$, with $v_c^2 = 4\pi G\rho_0 r_c^2\left[1 - \dfrac{r_c}{r}\arctan\dfrac{r}{r_c}\right]$
- Burkert: $\rho = \dfrac{\rho_0 r_0^3}{(r+r_0)(r^2+r_0^2)}$

Stars lag the circular speed (asymmetric drift), so when stellar kinematics are used you need $v_c$ and not the mean rotation. Gas is cold, and gas rotation is close to circular, except in a bar (Module 07).

Milky Way terminal-velocity method. For gas at galactic longitude $\ell$ in the first quadrant, the tangent point is at $R=R_0\sin\ell$ and the maximum line-of-sight velocity is

$$v_t(\ell) = v_c(R_0\sin\ell) - v_c(R_0)\sin\ell$$

## Hands-on problems

**1. [E] Halo mass profiles.** Compute $v_c(r)$ for NFW, pseudo-isothermal and Burkert halos with the same $V_{200}$. Find the radius where each peaks (NFW at about $2.16\,r_s$) and compare their central behaviour. Which one gives a "core", which a "cusp"?

**2. [E] A simple Milky Way fit.** Take a published Milky Way rotation curve (for example, a compilation of tangent-point and masers data from the literature, or the Eilers et al. points) and fit a three-component model (Miyamoto-Nagai disk, Hernquist bulge, NFW halo) by least squares. Report $v_c(R_0)$, the local dark matter density and the virial mass. Do the same with the mass of the disk fixed to two values, 4 and $6\times10^{10}M_\odot$, to see what it does to the halo.

**3. [M] Terminal-velocity check.** Use your Milky Way model to predict $v_t(\ell)$ for $\ell$ between 20 and 80 degrees and compare it with a published terminal-velocity curve. Where does the model deviate? (Hint: the inner Galaxy, where the bar breaks axisymmetry.)

**4. [M] SPARC galaxies.** Download the SPARC database (public tables of rotation curves with disk, bulge and gas contributions for about 175 galaxies; verify the URL and the file formats). For at least three galaxies with different morphology (a dwarf, an intermediate spiral and a massive spiral), fit stellar mass-to-light ratio, halo scale and halo normalization with `emcee`, with a Gaussian prior on the stellar mass-to-light ratio (center at 0.5 for 3.6 micron data, width about 0.1 dex; check the SPARC papers). Show corner plots.

**5. [M] Maximum disk versus submaximal.** For the same galaxies, compute the best fit with the stellar mass-to-light ratio at its maximum allowed value ("maximum disk") and at your prior center. Quantify the change in halo mass. This is the central degeneracy of the field.

**6. [M] The baryonic Tully-Fisher relation.** For the SPARC sample, take the flat rotation speed $V_f$ and the baryonic mass (stellar plus 1.33 times the HI mass), fit $\log M_b = a\log V_f + b$ and report the slope. Check against the literature (close to 4, verify) and plot the scatter.

**7. [M] Radial acceleration relation.** For all points, compute $g_{\rm obs}=v^2/R$ and $g_{\rm bar}$ from the baryonic components alone. Plot $g_{\rm obs}$ against $g_{\rm bar}$ and describe what you see. This is an observational constraint that any dark matter model needs to explain. You do not need to take a side in the debates about its interpretation, only to understand the data and its uncertainties.

**8. [H] Realistic uncertainties.** Add systematic errors due to inclination uncertainty (say 3 degrees), distance (10 percent), and the stellar mass-to-light prior. Propagate them through the fit with `emcee` by treating inclination and distance as nuisance parameters. Show how much the halo parameter posteriors broaden.

**9. [H] Non-circular motions.** In a barred galaxy the gas orbits are not circular and the "rotation curve" derived from Doppler shifts is biased. Using your orbit code from Module 03 and the Dehnen bar potential from Module 02, set up gas test particles on closed orbits (x1 family, previewing Module 08) and estimate the error in the inferred circular speed in the bar region, as a function of bar strength.

## Checks

- The NFW peak position at $2.16\,r_s$ and the Freeman exponential-disk peak at about $2.15\,R_d$ from Module 02 are reproduced from the fit code too.
- Milky Way: $v_c(R_0)$ within the range 220 to 240 km/s and a virial mass of order $10^{12}M_\odot$ (broad range, depending on the data used).
- Baryonic Tully-Fisher slope near 4 for SPARC, within the scatter.

## Pitfalls

- Fitting with the wrong units for surface brightness and masses. Create a data validation step in your code.
- Over-interpreting a single best-fit curve. Always show the posterior.
- Treating the halo model as truth: a good fit does not tell you which of NFW, Burkert or pseudo-isothermal is right.

## Gate questions

1. Why does a "maximum disk" fit give a lower dark matter mass in the inner galaxy?
2. Why is the rotation curve of a barred galaxy harder to interpret in the bar region?
3. What does a declining outer Milky Way rotation curve imply for the total mass, and what are its most important systematic errors?

## Deliverable

`notebooks/04_rotation_curves.ipynb` with the Milky Way model, three SPARC fits with corner plots, the baryonic Tully-Fisher relation, and the radial acceleration relation. `data/` with the downloaded tables and a `SOURCES.md` listing where each came from.
