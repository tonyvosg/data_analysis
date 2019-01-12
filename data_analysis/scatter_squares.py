from matplotlib import pyplot as plt
x_values = list(range(1,1000,100))
y_values = [x*2 for x in x_values]
#plt.plot(x_values, y_values, c='red', edgecolor='yellow', s=40)
#plt.plot(x_values, y_values, c=(0,0,0.8), edgecolor='yellow', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.axis([0,1100,0,10000])
plt.savefig("squaresPlot.png", bbox_inches = "tight")
plt.show()