import math as m

timesteps = 1000

G = 1
M = 1
a = 1

def phi(r: float) -> float:
    return -G*M/m.sqrt((r**2 + a**2))

def run():
    """Run simulation 1."""
    print("Run simulation 1")
    r = 10
    print(f"phi({r}) = {phi(r)}")



