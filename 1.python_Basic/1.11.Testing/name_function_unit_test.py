import unittest
from name_function import get_formatted_name
class NameFunctionTestClass(unittest.TestCase):
	def test_first_last_name(self):
		result = get_formatted_name("tony", "vo")
		self.assertEqual(result, "Tony Vo")
	def test_first_middle_last_name(self):
		result = get_formatted_name("tony", "vo", "duy")
		self.assertEqual(result, "Tony Vo Duy")
unittest.main()