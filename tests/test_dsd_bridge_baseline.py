import math
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import dsd_bridge_baseline as d


class TestDSDBridgeBaseline(unittest.TestCase):
    def test_symbolic_seed(self):
        s = d.symbolic_seed_checks()
        self.assertTrue(s["divergence_zero"])
        self.assertTrue(s["omega_residual_zero"])
        self.assertTrue(s["pressure_source_residual_zero"])

    def test_axis_energy_closure(self):
        for r in (0.2, 0.5, 1.0, math.sqrt(2), 2.0):
            ex, ey, ez = d.shell_axis_energy(r)
            self.assertAlmostEqual(ex+ey+ez, d.shell_energy(r), places=12)

    def test_typed_radial_status(self):
        self.assertEqual(
            d.radial_readout_status((0.0, 0.0, 0.0))["status"],
            "undefined/inapplicable",
        )
        self.assertEqual(
            d.radial_readout_status((1.0, 0.0, 0.0))["status"],
            "defined-zero",
        )

    def test_special_shells(self):
        self.assertTrue(d.symbolic_seed_checks()["shell_energy_isotropic_at_r_sqrt2"])
        self.assertAlmostEqual(d.shell_enstrophy(math.sqrt(2.5)), 0.0, places=12)
        self.assertGreater(d.shell_energy(math.sqrt(2.5)), 0.0)

    def test_scaling(self):
        rows = d.scale_checks()
        self.assertLess(max(row["r2_energy_abs_error"] for row in rows), 1e-12)
        self.assertLess(max(row["r4_enstrophy_abs_error"] for row in rows), 1e-12)
        self.assertLess(max(row["pressure_l2_rel_error"] for row in rows), 5e-6)

    def test_collision(self):
        c = d.aggregate_collision()
        self.assertTrue(c["same_quadratic_descriptor"])
        self.assertFalse(c["signed_velocity_state_equal"])


if __name__ == "__main__":
    unittest.main()
