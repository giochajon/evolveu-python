import unittest
from tax_calc import tax_calc

class TesttaxCalc(unittest.TestCase):
	


	def test_taxes(self):
		self.assertEqual(tax_calc(35000), 5250)
		self.assertEqual(tax_calc(50000), 7618.5)
		self.assertEqual(tax_calc(10000), 18140.66)
		self.assertEqual(tax_calc(150000), 31211.57)

if __name__ == '__main__':
  unittest.main()