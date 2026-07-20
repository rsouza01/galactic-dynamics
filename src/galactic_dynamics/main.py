import numpy as np
from astropy import units as u
from astropy import constants as const
import galactic_dynamics.simulation_1.main as sim1
import galactic_dynamics.simulation_2.main as sim2

def main():

    print("Galactic Dynamics")
    sim1.run()
    sim2.run()


if __name__ == "__main__":
    main()