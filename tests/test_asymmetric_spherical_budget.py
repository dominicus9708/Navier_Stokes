import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import asymmetric_spherical_budget as a

class TestAsymmetricSphericalBudget(unittest.TestCase):
    def test_all(self):
        d=a.run_checks()
        self.assertEqual(d['passed'],d['total'])

if __name__=='__main__': unittest.main()
