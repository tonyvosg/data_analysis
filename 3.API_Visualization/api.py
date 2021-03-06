#use APIs to write self-contained pro- grams that automatically gather the data they need 
#and use that data to create a visualization
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
#status code is 200 if the call is successful
print("Status code: ", r.status_code)
#store api response into a dictionay
response_dict = r.json()
print(response_dict['total_count'])
print(response_dict['incomplete_results'])
print(response_dict.keys())