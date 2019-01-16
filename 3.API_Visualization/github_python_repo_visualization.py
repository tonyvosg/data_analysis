import requests
import pygal
import requests
from appscript import *
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_json = r.json()
print(response_json)
print("Status code: ", r.status_code)
print("Total respositories: " + str(response_json['total_count']))
print("Complete result? : " + str(response_json['incomplete_results']))
#print("Repositories returned: "+str(response_json['items']))
response_items = response_json['items']
first_repo_dict = response_items[0]
for key in first_repo_dict.keys():
	print(key)
print("Selected info about first repository: ")
print("Name ", first_repo_dict['name'])
print("Owner ", first_repo_dict['owner']['login'])
print("Stars ", first_repo_dict['stargazers_count'])
print("Repository ", first_repo_dict['html_url'])
print("Created ", first_repo_dict['created_at'])
print("Updated ", first_repo_dict['updated_at'])
print("Description ", first_repo_dict['description'])
#names and stars of repositories
names, colum_data = [], []
for repo_dict in response_items:
	names.append(repo_dict['name'])
	each_column = {
		'value' : int(repo_dict['stargazers_count']),
		'label' : repo_dict['description'],
		'xlink' : repo_dict['html_url'],
	}
	colum_data.append(each_column)
print(colum_data)
#make visualization
my_style = LS('#996633', base_style = LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45,show_legend=False)
chart.title='Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('',colum_data)
chart.render_to_file('python_repos_1.svg')
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Documents/2.BuildYourProject/3.API_Visualization/python_repos_1.svg"})