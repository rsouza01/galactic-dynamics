import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def plot_energy(dt, energy_history, filename="./energy_vs_time.png"):

    n_steps = len(energy_history)

    # Time array corresponding to each step
    t_array = np.arange(n_steps) * dt

    plt.figure(figsize=(8, 4), dpi=150)
    plt.plot(t_array, energy_history, color='crimson', lw=1.2, label=r"$E(t) = E_{\text{kin}} + E_{\text{pot}}$")

    plt.xlabel(r"Time $t$")
    plt.ylabel(r"Specific Energy $E(t)$")
    plt.title("Total Specific Energy over Time")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Force Matplotlib to show offset scientific notation on y-axis 
    # to highlight variations at the 10^-12 level
    plt.ticklabel_format(useOffset=False, axis='y')
    plt.ylim(-0.5, 0.0)  # Set explicit physical bounds
    plt.tight_layout()

    saved_filename = os.path.join(script_dir, filename)

    plt.savefig(saved_filename, bbox_inches='tight')
    plt.close()

    print(f"Plot successfully saved as '{saved_filename}'")

def plot_relative_energy(energy_history, filename="./relative_energy.png"):
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

def plot_orbit(x, y, filename="./plummer_orbit.png"):
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

