import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import critical_channel_baseline as c


class TestCriticalChannelBaseline(unittest.TestCase):
    def test_all_checks(self):
        d = c.run_checks()
        self.assertEqual(d["passed"], d["total"])
        self.assertEqual(d["global_net_stretch"], "0")
        self.assertEqual(d["strain_trace"], "0")


if __name__ == "__main__":
    unittest.main()
