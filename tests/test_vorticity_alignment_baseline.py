import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import vorticity_alignment_baseline as v


class TestVorticityAlignmentBaseline(unittest.TestCase):
    def test_all(self):
        d=v.run_checks()
        self.assertEqual(d["passed"],d["total"])
        self.assertTrue(all(r["status"]=="undefined/inapplicable" for r in d["undefined_samples"]))


if __name__=="__main__":
    unittest.main()
