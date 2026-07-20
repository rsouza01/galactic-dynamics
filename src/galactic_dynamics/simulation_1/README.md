# Simulation 1: The Galaxy Without a Bar

## Scientific Question

Before understanding bars, answer:

> What does a star do in an ordinary axisymmetric galaxy?

You need intuition before complexity.

***

# Goal

Build a miniature galaxy consisting only of:

```text
Potential
+
One test star
```

No bar.
No N-body.
No halo particles.
No collisions.

Just a star moving in a smooth gravitational field.

***

# What You Will Learn

By the end you should know:

* Why circular orbits exist
* Why most stellar orbits are not circular
* What energy conservation looks like
* What angular momentum conservation looks like
* How orbit integration behaves numerically

***

# Step 1: Choose a Potential

Start with the Plummer sphere.

Reason:

The math is easy.

Potential:

$$\Phi(r) = -\frac{GM}{\sqrt{r^2+a^2}}$$

Choose:

```text
G = 1
M = 1
a = 1
```

Astronomers love code units.

Forget physical units initially.

***

# Step 2: Derive the Acceleration

The integrator never needs the potential.

It needs acceleration.

Compute:

$$
\vec a
=
-\nabla \Phi
$$

Result:

$$
a_x
=
-\frac{GMx}
{(r^2+a^2)^{3/2}}
$$

$$
a_y
=
-\frac{GMy}
{(r^2+a^2)^{3/2}}
$$

***

# Step 3: State Vector

Represent a star as:

```python
[x,y,vx,vy]
```

Example:

```python
x = 5
y = 0
vx = 0
vy = 0.3
```

***

# Step 4: First Integrator

Use RK4.

Not because it's best.

Because it's easy.

Write:

```python
rk4_step(state,dt)
```

***

# First Experiment

Run:

```text
1000 timesteps
```

Plot:

```python
x versus y
```

Question:

What shape appears?

***

# Expected Result

Probably an ellipse-like rosette.

Not a closed Kepler ellipse.

This surprises many people.

***

# What You Learn

Galactic potentials differ from Kepler potentials.

The orbit precesses.

This concept later becomes enormously important for bars.

***

# Step 5: Monitor Energy

Compute every timestep:

$$
E
=
\frac12v^2+\Phi
$$

Plot:

```python
E(t)
```

***

# Question

Does energy remain constant?

If not:

* timestep too large
* bug

This is your first diagnostic tool.

***

# Step 6: Angular Momentum

Calculate

$$
L_z=xv_y-yv_x
$$

Plot:

```python
Lz(t)
```

Question:

Is it conserved?

It should be.

***

# Scientific Lesson

Axisymmetry

↓

Angular momentum conservation

This connection is fundamental.

Later:

Bar

↓

No axisymmetry

↓

Angular momentum changes

That's literally the story of barred galaxies.

***

# Step 7: Build Circular Orbits

Most people skip this.

Don't.

***

Find:

$$
v_c(r)
=
\sqrt{r \frac{d\Phi}{dr}}
$$

At:

```text
r = 5
```

Compute circular velocity.

Set:

```python
vx=0
vy=vc
```

***

# Run Simulation

Question:

What happens?

***

# Expected Result

Perfect circle.

Or nearly perfect.

***

# Important Insight

The circular orbit is not generic.

It is a special orbit.

Most stars do something more complicated.

***

# Step 8: Perturb the Orbit

Now increase velocity by 2%.

```python
vy = 1.02 * vc
```

Run again.

***

# Question

Why doesn't the star fly away?

***

# Discovery

It oscillates around the circular orbit.

Congratulations.

You just discovered epicyclic motion experimentally.

Before reading the equations.

This is exactly how I would learn it.

***

# Step 9: Build a Rotation Curve

Now stop integrating.

Let's study the galaxy itself.

***

Create:

```python
r = [0.1 ... 20]
```

For each radius compute:

$$
v_c(r)
$$

Plot

```text
radius
versus
circular velocity
```

***

# Why This Matters

Every resonance in barred dynamics depends on:

$$
\Omega(r)
=
\frac{v_c(r)}{r}
$$

Later you'll use this everywhere.

***

# Step 10: Build Ω(r)

Calculate:

$$
\Omega(r)
=
v_c(r)/r
$$

Plot.

***

# Interpretation

This is the angular frequency of stars.

Think:

```text
How fast stars orbit
as a function of radius.
```

***

# Step 11: Compare Numerical Methods

This is where Newman enters.

Use:

### RK4

and

### Leapfrog

Integrate same orbit.

Same time.

Same timestep.

***

# Measure

Energy error.

Plot

```text
Energy Error
versus Time
```

***

# Discovery

RK4:

```text
more accurate short-term
```

Leapfrog:

```text
better long-term
```

This is one of the most important lessons in computational astrophysics.

***

# Step 12: Create Your First Scientific Report

Write 5 pages.

Include:

## Potential

Explain Plummer model.

***

## Methods

Explain integration.

***

## Results

Show:

* orbit
* energy conservation
* angular momentum conservation
* rotation curve

***

## Discussion

Answer:

Why was angular momentum conserved?

Why did the orbit precess?

Why wasn't every orbit circular?

***

# Final Outcome

You have not learned "coding."

You have learned:

```text
Potential
    ↓
Force
    ↓
Orbit
    ↓
Integrals of motion
    ↓
Rotation curve
    ↓
Angular frequency
```

This chain is the foundation of literally everything that comes later.

The next simulation (which I would call **Simulation 2: Epicyclic Theory and Resonances**) would then build directly on this and end with computing the Lindblad resonances that control barred-galaxy dynamics. That's where the road toward actual bars truly begins. 🌌📈
