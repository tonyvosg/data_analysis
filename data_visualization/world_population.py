import json
from appscript import *
from pygal.maps.world import World
from countries import get_country_code
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
#print 2010 population of each country
cc_population = {} #a dictionary to hold country_code - population
for data_row in pop_data:
	if(data_row['Year'] == '2010'):
		country_name = data_row['Country Name']
		#we need to convert string into float first
		#after that int() function can remove decimal
		country_code = get_country_code(country_name)
		population = int(float(data_row['Value']))
		if country_code:
			cc_population[country_code] = population
			print(country_code + ": "+str(population))
		else:
			print("ERROR - "+country_name)
		#print(country_name + " : " + str(population))
wm = World()
wm.title = 'World Population 2020 by Country'
wm.add('2010', cc_population)
wm.render_to_file('"world_population.svg"')
#open file
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Desktop/Portfolio/data_analysis/world_population.svg"})