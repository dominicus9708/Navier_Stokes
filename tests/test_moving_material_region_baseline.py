import os, sys, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import moving_material_region_baseline as m


class TestMovingMaterialRegionBaseline(unittest.TestCase):
    def test_all(self):
        d = m.run_all()
        self.assertEqual(d['passed'], d['total'])


if __name__ == '__main__':
    unittest.main()
