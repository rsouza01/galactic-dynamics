import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# Plummer Potential
# =============================================================================
def phi(x, y, G=1.0, M=1.0, scale_a=1.0):
    """Calculates Plummer potential."""
    r_soft_sq = x**2 + y**2 + scale_a**2
    return -G * M / (r_soft_sq)**(0.5)

# =============================================================================
# Plummer Acceleration Model
# =============================================================================
def acceleration(x, y, G=1.0, M=1.0, scale_a=1.0):
    """Calculates Plummer acceleration components ax, ay."""
    r_soft_sq = x**2 + y**2 + scale_a**2
    prefactor = -G * M / (r_soft_sq**1.5)
    return prefactor * x, prefactor * y

# =============================================================================
# State Derivative Function (dS/dt)
# =============================================================================
def state_derivatives(state, G=1.0, M=1.0, scale_a=1.0):
    """
    Unpacks S = [x, y, vx, vy] and returns dS/dt = [vx, vy, ax, ay].
    """
    x, y, vx, vy = state
    ax, ay = acceleration(x, y, G=G, M=M, scale_a=scale_a)
    return np.array([vx, vy, ax, ay])

# =============================================================================
# Fourth-Order Runge-Kutta Step (RK4)
# =============================================================================
def rk4_step(state, dt, G=1.0, M=1.0, scale_a=1.0):
    """Advances state by time dt using RK4 integration."""
    k1 = state_derivatives(state, G, M, scale_a)
    k2 = state_derivatives(state + 0.5 * dt * k1, G, M, scale_a)
    k3 = state_derivatives(state + 0.5 * dt * k2, G, M, scale_a)
    k4 = state_derivatives(state + dt * k3, G, M, scale_a)
    
    return state + (dt / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)

# =============================================================================
# Fourth-Order Runge-Kutta Step (RK4)
# =============================================================================
def energy(state, G=1.0, M=1.0, scale_a=1.0):
    """Advances state by time dt using RK4 integration."""
    x, y, vx, vy = state

    return 0.5 * (vx**2 + vy**2) + phi(x, y, G, M, scale_a)


# =============================================================================
# Main Simulation & Orbit Integration
# =============================================================================
def run_simulation():
    # Parameters
    G, M, scale_a = 1.0, 1.0, 1.0
    
    # Time settings
    n_steps = 18000
    dt = 0.01
    t_max = n_steps * dt  # Total simulated time = 10.0
    
    # Initial conditions: Position r0 = (2.0, 0.0)
    x0, y0 = 2.0, 0.0
    
    # Circular velocity at r0=2.0 would be v_circ = sqrt(G*M*r^2 / (r^2 + a^2)^(3/2))
    v_circ = np.sqrt((G * M * x0**2) / ((x0**2 + scale_a**2)**1.5))
    
    # Set tangential velocity slightly sub-circular (0.75 * v_circ) to trigger precession
    vx0 = 0.0
    vy0 = 0.75 * v_circ
    
    current_state = np.array([x0, y0, vx0, vy0])
    
    # Arrays to store orbit trajectory for plotting
    x_history = np.zeros(n_steps)
    y_history = np.zeros(n_steps)
    energy_history = np.zeros(n_steps)
    
    # Time Integration Loop
    for i in range(n_steps):
        x_history[i] = current_state[0]
        y_history[i] = current_state[1]
        energy_history[i] = energy(current_state, G, M, scale_a)
        current_state = rk4_step(current_state, dt, G, M, scale_a)
        
    return x_history, y_history, energy_history

# =============================================================================
# 5. Plotting & Saving to Disk
# =============================================================================
def plot_energy(energy_history, filename="./energy.png"):
    # Relative energy error relative to initial value E_0
    rel_energy_error = (energy_history - energy_history[0]) / abs(energy_history[0])

    # Save to disk
    saved_filename = os.path.join(script_dir, filename)

    plt.figure(figsize=(8, 4), dpi=150)
    plt.plot(rel_energy_error, color='crimson', lw=1.2)
    plt.xlabel("Step")
    plt.ylabel(r"$(E(t) - E_0) / |E_0|$")
    plt.title("RK4 Relative Energy Conservation Drift")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(saved_filename, bbox_inches='tight')
    plt.close()
    print(f"Plot successfully saved as '{saved_filename}'")

def plot_and_save(x, y, filename="./plummer_orbit.png"):
    plt.figure(figsize=(7, 7), dpi=300)
    
    # Plot central core marker
    plt.plot(0, 0, 'k*', markersize=12, label="Cluster Center")
    
    # Plot orbit history
    plt.plot(x, y, color='tab:blue', lw=1.2, label="Star Trajectory")
    plt.plot(x[0], y[0], 'go', label="Initial Position")
    
    plt.axhline(0, color='gray', linestyle=':', alpha=0.5)
    plt.axvline(0, color='gray', linestyle=':', alpha=0.5)
    
    plt.xlabel(r"$x \quad [a]$")
    plt.ylabel(r"$y \quad [a]$")
    plt.title("Stellar Orbit in a Plummer Potential")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend(loc="upper right")

    # Save to disk
    saved_filename = os.path.join(script_dir, filename)

    plt.tight_layout()
    plt.savefig(saved_filename, bbox_inches='tight')
    plt.close()
    print(f"Plot successfully saved as '{saved_filename}'")

def run():
    """Run simulation 1."""
    print("Run simulation 1")

    x_traj, y_traj, energy_traj = run_simulation()
    plot_and_save(x_traj, y_traj)
    plot_energy(energy_traj)
