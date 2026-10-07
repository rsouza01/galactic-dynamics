# Module 03: Orbits in spherical and axisymmetric potentials

**Difficulty:** Medium. **Time:** about 3 weeks.

## Goal

Integrate orbits reliably, understand what the integrals of motion are, see order and chaos on surfaces of section, and compute epicycle frequencies and Oort constants. This is the foundation for bars (Module 08) and resonances (Module 09).

## Prerequisites

Modules 01 and 02. Hamiltonian mechanics.

## Reading

- **B&T Ch. 3:** orbits in spherical potentials (rosettes, radial period, apsidal angle), orbits in axisymmetric potentials (the effective potential, epicycles, the third integral), numerical orbit integration, and the introduction to angle-action variables.
- **S&G topics:** stellar orbits in disks, epicycle approximation, Oort constants.
- **Paper:** Henon and Heiles (1964), for the classic model of order and chaos.

## Key equations (derive)

Spherical potential $\Phi(r)$ with energy $E$ and angular momentum $L$. The radial period and the azimuthal advance per radial period:

$$T_r = 2\int_{r_-}^{r_+}\frac{dr}{\sqrt{2[E-\Phi(r)] - L^2/r^2}}, \qquad \Delta\varphi = 2\int_{r_-}^{r_+}\frac{L\,dr/r^2}{\sqrt{2[E-\Phi(r)]-L^2/r^2}}$$

Limits to know: $\Delta\varphi = 2\pi$ for a Kepler potential, $\pi$ for a harmonic potential (a homogeneous core), and values in between for real galaxies. Orbits in a general spherical potential are rosettes.

Axisymmetric potential $\Phi(R,z)$, circular frequency $\Omega$, epicycle frequency $\kappa$ and vertical frequency $\nu$:

$$\Omega^2 = \frac{1}{R}\frac{\partial\Phi}{\partial R}, \qquad \kappa^2 = R\frac{d\Omega^2}{dR} + 4\Omega^2 = \frac{\partial^2\Phi}{\partial R^2} + 3\Omega^2, \qquad \nu^2 = \frac{\partial^2\Phi}{\partial z^2}\Big|_{z=0}$$

Limits: $\kappa = 2\Omega$ for solid-body rotation, $\kappa=\sqrt2\,\Omega$ for a flat rotation curve, $\kappa=\Omega$ for Kepler.

Oort constants and their relation to $\Omega$ and $\kappa$:

$$A = \tfrac12\left(\frac{v_c}{R} - \frac{dv_c}{dR}\right), \qquad B = -\tfrac12\left(\frac{v_c}{R} + \frac{dv_c}{dR}\right), \qquad \Omega = A - B, \qquad \kappa^2 = -4B(A-B)$$

For reference, the solar neighbourhood values are roughly $A\approx15$ and $B\approx-12$ km/s/kpc.

Leapfrog (kick-drift-kick), which is symplectic and time-reversible:

$$v_{n+1/2} = v_n + \tfrac{\Delta t}{2}a(x_n),\quad x_{n+1} = x_n + \Delta t\, v_{n+1/2},\quad v_{n+1} = v_{n+1/2}+\tfrac{\Delta t}{2}a(x_{n+1})$$

## Hands-on problems

**1. [E] Orbit integrators.** In `orbits/integrators.py`, implement kick-drift-kick leapfrog, classical RK4, and a wrapper around `scipy.integrate.solve_ivp` with `DOP853` and tight tolerances. Integrate a Kepler orbit with eccentricity 0.9 for 1000 periods with each. Plot the relative energy error against time. *Expected:* leapfrog shows a bounded oscillating error, RK4 a secular drift, and DOP853 at tolerance $10^{-12}$ is excellent for this problem but will drift in a very long run.

**2. [E] Rosettes.** Integrate orbits in a Plummer potential, an NFW potential, and the Kepler potential, with the same $(E, L)$ type of initial conditions. Measure $\Delta\varphi$ per radial period and confirm: close to $2\pi$ in Kepler, close to $\pi$ for small orbits in a Plummer core, and strictly between for NFW.

**3. [M] Radial period two ways.** Compute $T_r$ by direct quadrature (careful with the integrable endpoint singularities, use the substitution $r=\tfrac12(r_++r_-)+\tfrac12(r_+-r_-)\sin\theta$) and by timing orbit crossings. The two should agree to $10^{-6}$.

**4. [M] Epicycles.** In a logarithmic potential with $v_0=220$ km/s, compute $\kappa$ numerically and confirm $\kappa=\sqrt2\,\Omega$. Integrate a slightly eccentric near-circular orbit and compare the radial oscillation period with $2\pi/\kappa$. Repeat for the Miyamoto-Nagai + halo model from Module 02 at $R=8.2$ kpc. Compute $A$ and $B$ from the rotation curve and check $\Omega=A-B$ and $\kappa^2=-4B(A-B)$.

**5. [M] Henon-Heiles surface of section.** For the potential $\Phi=\tfrac12(x^2+y^2)+x^2y-\tfrac13y^3$, write a surface-of-section routine using `solve_ivp` events (crossings of $x=0$ with $p_x>0$). Make the section for $E = 1/12$, $1/8$ and $1/6$. *Expected:* at $E=1/12$ nearly all orbits lie on smooth invariant curves, at $1/8$ islands and a growing chaotic sea coexist, at $1/6$ most of the section is chaotic.

**6. [M] Lyapunov exponents.** For two orbits in Henon-Heiles (one regular, one chaotic), estimate the largest Lyapunov exponent by integrating a nearby orbit and renormalizing the separation periodically. Regular orbits give an exponent consistent with zero, with the separation growing linearly, and chaotic orbits give a clearly positive exponent.

**7. [M] Third integral.** In an axisymmetric potential, $\Phi=\tfrac12v_0^2\ln\big(R_c^2+R^2+z^2/q^2\big)$ with $q=0.9$, make the $(R,v_R)$ section at $z=0$, $v_z>0$ for a few energies. Most orbits fill smooth curves, which is evidence for a third integral that is not conserved exactly but acts nearly so.

**8. [H] Non-axisymmetric planar log potential.** Use the planar logarithmic potential with $q_y=0.9$ and a small core $R_c$. Classify orbits into boxes (no fixed sense of rotation, pass near the center) and loops (tubes, with constant sign of $L_z$). Identify box-like chaotic orbits near the center with small $R_c$. Count how the fraction of each family depends on $R_c$ and on $E$.

**9. [H] Angle-action variables.** Use `galpy`'s Staeckel approximation (or `AGAMA`) to compute the actions $(J_R, J_\varphi, J_z)$ along a long integrated orbit in a Milky Way-like axisymmetric potential. Plot the action scatter as a fraction of its mean for different orbit eccentricities and heights. Then repeat with your own epicycle-approximation estimate of $J_R$ and compare. This prepares the ground for resonances (Module 09).

## Checks

- Leapfrog bounded energy error and RK4 drift reproduced in problem 1.
- $\Delta\varphi\approx2\pi$ and $\pi$ in the two limiting potentials.
- Oort relations satisfied to $10^{-6}$ for an analytic model.
- Henon-Heiles sections look as described. A good practice is to make a figure for each energy and save it in `notebooks/`.

## Pitfalls

- Using adaptive-step integrators for very long orbit integrations: they usually do not conserve energy over long times, and you should prefer a symplectic scheme with a fixed or time-symmetrically adapted step.
- Making a surface of section without interpolating to the crossing: you get a smeared figure. Use event detection or interpolate linearly.
- Forgetting that $L_z$ is a conserved quantity only in axisymmetric potentials. In Module 08 it will not be.

## Gate questions

1. Why does the existence of a third integral in axisymmetric potentials make the orbits "almost" three-dimensional tori?
2. Explain in your own words why leapfrog's energy error is bounded while RK4's is not.
3. Derive $\kappa^2=-4B(A-B)$ from the definitions of $A$, $B$, $\Omega$.

## Deliverable

`orbits/` package (integrators, surfaces of section, Lyapunov estimator) with tests, and `notebooks/03_orbits.ipynb` with the energy-error plot, the Henon-Heiles sections and the epicycle checks.
