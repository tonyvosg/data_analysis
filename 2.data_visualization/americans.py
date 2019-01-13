from pygal.maps.world import World
#create an instance of world map class
wm = World()
#set title for the map
wm.title = 'North, Central and South Americal'
#set up new color and add new color to the left
wm.add('North America', {'ca':34126000,'mx':113423000,'us':309349000})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
	'gy', 'pe', 'py', 'sr', 'uy', 've'])
#render to a file
wm.render_to_file('americas.svg')