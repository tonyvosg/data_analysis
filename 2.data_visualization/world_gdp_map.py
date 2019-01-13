import json
from appscript import *
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from countries import get_country_code
filename = 'world_gdp_json.json'
filename_output = "world_gdp.svg"
with open(filename) as f:
	world_gdp_file = json.load(f)
#print 2010 population of each country
world_gdp = {} #a dictionary to hold country_code - gdp
for data_row in world_gdp_file:
	#print(data_row)
	if(data_row['Year'] == 2000):
		country_name = data_row['Country Name']
		#print(country_name)
		country_code = get_country_code(country_name)
		#country_code = data_row['Country Code'] #standardize country code for each country
		#print(country_code)
		gdp = int(float(data_row['Value'])) 		#we need to convert string into float first after that int() function can remove decimal
		#print(gdp)
		if country_code:
			world_gdp[country_code] = gdp
			#print(country_name + " " + country_code + " " + gdp)
print(world_gdp)
style_obj = RS('#FF0000', base_style = LCS) #return an object of style
wm = World(style = style_obj)
wm.title = 'World GDP 2000 by Country'
wm.add('2000', world_gdp)
wm.render_to_file("world_gdp_map.svg")
#open pygal file with Safari
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Desktop/Portfolio/data_visualization/world_gdp_map.svg"})