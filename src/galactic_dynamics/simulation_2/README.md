# Simulation 2: Introducing the Bar and Breaking Symmetry

## Scientific Question

Once a galaxy develops a non-axisymmetric bar:

> What happens to a star's constants of motion when spatial symmetry is broken, and how does a rotating potential rewrite the rules of stellar paths?

You are moving from a static, predictable sandbox to a dynamic, time-dependent system.

---

# Goal

Modify your miniature galaxy by introducing a rotating central bar:

```text
Axisymmetric Potential
+
Rotating Bar Perturbation
+
One test star

```

No $N$-body self-gravity yet. We isolate how individual orbits respond to a pre-existing bar potential rotating at a constant pattern speed $\Omega_p$.

---

# What You Will Learn

By the end you should know:

* Why angular momentum ($L_z$) is no longer conserved
* What the Jacobi Constant ($E_J$) is and why it replaces energy
* How Lagrange points ($L_1$ through $L_5$) manifest in a galactic potential
* How to visually identify the Corotation Resonance (CR)

---

# Step 1: Upgrade the Potential

Keep your background Plummer sphere (or switch to a flat-rotation logarithmic potential), but superimpose a rotating, non-axisymmetric bar perturbation.

We use a smoothed, analytical bar profile to keep the math elegant.

Potential in polar coordinates $(r, \phi)$ within the frame rotating at pattern speed $\Omega_p$:

$$\Phi_{\text{bar}}(r, \phi) = A_{\text{bar}} \cos(2\phi) \frac{r^2}{(r^2 + r_{\text{bar}}^2)^{5/2}}$$

Choose parameters:

```text
A_bar = 0.1   # Amplitude (strength of the bar)
r_bar = 2.0   # Scale radius of the bar
Omega_p = 0.2 # Pattern speed (rotation speed of the bar)

```

---

# Step 2: Derive Acceleration in the Rotating Frame

You have two choices: integrate in the inertial frame with a time-dependent potential $\Phi(r, \phi - \Omega_p t)$, or integrate in the *rotating frame* where the potential is static but fictitious forces appear.

We choose the rotating frame because a static potential is vastly easier to analyze.

Compute the inertial gradients ($-\nabla \Phi$) and add the Coriolis and Centrifugal terms:

$$a_x = -\frac{\partial \Phi_0}{\partial x} - \frac{\partial \Phi_{\text{bar}}}{\partial x} + 2\Omega_p v_y + \Omega_p^2 x$$

$$a_y = -\frac{\partial \Phi_0}{\partial y} - \frac{\partial \Phi_{\text{bar}}}{\partial y} - 2\Omega_p v_x + \Omega_p^2 y$$

---

# Step 3: Implement the Analytic Derivatives

To feed your integrator, explicitly write out the cartesian derivatives for the bar potential using $\cos(2\phi) = (x^2 - y^2)/r^2$:

```python
# Let denom = (x^2 + y^2 + r_bar^2)^3.5
# d(Phi_bar)/dx:
fx_bar = -A_bar * (x * (2 * r_bar**2 - 3 * x**2 + 7 * y**2)) / denom

# d(Phi_bar)/dy:
fy_bar = -A_bar * (y * (-2 * r_bar**2 - 7 * x**2 + 3 * y**2)) / denom

```

---

# Step 4: Run the First Barred Experiment

Launch a star outside the bar on a pristine circular orbit from Simulation 1:

```python
x = 5.0
y = 0.0
vx = 0.0
vy = vc_plummer(5.0)

```

Run for 2000 timesteps using your Leapfrog integrator. Plot $x$ versus $y$.

---

# Question

Does the star trace out a clean, precessing rosette like it did in Simulation 1?

---

# Expected Result

The orbit looks erratic, distorted, or completely boxy. It might change its radial extent dramatically.

---

# Step 5: Monitor the Classical Constants

Plot standard energy $E(t) = \frac{1}{2}v^2 + \Phi_0 + \Phi_{\text{bar}}$ and angular momentum $L_z(t) = xv_y - yv_x$ over time.

---

# Question

Are they conserved?

---

# Discovery

Both $E(t)$ and $L_z(t)$ vary wildly over time.

Because the bar breaks axisymmetry, torque is applied to the star $\left(\frac{dL_z}{dt} = -\frac{\partial \Phi}{\partial \phi} \neq 0\right)$, trading angular momentum back and forth. Because the system is time-dependent in the inertial frame, energy is pumped into and out of the orbit.

---

# Step 6: Discover the Jacobi Constant

Now, compute and plot the **Jacobi Integral ($E_J$)** at every timestep:

$$E_J = \frac{1}{2}(v_x^2 + v_y^2) + \Phi_0(x,y) + \Phi_{\text{bar}}(x,y) - \frac{1}{2}\Omega_p^2(x^2 + y^2)$$

---

# Question

What does the profile of $E_J(t)$ look like?

---

# Expected Result

A completely flat line.

---

# Scientific Lesson

Symmetry broken in space (no axisymmetry) $\rightarrow$ $L_z$ dies.
Symmetry preserved in time (static in rotating frame) $\rightarrow$ $E_J$ lives.

The Jacobi constant is now your *only* map through phase space.

---

# Step 7: Find the Corotation Resonance (CR)

Let's locate where the star's orbital frequency matches the bar's rotation speed.

From your Simulation 1 rotation curve, find the radius $R_c$ where:

$$\Omega(R_c) = \Omega_p$$

Place a test star precisely at $x = R_c, y = 0$ with zero relative velocity in the rotating frame ($vx=0, vy=0$).

---

# Run Simulation

Question:

What happens to a star left at rest exactly where the bar's speed matches the circular orbit speed?

---

# Expected Result

If placed along the major or minor axis of the bar, it will either sit completely still or slowly loop around a specific point like a Trojan asteroid.

---

# Discovery: The Effective Potential and Lagrange Points

You just discovered the Lagrange points of a galaxy. By plotting the "Effective Potential":

$$\Phi_{\text{eff}}(x, y) = \Phi_0 + \Phi_{\text{bar}} - \frac{1}{2}\Omega_p^2(x^2 + y^2)$$

as a 3D surface or contour map, you will see five equilibrium points where $\nabla \Phi_{\text{eff}} = 0$.

* $L_1, L_2$: Ridges along the bar major axis (stars can escape the bar here).
* $L_4, L_5$: Stable valleys $90^\circ$ ahead and behind the bar (stars orbit these points in tadpole or horseshoe paths).

---

# Step 8: Create the Simulation 2 Report

Write 5 pages analyzing your data.

## Methods

Explain how you coded the non-inertial frame forces.

## Results

* Show the simultaneous destruction of $L_z$ and preservation of $E_J$.
* Contour plot of $\Phi_{\text{eff}}(x, y)$ marking the positions of $L_1$ through $L_5$.
* Plot of a "Corotation orbit" trapping a particle near $L_4$.

## Discussion

Answer:

* If $L_z$ isn't conserved, how can we categorize galactic orbits long-term?
* Why do stars leak out of the galaxy primarily near the ends of the bar ($L_1/L_2$)?

---

# Final Outcome

You have unlocked the fundamental language Binney & Tremaine use for non-axisymmetric systems:

```text
Rotating Bar
    ↓
Torque (dPhi/dphi != 0)
    ↓
Loss of L_z conservation
    ↓
Emergence of Jacobi Constant (E_J)
    ↓
Effective Potential Landscapes
    ↓
Lagrange Points & Corotation

```

Now you are fully armed to tackle **Simulation 3: Resonant Orbit Families ($x_1$ and $x_2$) and Poincaré Sections**, where we finally see how stars align themselves to physically construct and support the bar structure! How does this second leg of the journey look?
