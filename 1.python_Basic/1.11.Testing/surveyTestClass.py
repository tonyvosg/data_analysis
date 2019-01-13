import unittest
from survey import AnonymousSurvey
class AnonymousSurveyTestClass(unittest.TestCase):
	def test_single_response(self):
		survey = AnonymousSurvey("What do you like to speak?")
		survey.store_response("English")
		self.assertIn('English', survey.responses)
	def test_multiple_responses(self):
		survey = AnonymousSurvey("What do you like to speak?")
		responses =  ['English', 'Spanish', 'Mandarin']
		#store each response
		for response in responses:
			survey.store_response(response)
		#testing for each response
		for response in responses:
			self.assertIn(response, survey.responses)
unittest.main()