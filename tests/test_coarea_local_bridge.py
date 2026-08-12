import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import coarea_local_bridge as c


class TestCoareaLocalBridge(unittest.TestCase):
    def test_all(self):
        d=c.run_checks()
        self.assertEqual(d["passed"],d["total"])


if __name__=="__main__":
    unittest.main()
