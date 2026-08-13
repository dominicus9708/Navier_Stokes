import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from deformation_factorization_ledger_gate import run_checks


class DeformationFactorizationLedgerTest(unittest.TestCase):
    def test_all_ledger_checks(self):
        result = run_checks(samples=40)
        self.assertEqual(result["passed"], result["total"])


if __name__ == "__main__":
    unittest.main()
