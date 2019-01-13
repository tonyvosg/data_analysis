from survey import AnonymousSurvey
question = "What language do you wanna learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' to quit")
while True:
	response = input("Languages: ")
	if response == 'q':
		break
	my_survey.store_response(response)
print("Thanh you for your response")
my_survey.show_results()