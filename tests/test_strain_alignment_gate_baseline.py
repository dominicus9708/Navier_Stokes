import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import strain_alignment_gate_baseline as s

class TestStrainAlignmentGate(unittest.TestCase):
    def test_all(self):
        d=s.run_checks()
        self.assertEqual(d['passed'],d['total'])

if __name__=='__main__': unittest.main()
