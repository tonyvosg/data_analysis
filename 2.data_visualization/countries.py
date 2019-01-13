from pygal.maps.world import COUNTRIES
def get_country_code(country_name): 
	for code, name in COUNTRIES.items():
		if name == country_name:
			#print(code)
			return code
	return None
get_country_code('Andorra')
get_country_code('United Arab Emirates')
get_country_code('Afghanistan')