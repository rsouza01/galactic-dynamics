# From Galactic Dynamics to Barred Galaxy Simulations

## Goal

Develop a research-level understanding of:

- Barred spiral galaxies
- Orbital structure in bars
- Resonances
- Secular evolution
- Rotation curves
- Stellar dynamics in disks
- N-body simulations
- Numerical modeling in Python

End objective:

> Build and analyze self-consistent barred galaxy simulations, understand the underlying orbital physics, and reproduce classic results from the literature.

---

# Phase 0 — Preparation

Duration: 2–3 weeks

Before touching bars, make sure you are comfortable with:

- Hamiltonian mechanics
- Canonical transformations
- Rotating reference frames
- Classical orbital dynamics

Fortunately your physics background already covers most of this.

Quick review topics:

- Effective potentials
- Jacobi integral
- Lagrange points
- Resonances
- Action-angle variables (at least conceptually)

---

# Phase 1 — Galactic Dynamics Foundations

Duration: 6–8 weeks

## Main Reference

### Binney & Tremaine

Read thoroughly:

### Chapter 1
Introduction

Understand:

- Collisionless systems
- Timescales
- Why galaxies are not gases

---

### Chapter 2
Potential Theory

Master:

- Poisson equation
- Multipole expansions
- Disk potentials
- Spherical potentials

Implement:

- Plummer sphere
- Hernquist sphere
- NFW halo

Python project:

```python
def v_circular(r):
    return np.sqrt(r * dPhi_dr)
```

Generate:

- Circular velocity curves
- Mass profiles

---

### Chapter 3
The Orbits of Stars

This chapter is absolutely critical.

Study:

- Integrals of motion
- Surfaces of section
- Resonant orbits
- Orbit families

Python projects:

- RK4 integrator
- Leapfrog integrator

Simulate:

- Circular orbit
- Elliptical orbit
- Box orbit
- Loop orbit

Produce:

- Phase-space plots
- Poincaré sections

---

# Phase 2 — Computational Physics

Duration: 4–6 weeks

## Newman

Focus on:

### Numerical integration

Use:

- Simpson
- Gaussian quadrature

Reason:

Galaxy potentials often require numerical integration.

---

### ODE solvers

Master:

- Euler
- RK2
- RK4
- Adaptive RK

Then compare with:

- Leapfrog
- Velocity-Verlet

Important observation:

For long orbit integration,

```text
Leapfrog > RK4
```

because symplectic structure matters.

Learn this experimentally.

---

### FFT chapters

Critical later for:

- Particle mesh methods
- Potential solving

---

### Monte Carlo

Used later for:

- Initial particle distributions
- Distribution functions

---

# Phase 3 — Disk Dynamics

Duration: 6–8 weeks

Return to Binney & Tremaine.

## Chapter 6

Disk Dynamics and Spiral Structure. 【1-e55d2f】【2-d304e0】

Study:

- Rotation curves
- Epicyclic theory
- Stability
- Density waves

Key concepts:

### Angular velocity

\[
\Omega(r)
\]

### Epicyclic frequency

\[
\kappa(r)
\]

### Resonance condition

\[
m(\Omega-\Omega_p)=\pm \kappa
\]

Where:

- Ω = orbital frequency
- Ωp = pattern speed

This equation essentially governs barred galaxy dynamics.

---

# Phase 4 — Understanding Bars

Duration: 2–3 months

This is where the fun begins.

---

## Read

### Athanassoula reviews

Especially:

- Bar formation
- Secular evolution
- Angular momentum transfer
- Resonances

Athanassoula's work emphasizes that angular momentum redistribution drives bar evolution and that resonances play the central role. 【3-5820e4】【4-bdf176】

---

## Learn These Concepts

### Pattern Speed

\[
\Omega_p
\]

The entire bar rotates as a rigid pattern.

Not the stars.

The pattern.

This distinction is crucial.

---

### Corotation Radius

Location where:

\[
\Omega(r)=\Omega_p
\]

Stars rotate with the bar.

---

### Inner Lindblad Resonance

ILR

\[
\Omega-\Omega_p=\kappa/2
\]

---

### Outer Lindblad Resonance

OLR

\[
\Omega-\Omega_p=-\kappa/2
\]

---

### Corotation Resonance

CR

\[
\Omega=\Omega_p
\]

---

# Phase 5 — Orbital Families

Duration: 1 month

This is arguably the most beautiful part of barred dynamics.

The bar exists because orbit families support it.

The important family:

## x1 Orbits

These:

- align with the bar
- support the bar
- create its backbone

Without x1 orbits:

No bar.

---

Other families:

### x2

Perpendicular to bar.

Usually inside ILR.

---

### x4

Retrograde.

---

Project:

Create a rotating bar potential.

Integrate thousands of orbits.

Classify:

- x1
- x2
- chaotic

---

# Phase 6 — First Bar Simulation

Duration: 1 month

Create a fixed bar.

Not self-consistent yet.

Use:

## Disk

Miyamoto-Nagai

## Halo

NFW

## Bar

Ferrers bar

Classic choice.

Simulate:

```text
Disk
+
Halo
+
Rotating bar
```

Compute:

- Stellar trajectories
- Resonances
- Orbit trapping

Visualize:

- Face-on disk
- Bar frame

---

# Phase 7 — GalPy

Duration: 1 month

Now stop coding everything yourself.

Learn GalPy.

It already has:

- Disk potentials
- Halo potentials
- Bar potentials
- Orbit integration

Use it to reproduce:

- Milky Way bar
- Resonance maps
- Orbit families

You learn much faster once the framework handles the boilerplate.

---

# Phase 8 — Self-Consistent N-Body Bars

Duration: 2–3 months

Now let the bar form naturally.

Essential idea:

Start from:

```text
Axisymmetric disk
+
Dark matter halo
```

Add particles.

Wait.

A bar develops.

This is one of the classic results of galactic dynamics.

Numerical simulations revealed that galaxies evolve and bars emerge through secular processes rather than remaining static systems. 【4-bdf176】

---

## Build

Direct gravity:

```text
O(N²)
```

Start with:

- 1000 particles
- 5000 particles

Observe:

- Disk instability
- Bar formation

Measure:

- Bar length
- Pattern speed
- Strength

---

# Phase 9 — Angular Momentum Transport

Duration: 1 month

This is the modern view of bars.

Study:

- Disk-halo interactions
- Resonant exchanges
- Secular evolution

The fundamental picture is that resonant material in the bar emits angular momentum while material in the outer disk and halo absorbs it, driving the long-term evolution of the bar. 【3-5820e4】【4-bdf176】

Questions:

- Why do bars strengthen?
- Why do bars slow down?
- What role does the halo play?

These are research-level questions.

---

# Phase 10 — Research-Level Topics

Only after everything above.

Choose one.

---

## Topic A

Boxy/Peanut Bulges

Study:

- Vertical resonances
- Buckling instability

---

## Topic B

Chaos in Bars

Study:

- Lyapunov exponents
- Chaotic orbits
- Sticky regions

---

## Topic C

Bar-Halo Interaction

Study:

- Dark matter response
- Halo resonances

---

## Topic D

Milky Way Bar

Use Gaia data.

Study:

- Hercules stream
- Resonance structures
- Local stellar kinematics

---

# Simulation Roadmap

## Project 1

Kepler problem

---

## Project 2

Plummer sphere

---

## Project 3

Hernquist galaxy

---

## Project 4

NFW halo

---

## Project 5

Rotation curves

---

## Project 6

Epicyclic approximation

---

## Project 7

Poincaré sections

---

## Project 8

Fixed Ferrers bar

---

## Project 9

Orbit-family classification

---

## Project 10

Self-generated bar via N-body

---

# Essential Reading Order

## Mandatory

1. Binney & Tremaine Ch. 2
2. Binney & Tremaine Ch. 3
3. Newman ODE chapters
4. Newman FFT chapters
5. Binney & Tremaine Ch. 4
6. Binney & Tremaine Ch. 5
7. Binney & Tremaine Ch. 6

The second edition of Binney & Tremaine significantly expanded coverage of numerical simulations, orbit theory, stability, and galaxy evolution and remains the standard reference in the field. 【1-e55d2f】【2-d304e0】

---

# Final Goal

If you complete all phases, you should be able to:

- Derive and interpret resonance locations
- Explain why bars form
- Explain why bars evolve
- Identify x1/x2 orbital families
- Build a self-consistent barred galaxy simulation
- Read Athanassoula, Sellwood, and contemporary barred-galaxy papers comfortably
- Design your own galactic dynamics research projects

That is essentially the path from "astrophysicist interested in galaxies" to "competent galactic dynamicist."
````
