import unittest
from survey import AnonymousSurvey
class AnonymousSurveyTestClass(unittest.TestCase):
	def setUp(self):
		#create tested objects once
		#use them for each of these methods
		self.my_survey = AnonymousSurvey("What do you like to speak?")
		#test data
		self.responses = ['English', 'Spanish', 'Mandarin']
	def test_single_response(self):		
		self.my_survey.store_response(self.responses[1])
		self.assertIn(self.responses[1], self.my_survey.responses)
	def test_multiple_responses(self): 
		#store each response
		for response in self.responses:
			self.my_survey.store_response(response)
		#testing for each response
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
unittest.main()