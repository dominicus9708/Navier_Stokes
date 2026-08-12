import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import spherical_energy_budget as s

class TestSphericalEnergyBudget(unittest.TestCase):
    def test_all(self):
        d=s.run_checks()
        self.assertEqual(d['passed'],d['total'])

if __name__=='__main__': unittest.main()
