import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import translation_coupling_baseline as t


class TestTranslationCoupling(unittest.TestCase):
    def test_all(self):
        d = t.run_checks()
        self.assertEqual(d["passed"], d["total"])
        self.assertEqual(d["superposition"]["div_total"], "0")
        self.assertNotEqual(d["superposition"]["cross_Q_at_test_point"], 0.0)


if __name__ == "__main__":
    unittest.main()
