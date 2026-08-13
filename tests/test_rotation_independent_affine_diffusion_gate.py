import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rotation_independent_affine_diffusion_gate import run_checks


class RotationIndependentAffineDiffusionGateTest(unittest.TestCase):
    def test_all_checks(self):
        result = run_checks()
        self.assertEqual(result["passed"], result["total"])


if __name__ == "__main__":
    unittest.main()
