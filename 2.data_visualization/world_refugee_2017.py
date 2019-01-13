import csv
from appscript import *
from countries import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
filename = 'world_refugee.csv'
#open a file
year = input("What year you wanna see? ")
with open(filename) as f:
	reader = csv.reader(f)
	for i in range(0,5):
		header_row = next(reader)
	index = header_row.index(year)
	#next function read the next row
	refugee_dict = {}
	for row in reader:
		country_name = row[0]
		country_code = get_country_code(country_name)
		if country_code:
			country_refugee = row[index]
			if(country_refugee):
				refugee_dict[country_code] = int(country_refugee)
			else:
				refugee_dict[country_code] = 0
	print(refugee_dict)
#print the map
style_obj = RS('#FF0000', base_style = LCS) #return an object of style
wm = World(style = style_obj)
wm.title = "Refugee population of" + year + "by Country"
wm.add(year, refugee_dict)
wm.render_to_file("world_refugee_map.svg")
#open pygal file with Safari
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Desktop/Portfolio/data_visualization/world_refugee_map.svg"})