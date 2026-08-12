import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import stretching_coupling_baseline as s


class TestStretchingCouplingBaseline(unittest.TestCase):
    def test_all(self):
        d=s.run_checks()
        self.assertEqual(d["passed"],d["total"])
        self.assertLess(d["numeric_values"]["self_sum"],0.0)
        self.assertGreater(d["numeric_values"]["sigma_total"],0.0)


if __name__=="__main__":
    unittest.main()
