import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import lagrangian_metric_cancellation_gate as m


class TestLagrangianMetricCancellationGate(unittest.TestCase):
    def test_all(self):
        d = m.run_checks()
        self.assertEqual(d['passed'], d['total'])


if __name__ == '__main__':
    unittest.main()
