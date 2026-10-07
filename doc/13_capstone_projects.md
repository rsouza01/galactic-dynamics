# Module 13: Capstone project

**Difficulty:** Hard. **Time:** 8 to 10 weeks.

## Goal

Complete one research-style project from question to written note, using the tools from the earlier modules. The point is not novelty but a defensible, reproducible result with honest uncertainties. Choose one of the options below, or propose your own, by the end of Module 10.

## How to choose

| Option | Main subjects | Compute | Modules used |
| --- | --- | --- | --- |
| A. Bar formation and slowdown in a live-halo galaxy | barred spirals, secular evolution | high (N-body) | 05, 06, 07, 09, 10 |
| B. Orbit structure of the Milky Way bar, the Hercules stream and stream gaps | orbits in bars, resonances | low (test particles) | 03, 08, 09 |
| C. Globular clusters in a barred galaxy | clusters, bars, resonances | medium | 06, 08, 09, 12 |
| D. Schwarzschild modelling of an elliptical galaxy | ellipticals | medium | 03, 11 |
| E. Core formation by black-hole binaries in mergers | ellipticals, N-body | high | 06, 11 |
| F. Integrated: *How does a bar reshape a globular cluster system?* | bars and clusters | medium to high | 06, 08, 09, 10, 12 |

If compute is a constraint, choose B or D, which are both rich in physics with modest requirements. Option F is the one that best matches your interest in barred galaxies and globular clusters at once.

## Common structure for every option

**Phase 1 (weeks 1 to 2): Question and plan.** Write a half-page statement of the question, the hypotheses, the model, the quantities you will measure, and what result would convince you. List the tests that will validate each component.

**Phase 2 (weeks 3 to 5): Build and validate.** Build the pipeline and run all the unit tests and the small-scale checks from the earlier modules. Convergence tests (particle number, time step, softening, library size) are not optional.

**Phase 3 (weeks 6 to 8): Production runs and analysis.** Run the production suite with all configuration files and seeds recorded. Produce the figures. Estimate uncertainties, for example by bootstrap or by repeating with different seeds.

**Phase 4 (weeks 9 to 10): Write-up.** A note of about 10 to 15 pages: question, model, methods, tests, results, discussion, limitations, reproduction instructions. Include a README such that `make all` rebuilds everything from the configs.

## Option A: Bar formation and slowdown in a live-halo galaxy

**Question.** How do the halo's central density and spin change the pattern speed evolution and the ratio $\mathcal R=R_{\rm CR}/R_{\rm bar}$ of a bar in an isolated Milky Way-like galaxy?

**Plan.**
1. Generate a family of disk plus live-halo models with an equilibrium generator (`AGAMA`, `GalIC` or your own), varying the halo concentration and spin, at $N\ge5\times10^5$.
2. Run each for at least 5 Gyr with a tree code.
3. Measure $A_2(t)$, bar length, $\Omega_p(t)$, $\mathcal R(t)$, buckling epoch and the angular momentum transferred to the halo (Module 10).
4. Use the resonance analysis of Module 09 to show that the transferred angular momentum is deposited at specific resonances in the halo.
5. Compare with the bar properties in the literature.

**Validation.** Total angular momentum conserved; an $N$-convergence test; a control run with a rigid halo.

**Pitfalls.** Spurious bar formation from non-equilibrium initial conditions; two-body heating at low halo $N$.

## Option B: Orbit structure of the Milky Way bar, the Hercules stream and stream gaps

**Question.** What range of bar pattern speed and angle is consistent with the Hercules stream in the solar neighbourhood *and* with the gap structure in a thin stream such as Palomar 5?

**Plan.**
1. Build the Milky Way plus Dehnen bar model (Module 02) with adjustable $\Omega_p$, strength and angle.
2. Compute the periodic orbit families and Poincare sections (Module 08) for the adopted parameters. Identify the resonance radii.
3. Reproduce the Hercules structure in the local $(U,V)$ distribution with the backward-integration method (Dehnen 2000) for a grid of $\Omega_p$ values and compare with the Gaia velocity distribution (a published local sample, from Gaia DR3 or earlier data).
4. Generate a Palomar 5-like stream with a particle-spray model and measure the bar's imprint in the stream (Pearson et al. 2017), as a function of $\Omega_p$.
5. Combine the two constraints and map the allowed region of parameter space.

**Validation.** Jacobi conservation; Hercules recovered in the literature case; stream reproduced without the bar.

**Pitfalls.** Spiral arms and the bar compete in producing velocity-space features, so consider the spiral as a systematic uncertainty.

## Option C: Globular clusters in a barred galaxy

**Question.** Which Milky Way globular clusters are significantly affected by the bar, and by how much does it change their tidal mass loss compared with an axisymmetric potential?

**Plan.**
1. Retrieve cluster positions, distances, proper motions and masses (Vasiliev and Baumgardt 2021; Baumgardt and Hilker 2018).
2. Integrate their orbits for 5 Gyr in axisymmetric and barred potentials. Sample the observational errors by Monte Carlo.
3. Classify the orbits with frequency analysis (Module 09) and locate resonances.
4. Compute a mass-loss estimate along each orbit through an analytic prescription for tidal heating and compare the two potentials. Validate this prescription for a few clusters by direct N-body simulation in the actual orbit.
5. Report which clusters are bar-affected and the sensitivity to $\Omega_p$.

**Validation.** Axisymmetric limit matches `galpy`/`gala` orbits; direct N-body mass loss matches the analytic estimate within a stated tolerance.

## Option D: Schwarzschild modelling of an elliptical galaxy

**Question.** How well can the mass, anisotropy and (for a triaxial system) shape be recovered from line-of-sight data, and what degeneracies limit the answer?

**Plan.**
1. Build a mock triaxial galaxy (a Dehnen $\gamma$-model with a known potential, or a relaxed N-body remnant) and generate mock integral-field kinematics with realistic noise and a PSF.
2. Implement the Schwarzschild method with a regular orbit library including chaotic orbits (Module 11).
3. Fit the mock data, scanning potential parameters (mass normalization, axis ratios), and compute the confidence region.
4. Quantify the biases and degeneracies (mass-anisotropy, shape, inclination).
5. Optionally apply the code to published kinematics of a real galaxy.

**Validation.** Known input recovered within the uncertainties; convergence with orbit number and with the number of cells.

## Option E: Core formation by black-hole binaries in mergers

**Question.** How does the stellar mass deficit created by a black hole binary scale with the black hole mass and with the mass ratio of the merger?

**Plan.**
1. Build equilibrium cuspy galaxies with a central black hole. Merge pairs on parabolic and hyperbolic orbits with mass ratios 1:1 to 1:4.
2. Track the binary's hardening, the central density profile and the mass deficit, with convergence tests in $N$.
3. Compare with published scalings and discuss the "final parsec problem" and its consequences.

**Validation.** Energy conservation in the binary; convergence with $N$ and softening; control run without black holes.

## Option F: How does a bar reshape a globular cluster system?

**Question.** A rotating bar changes the orbits of clusters. Does it redistribute the cluster system's kinematics (anisotropy, angular momentum distribution, spatial distribution), and is this effect visible in the Milky Way's cluster system?

**Plan.**
1. Use an N-body bar-forming galaxy from Option A (or a rigid analytic bar with growth) and a set of tracer clusters placed initially with an equilibrium halo-like distribution (and a disk-like population).
2. Follow the cluster orbits as the bar forms and evolves. Measure the angular momentum change as a function of resonance and initial orbit (Module 09).
3. Measure the final distribution of the cluster population: radial and tangential velocity dispersions, spatial distribution (bar-aligned clustering), and how many are trapped in resonances.
4. Compare with the observed cluster kinematics of the Milky Way (Vasiliev and Baumgardt 2021).
5. For a subset, run direct N-body models of the clusters in the evolving field to estimate the mass loss.

**Validation.** Same checks as Options A and C, plus a control run with an unbarred galaxy.

## Deliverables for every option

- A repository under `capstone/` with `README.md`, configuration files, scripts and tests. `make all` (or a single script) reproduces every figure.
- A written note (Markdown or LaTeX) of 10 to 15 pages, with uncertainties on every number.
- A one-page "limitations and what I would do next" section.
- A 15-minute talk outline.

## Grading rubric (for self-assessment)

| Criterion | What full marks look like |
| --- | --- |
| Correctness | All tests pass, known limits reproduced, conserved quantities tracked |
| Convergence | Results shown to be insensitive to particle number, time step, softening and library size within the stated errors |
| Uncertainties | Bootstrap, multiple seeds or posterior distributions, not a single run |
| Reproducibility | Anyone can rebuild every figure from the repository |
| Physics insight | The discussion links the result to the resonance and angular-momentum picture of Modules 08 to 10 |
| Honesty | Limitations and failed attempts stated openly |

## What comes after

Possible next steps: contribute a well-tested module to `galpy` or `gala`; write the work up for a conference proceeding or a research note; extend the program with gas dynamics and star formation (hydrodynamical simulations), cosmological zoom-in simulations of barred galaxies, or distribution-function-based dynamical modelling (made-to-measure and the actions-based methods in `AGAMA`).
