import matplotlib.pyplot as plt
from RandomWalk_Modified import RandomWalk
while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor='none', s = 5)
	#emphasize the first and last points
	plt.scatter(0,0,c='green', edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolor='none',s=100)
	#remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	#show the plot
	plt.show()
	#set the size of the plotting window
	plt.figure(dpi=128, figsize=(20,12))
	#save figure
	plt.savefig("random_walk_plot.png", bbox_inches = "tight")
	#ask users whether we should keep it running
	keep_running = input('Make another walk? (y/n): ')
	if(keep_running == 'n'):
		break