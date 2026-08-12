import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import vorticity_direction_gradient_baseline as v

class TestDirectionGradient(unittest.TestCase):
    def test_all(self):
        d=v.run_checks()
        self.assertEqual(d['passed'],d['total'])

if __name__=='__main__': unittest.main()
