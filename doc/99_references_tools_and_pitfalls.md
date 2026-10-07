# Appendix: references, tools, pitfalls and shortcuts

> All references below are from my memory of the literature, not freshly opened sources. Look each one up before relying on it, and prefer the primary paper when a number matters.

## 1. Your topic list mapped to modules

| Your topic | Where it is covered |
| --- | --- |
| Barred spiral galaxies | 07 (observations and formation), 10 (secular evolution), 13 |
| Orbital structure in bars | 03 (orbit basics), 08 (orbits in bars) |
| Resonances | 08, 09 |
| Secular evolution | 10 |
| Rotation curves | 04 |
| Stellar dynamics in disks | 05 |
| N-body simulations | 06, and used in 07, 10, 11, 12 |
| Numerical modelling in Python | 01 (toolkit), 06 (performance and N-body), throughout |
| Globular clusters | 12 |
| Elliptical galaxies | 11 |

## 2. Books

| Book | Use |
| --- | --- |
| Binney and Tremaine, *Galactic Dynamics* (2nd ed., 2008) | The theory backbone for all modules |
| Sparke and Gallagher, *Galaxies in the Universe: An Introduction* | Observational and conceptual context, physical pictures |
| Binney and Merrifield, *Galactic Astronomy* | Observational background |
| Spitzer, *Dynamical Evolution of Globular Clusters* | Module 12 |
| Heggie and Hut, *The Gravitational Million-Body Problem* | Module 12 and N-body methods |
| Aarseth, *Gravitational N-Body Simulations* | Module 06 and 12 |
| Contopoulos, *Order and Chaos in Dynamical Astronomy* | Modules 08 and 09 |
| Lichtenberg and Lieberman, *Regular and Chaotic Dynamics* | Module 09 |
| Merritt, *Dynamics and Evolution of Galactic Nuclei* | Module 11 and capstone E |
| Goldstein, Poole and Safko, *Classical Mechanics* | Hamiltonian background for Module 09 |

## 3. Papers and reviews by module

**01, 04 (Milky Way and rotation curves).** Bland-Hawthorn and Gerhard (2016); Eilers et al. (2019); Lelli, McGaugh and Schombert (2016); McGaugh, Lelli and Schombert (2016); Navarro, Frenk and White (1996).

**02, 03 (potentials, orbits).** Dehnen (1993); Hernquist (1990); Henon and Heiles (1964); Miyamoto and Nagai (1975); Freeman (1970).

**05 (disks).** Toomre (1964, 1981); Julian and Toomre (1966); Lin and Shu (1964); Goldreich and Lynden-Bell (1965).

**06 (N-body).** Barnes and Hut (1986); Makino and Aarseth (1992); Hernquist (1993); Athanassoula et al. (2000); Dehnen (2001); Dehnen and Read (2011); Springel's code papers for tree-PM methods.

**07 (bars).** Ostriker and Peebles (1973); Efstathiou, Lake and Negroponte (1982); Combes and Sanders (1981); Tremaine and Weinberg (1984); Sellwood and Wilkinson (1993); Athanassoula (1992); Debattista and Sellwood (2000); Gerhard (2011); Portail et al. (2017).

**08 (orbits in bars).** Contopoulos and Papayannopoulos (1980); Sanders and Huntley (1976); Athanassoula et al. (1983); Pfenniger and Friedli (1991); Combes et al. (1990); Dehnen (2000); Pearson, Price-Whelan and Johnston (2017).

**09 (resonances).** Lynden-Bell and Kalnajs (1972); Tremaine and Weinberg (1984); Weinberg (1985); Chirikov (1979); Laskar (1990, 1993); Papaphilippou and Laskar (1996).

**10 (secular evolution).** Kormendy and Kennicutt (2004); Sellwood (2014); Sellwood and Binney (2002); Athanassoula (2002, 2003); Raha et al. (1991); Shen and Sellwood (2004).

**11 (ellipticals).** Schwarzschild (1979, 1993); Lynden-Bell (1967); van Albada (1982); Merritt and Aguilar (1985); Toomre and Toomre (1972); Barnes (1992); Binney (1978); Emsellem et al. (2007, 2011); Cappellari (2016); Milosavljevic and Merritt (2001); Merritt and Fridman (1996); Wolf et al. (2010).

**12 (globular clusters).** King (1966); Henon (1961, 1971); Lynden-Bell and Wood (1968); Casertano and Hut (1985); Meylan and Heggie (1997); Baumgardt and Hilker (2018); Vasiliev and Baumgardt (2021); Tremaine, Ostriker and Spitzer (1975); Fardal et al. (2015).

## 4. Software

| Package | Purpose | Notes |
| --- | --- | --- |
| `numpy`, `scipy`, `matplotlib` | core numerics and plots | |
| `numba` | JIT compilation for loops | easiest speed-up in Python |
| `jax` | GPU and autodiff | optional |
| `h5py` | snapshot storage | store units and git hash in the header |
| `emcee`, `corner` | MCMC and posterior plots | Modules 04, 11, 12 |
| `galpy` | orbits, potentials, actions | great cross-check, mind its natural units |
| `gala` | orbits, potentials, streams | has a mock-stream generator |
| `AGAMA` | potentials, actions, distribution functions, initial conditions, Schwarzschild modelling | needs compilation; powerful |
| `pynbody` | snapshot analysis | |
| `pytreegrav` or other tree packages | force calculation | check maintenance status |
| NEMO (`gyrfalcON`), GADGET-type codes | fast N-body for large $N$ | external codes |
| NBODY6-family, PeTar, AMUSE | direct N-body for clusters | external codes |
| `pytest` | tests | one test per module |

Verify each package's installation instructions and maintenance status before you rely on it.

## 5. Data sources

- Rotation curves: the SPARC database (Lelli et al.).
- Milky Way globular clusters: the Harris catalogue; Baumgardt and Hilker (2018) masses; Vasiliev and Baumgardt (2021) Gaia-based kinematics.
- Stellar kinematics and the Milky Way bar: Gaia releases, plus published tables from the bar papers listed above.
- Early-type galaxy kinematics: the ATLAS3D and related integral-field survey papers.

## 6. Pitfalls that recur across modules

1. **Units.** One `units.py`. Never convert twice.
2. **Frame confusion.** Inertial versus rotating frames in the bar modules: energy versus Jacobi integral; sign of the Coriolis term.
3. **Non-equilibrium initial conditions.** Always evolve in isolation for a few dynamical times first.
4. **Particle noise.** Convergence tests in $N$ are mandatory.
5. **Softening.** Large for collisionless galaxy models, essentially zero (with regularization) for clusters.
6. **One snapshot as evidence.** Many features (spirals, bars, streams) are transient; use time series.
7. **Believing a posterior shaped by the prior.** Always test prior sensitivity.
8. **Mixing sign conventions** (complex time dependence, Love numbers, resonance integers $l$). Fix one in `notes/`.
9. **Trusting remembered numbers.** Validate against the primary source.

## 7. Minimal paths

If you have less time than the full program:

- **Bars only:** 01, 02, 03, 05, 06, 07, 08, 10, then capstone B or A. About 6 months.
- **Globular clusters only:** 01, 02, 03, 06, 12, then capstone C. About 4 months.
- **Ellipticals only:** 01, 02, 03, 06, 11, then capstone D or E. About 4 months.
- **Theory first, simulations later:** 01, 02, 03, 05, 09, 11, 12 reading and analytic problems only; then come back to 06 and the code.

## 8. Glossary

- **ILR, CR, OLR:** inner Lindblad, corotation and outer Lindblad resonances. $\Omega-\kappa/2=\Omega_p$, $\Omega=\Omega_p$, $\Omega+\kappa/2=\Omega_p$ for $m=2$.
- **x1, x2, x3, x4:** families of periodic orbits in a bar (Module 08).
- **$E_J$:** Jacobi integral $E-\Omega_pL_z$.
- **$Q$:** Toomre's stability parameter.
- **$\mathcal R$:** $R_{\rm CR}/R_{\rm bar}$, the bar's fast/slow ratio.
- **Churning, blurring:** radial migration with and without heating (Module 10).
- **Violent relaxation:** the rapid relaxation of a collisionless system to a quasi-equilibrium by time-varying fields (Module 11).
- **$t_{\rm rh}$:** half-mass relaxation time.
- **ROI:** radial-orbit instability.
