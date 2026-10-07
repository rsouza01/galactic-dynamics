# Module 01: Foundations, scales and the Python toolkit

**Difficulty:** Easy. **Time:** about 1 week.

## Goal

Know the zoo of objects you will study, the numbers that characterize them, why some are "collisionless" and others "collisional", and have a working environment with a units module you will trust for the rest of the program.

## Prerequisites

Graduate-level classical mechanics and basic astronomy. Python.

## Reading

- **B&T Ch. 1**, all of it. Pay attention to the observational overview of galaxy types and the discussion of timescales.
- **S&G topics:** the introductory chapter, the chapter on the Milky Way (stellar populations, disk, bulge, halo, rotation, Oort constants), and the chapter(s) on galaxy morphology: spirals, bars, S0s, ellipticals.
- **Review:** Bland-Hawthorn and Gerhard (2016), *The Galaxy in context* (Annual Review of Astronomy and Astrophysics).

### Task 0: build your reading map

Open the tables of contents of your copies of B&T and S&G. In `notes/reading_map.md`, fill a table with columns *Module, B&T chapters/sections, S&G chapters/sections*, using the overview as a first guess. Update it as you go. This one hour of work is worth more than any list I could give you.

## Concepts

1. **The objects.** Disk galaxies (spirals, with or without a bar), S0s, ellipticals (E0 to E7, boxy or discy), globular clusters (GCs), the Milky Way as a barred spiral.
2. **Components.** Thin and thick disk, bar, bulge (classical versus pseudobulge), stellar halo, dark halo.
3. **Collisionless versus collisional.** In a galaxy the stars feel the smooth mean field of all the others, and individual encounters are negligible over a Hubble time. In a globular cluster, encounters change energies over a fraction of the age, so you need relaxation theory.
4. **Timescales.** Dynamical time, crossing time and relaxation time. Compare them with the age of the Universe to decide which physics matters.

## Key equations

Dynamical time of a system of mass $M$ and radius $r$, crossing time with velocity dispersion $\sigma$, and a crude relaxation time for $N$ equal-mass stars:

$$t_{\rm dyn} = \sqrt{\frac{r^3}{GM}}, \qquad t_{\rm cross} = \frac{r}{\sigma}, \qquad t_{\rm relax} \approx \frac{N}{8\ln N}\, t_{\rm cross}$$

The more careful half-mass relaxation time (Spitzer) for equal masses $m$, half-mass radius $r_h$ and Coulomb logarithm $\ln\Lambda$:

$$t_{\rm rh} = 0.138\,\frac{N^{1/2}\, r_h^{3/2}}{m^{1/2} G^{1/2}\ln\Lambda}, \qquad \ln\Lambda \approx \ln(0.11\,N)$$

Useful constants:

- $G = 4.30091\times10^{-6}\ \mathrm{kpc\,(km/s)^2\,M_\odot^{-1}}$ (equivalently $4.30091\times10^{-3}$ in pc units)
- $1\ \mathrm{kpc/(km/s)} \approx 977.8$ Myr, and $1\ \mathrm{pc/(km/s)} \approx 0.978$ Myr

## Fiducial systems (approximate, verify)

| System | Mass scale | Size scale | Velocity scale | Notes |
| --- | --- | --- | --- | --- |
| Milky Way disk | stellar mass about 5e10 Msun | Sun at about 8.2 kpc, scale length about 2.6 kpc | circular speed about 230 km/s | bar half-length about 5 kpc, pattern speed about 40 km/s/kpc |
| Typical globular cluster | about 2e5 Msun, N about 4e5 stars | half-mass radius about 3 pc | dispersion about 10 km/s | known MW GCs number about 150 |
| Giant elliptical | about 1e11 Msun | effective radius about 3 to 10 kpc | dispersion about 200 to 300 km/s | N about 1e11 stars |

## Hands-on problems

**1. [E] Environment.** Create the environment, install the packages from the overview, and run a test that imports every one of them. Commit it as `tests/test_env.py`.

**2. [E] Units module.** Write `units.py` with `G`, `kpc_per_kms_to_Myr`, helpers to convert km/s to kpc/Myr, and Msun to kg. Write unit tests for the two conversion factors above.

**3. [E] Timescale calculator.** Implement $t_{\rm dyn}$, $t_{\rm cross}$, $t_{\rm relax}$ and $t_{\rm rh}$ for the three fiducial systems and print them together with the ratio to 13.8 Gyr. Expected: the GC has $t_{\rm dyn}$ of order 0.2 Myr and $t_{\rm rh}$ of order 1 Gyr (for $N = 4\times10^5$, $m = 0.5\,M_\odot$, $r_h = 3$ pc); the Milky Way disk has $t_{\rm relax}$ about three to four orders of magnitude above the age of the Universe by this crude estimate.

**4. [M] A Plummer virial mass (derive).** For a Plummer sphere the central line-of-sight dispersion is $\sigma_0^2 = GM/(6b)$ and the 3D half-mass radius is about $1.305\,b$. Show that $M \approx 4.6\, r_h \sigma_0^2/G$. Then plug in typical GC numbers and check you recover about $10^5$ to $10^6\,M_\odot$ for $\sigma_0$ of order 5 to 15 km/s and $r_h$ of a few pc.

**5. [M] GC catalogue survey.** Download the Harris catalogue of Milky Way globular clusters (a public McMaster compilation of positions, distances, concentrations and structural radii). Compute an approximate $t_{\rm rh}$ for each cluster from its luminosity and half-light radius, histogram it, and mark which clusters are older than their relaxation time. Which ones should be "dynamically old"? Compare with the concentration parameter column.

**6. [M] Galaxy-zoo cheat sheet.** In `notes/zoo.md` write one paragraph each for: bar, boxy/peanut bulge, classical bulge, pseudobulge, nuclear ring, outer ring, fast and slow rotator, core and cusp elliptical. You will refine it as the modules go on.

**7. [H] When does "collisionless" fail?** Take a spherical stellar system with $N$ stars and find the $N$ for which $t_{\rm relax}$ equals the Hubble time, as a function of its crossing time. Plot the boundary in the plane of ($N$, $r_h$) and put the three fiducial systems on it. This is the quantitative reason the program has separate tracks for galaxies and clusters.

## Checks

- Unit tests for the conversion factors pass.
- GC fiducial: $t_{\rm dyn} \approx 0.2$ Myr and $t_{\rm rh} \approx 0.9$ Gyr (within about 20 percent).
- Problem 4 reproduces the Plummer factor 4.6 to two digits.

## Pitfalls

- Mixing pc and kpc versions of $G$. Use a single module.
- Using $N$ of stars in a galaxy with the equal-mass formula and trusting the result to better than an order of magnitude. It is an estimate.
- Confusing half-light (projected) and half-mass (3D) radii. The conversion factor is about 1.3 for a Plummer profile, and it matters.

## Gate questions

1. Why are encounters between stars irrelevant in a galaxy but dominant in the core of a globular cluster?
2. What property of the Milky Way disk makes a bar plausible dynamically, and what does it change about the way you model its mass distribution?
3. Name three observations that separate a classical bulge from a pseudobulge.

## Deliverable

`units.py`, `tests/test_units.py`, `notebooks/01_timescales.ipynb`, `notes/reading_map.md`, `notes/zoo.md`.
