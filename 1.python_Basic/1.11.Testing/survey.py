class AnonymousSurvey():
	def __init__(self,question):
		self.question = question
		self.responses = []
	def show_question(self):
		return self.question
	def store_response(self, new_response):
		self.responses.append(new_response)
	def show_results(self):
		print("Survey result: ")
		for response in self.responses:
			print('- '+response)