#use APIs to write self-contained pro- grams that automatically gather the data they need 
#and use that data to create a visualization
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_json = r.json()
print(response_json)
print("Status code: ", r.status_code)
print("Total respositories: " + str(response_json['total_count']))
print("Complete result? : " + str(response_json['incomplete_results']))
#print("Repositories returned: "+str(response_json['items']))
response_items = response_json['items']
first_repo = response_items[0]
for key in first_repo.keys():
	print(key)
print("Selected info about first repository: ")
print("Name ", first_repo['name'])
print("Owner ", first_repo['owner']['login'])
print("Stars ", first_repo['stargazers_count'])
print("Repository ", first_repo['html_url'])
print("Created ", first_repo['created_at'])
print("Updated ", first_repo['updated_at'])
print("Description ", first_repo['description'])