# Module 02: Potential theory and galaxy mass models

**Difficulty:** Easy to medium. **Time:** about 2 weeks.

## Goal

Build a library of analytic potential-density pairs for spheres, disks and bars, verify each against Poisson's equation numerically, and write a general Poisson solver. Every later module uses these classes.

## Prerequisites

Module 01. Vector calculus, Legendre polynomials, Green's functions.

## Reading

- **B&T Ch. 2**: Newton's theorems, potential-density pairs for spherical systems, the multipole expansion, flattened systems (Kuzmin, Miyamoto-Nagai), potential energy and the virial theorem, Poisson's equation with Green's functions.
- **S&G topics:** mass models, density laws for spheroids and disks.
- **Paper:** Dehnen (1993), *A family of potential-density pairs for spherical galaxies and bulges*.

## Key equations (derive each one)

Poisson's equation and the circular speed:

$$\nabla^2\Phi = 4\pi G\rho, \qquad v_c^2(R) = R\,\frac{\partial\Phi}{\partial R}\Big|_{z=0}$$

**Spherical models** ($M$ the total mass, $a$ or $b$ the scale radius):

| Model | Density | Potential |
| --- | --- | --- |
| Plummer | $\rho = \dfrac{3M}{4\pi b^3}\left(1+\dfrac{r^2}{b^2}\right)^{-5/2}$ | $\Phi = -\dfrac{GM}{\sqrt{r^2+b^2}}$ |
| Hernquist | $\rho = \dfrac{M}{2\pi}\dfrac{a}{r(r+a)^3}$ | $\Phi = -\dfrac{GM}{r+a}$ |
| NFW | $\rho = \dfrac{\rho_0}{(r/r_s)(1+r/r_s)^2}$ | $\Phi = -4\pi G\rho_0 r_s^3\,\dfrac{\ln(1+r/r_s)}{r}$ |
| Singular isothermal | $\rho = \dfrac{\sigma^2}{2\pi G r^2}$ | $\Phi = v_c^2\ln r + {\rm const}$, with $v_c = \sqrt2\,\sigma$ |

NFW enclosed mass: $M(<r) = 4\pi\rho_0 r_s^3\left[\ln(1+x) - \dfrac{x}{1+x}\right]$ with $x = r/r_s$.

**The Dehnen $\gamma$-family** (Hernquist is $\gamma=1$, Jaffe is $\gamma=2$):

$$\rho = \frac{(3-\gamma)M}{4\pi}\frac{a}{r^\gamma (r+a)^{4-\gamma}}, \qquad \Phi = -\frac{GM}{a}\,\frac{1}{2-\gamma}\left[1 - \left(\frac{r}{r+a}\right)^{2-\gamma}\right]\ (\gamma\ne 2)$$

**Axisymmetric disk models.** Miyamoto-Nagai:

$$\Phi = -\frac{GM}{\sqrt{R^2 + \left(a + \sqrt{z^2+b^2}\right)^2}}$$

Exponential disk $\Sigma = \Sigma_0 e^{-R/R_d}$ (thin, derive via Bessel functions; Freeman 1970), with $y = R/2R_d$:

$$v_c^2(R) = 4\pi G\Sigma_0 R_d\, y^2\left[I_0(y)K_0(y) - I_1(y)K_1(y)\right]$$

**Bar and triaxial models.** The logarithmic potential, flattened along $y$ and $z$ and used in Modules 03 and 08:

$$\Phi_L = \tfrac12 v_0^2\ln\left(R_c^2 + x^2 + \frac{y^2}{q_y^2} + \frac{z^2}{q_z^2}\right)$$

Potential energy of a homogeneous ellipsoid with semi-axes $a_1\ge a_2\ge a_3$ inside the body, as a one-dimensional integral, with $\Delta(\tau) = \sqrt{(a_1^2+\tau)(a_2^2+\tau)(a_3^2+\tau)}$:

$$\Phi(\mathbf x) = -\pi G\rho\, a_1a_2a_3\int_0^\infty \left[1 - \sum_i \frac{x_i^2}{a_i^2+\tau}\right]\frac{d\tau}{\Delta(\tau)}$$

Virial theorem and potential energy: $2K + W = 0$, with $W = -\tfrac12\int\rho\,\Phi_{\rm self}\, d^3x$ for self-gravity. For a Plummer sphere $W = -3\pi GM^2/(32b)$.

## Hands-on problems

**1. [E] Potentials library.** In `potentials/`, write a base class with `phi(x,y,z)`, `rho(x,y,z)`, `acc(x,y,z)` (analytic) and `vc(R)`. Implement Plummer, Hernquist, NFW, isothermal sphere, Miyamoto-Nagai, logarithmic, and the Dehnen $\gamma$-model.

**2. [E] Poisson check.** For every model, evaluate $\nabla^2\Phi$ by finite differences at 100 random points and compare with $4\pi G\rho$. Relative error should be below $10^{-5}$ with a well-chosen step. Do the same for the acceleration versus the numerical gradient of $\Phi$.

**3. [E] Known numbers.** Verify, and then record in your tests:
- Hernquist half-mass radius is $(1+\sqrt2)\,a \approx 2.414\,a$.
- NFW circular speed peaks at $r \approx 2.163\,r_s$.
- Exponential disk (Freeman): $v_c$ peaks near $R \approx 2.15\,R_d$ with $v_{c,\rm max}\approx 0.62\,\sqrt{GM_d/R_d}$.
- The Plummer potential energy above.

**4. [M] Rotation-curve zoo.** On one plot show $v_c(R)$ for Miyamoto-Nagai with $a=3$ kpc, $b=0.3$ kpc, $M=5\times10^{10}M_\odot$; a Hernquist bulge; and an NFW halo with $M_{200}\approx10^{12}M_\odot$ and a plausible concentration. Add them in quadrature for a Milky Way-like total. Check the total is flat to within about 10 percent between 4 and 20 kpc after you tune parameters.

**5. [M] Multipole Poisson solver.** Given a density on a grid (take Miyamoto-Nagai or a flattened Hernquist), expand in Legendre polynomials up to $\ell_{\max}$ and compute $\Phi$ in a few points. Compare with the analytic potential, and plot the error against $\ell_{\max}$ from 0 to 20 for axis points and equatorial points. Why does the convergence differ?

**6. [M] Grid Poisson solver.** Solve $\nabla^2\Phi=4\pi G\rho$ for a Hernquist sphere with an FFT-based convolution on a 3D grid, with zero padding for isolated boundary conditions (Hockney-Eastwood style). Measure the error against grid size.

**7. [M] Cross-validate.** Create the same Miyamoto-Nagai + Hernquist + NFW model in `galpy` or `gala` and in your code. Compare accelerations at 1000 random points, being very careful with units. Reproduce them to better than $10^{-8}$ relative.

**8. [H] Homogeneous ellipsoid.** Implement the integral above with `scipy.integrate.quad`. Check it against the exact sphere limit, against Gauss's law at the center, and against the multipole solver for an ellipsoid with axis ratios 1 : 0.8 : 0.6. This is the first step toward the Ferrers bar potentials of Module 08.

**9. [H] A bar potential.** Implement the quadrupole bar model of Dehnen (2000):

$$\Phi_b = A_b\cos\!\big[2(\varphi - \Omega_p t)\big]\times\begin{cases}-(R/R_b)^3, & R\le R_b\\[2pt] (R_b/R)^3, & R\ge R_b\end{cases}$$

with $A_b$ related to a dimensionless strength $\alpha$ by $A_b = -\alpha\, v_0^2\,(R_0/R_b)^3/3$, as I recall (check the paper). Verify $\Phi_b$ is continuous with a continuous first derivative at $R_b$.

## Checks

- Poisson tests pass at $10^{-5}$ for all models.
- The four known numbers above to better than 1 percent.
- Library cross-check with `galpy` or `gala` to $10^{-8}$ relative.

## Pitfalls

- Mass versus density normalization conventions differ between codes (for NFW, for example, some use $M_{200}$ and concentration, others $\rho_0$ and $r_s$).
- `galpy` and `gala` use internal natural units unless you tell them otherwise.
- The multipole expansion converges slowly for strongly flattened or cuspy systems. Use many terms and test with a known case.

## Gate questions

1. Why does a flat rotation curve imply $\rho\propto r^{-2}$ for a spherical halo?
2. What physical aspects of NFW and of the singular isothermal sphere differ at small and large radius?
3. Derive the Miyamoto-Nagai density from its potential with $\nabla^2\Phi/4\pi G$. For which values of $a$ and $b$ is it positive everywhere? What do the limits $a\to0$ (Plummer) and $b\to0$ (Kuzmin disk) look like?

## Deliverable

`potentials/` package with tests, `notebooks/02_mass_models.ipynb` with the rotation-curve zoo, and a short note in `notes/` with the derivations you did by hand.
