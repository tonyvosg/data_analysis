import json
from appscript import *
from pygal.maps.world import World
from countries import get_country_code
filename = 'population_data.json'
filename_output = "three_basket_world_population"
with open(filename) as f:
	pop_data = json.load(f)
#print 2010 population of each country
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {} #a dictionary to hold country_code - population
for data_row in pop_data:
	if(data_row['Year'] == '2010'):
		country_name = data_row['Country Name']
		country_code = get_country_code(country_name) #standardize country code for each country
		population = int(float(data_row['Value'])) 		#we need to convert string into float first after that int() function can remove decimal
		if country_code:
			if population < 10000000:
				cc_pop1[country_code] = population
			elif population < 1000000000:
				cc_pop2[country_code] = population
			else:
				cc_pop3[country_code] = population
			print(country_code + ": "+str(population))
		else:
			print("ERROR - No Country Code Found "+ country_name)
		#print(country_name + " : " + str(population))
wm = World()
wm.title = 'World Population 2020 by Country'
wm.add('0-10m', cc_pop1, c="blue")
wm.add('10m-1b', cc_pop2, c="yellow")
wm.add('>1b', cc_pop3, c="red")
wm.render_to_file("three_basket_world_population.svg")
#open pygal file with Safari
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Desktop/Portfolio/data_analysis/three_basket_world_population.svg"})