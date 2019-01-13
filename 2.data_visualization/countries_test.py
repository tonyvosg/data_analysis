import unittest
from countries import get_country_code
class get_country_code_test_class(unittest.TestCase):
	def testSetup(self):
		self.test_data = 'Vietnam'
	def gccTestFunction(self):
		result = get_country_code(test_data)
		self.assertEqual("vn", result)
unittest.main()