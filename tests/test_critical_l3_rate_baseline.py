import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import critical_l3_rate_baseline as c


class TestCriticalL3RateBaseline(unittest.TestCase):
    def test_full_audit(self):
        d = c.run_checks()
        self.assertEqual(d["passed"], d["total"])
        self.assertEqual(d["single_seed"]["Pi3_exact_by_symmetry"], 0.0)
        self.assertGreater(d["positive_pressure_shape"]["representative"]["Pi3"], 0.0)
        self.assertLess(d["negative_pressure_shape"]["representative"]["Pi3"], 0.0)


if __name__ == "__main__":
    unittest.main()
