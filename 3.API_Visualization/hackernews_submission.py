import requests
from operator import itemgetter

#make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)
#process information about each submission
top_submission_ids = r.json()
#print(top_submission_ids)
submission_dicts = []
#process information for each submission
for submission_id in top_submission_ids:
	#make a new call for each submission
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
	submission_r = requests.get(url)
	#print(submission_r.status_code)
	response_dict = submission_r.json()
	submission = {
		'title' : response_dict['title'],
		'link' 	: 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id),
		'comments' : response_dict.get('descedants',0)
	}
	submission_dicts.append(submission)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse = True)
for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title']) 
	print("Discussion link:", submission_dict['link']) 
	print("Comments:", submission_dict['comments'])
