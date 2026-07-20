import math
import unittest

from galactic_dynamics.simulation_1.main import phi


class TestPhiFunction(unittest.TestCase):
    def test_phi_at_positive_radius(self):
        self.assertAlmostEqual(phi(1.0), -1.0 / math.sqrt(2.0), places=12)

    def test_phi_at_zero_radius(self):
        self.assertAlmostEqual(phi(0.0), -1.0 / 1.0, places=12)

    def test_phi_is_negative_for_all_radii(self):
        for r in [0.1, 1.0, 10.0, 100.0]:
            with self.subTest(r=r):
                self.assertLess(phi(r), 0.0)

    def test_phi_decreases_in_magnitude_with_radius(self):
        self.assertLess(phi(0.5), phi(1.0))
        self.assertLess(phi(1.0), phi(2.0))


if __name__ == "__main__":
    unittest.main()
