import json
from countries import get_country_code
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
#print 2010 population of each country
for data_row in pop_data:
	if(data_row['Year'] == '2010'):
		country_name = data_row['Country Name']
		#we need to convert string into float first
		#after that int() function can remove decimal
		population = int(float(data_row['Value']))
		country_code = get_country_code(country_name)
		if country_code:
			print(country_code + ": "+str(population))
		else:
			print("ERROR - "+country_name)
		#print(country_name + " : " + str(population))
