import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1,4,9,16,25]
plt.plot(x_data, y_data, linewidth=5)
#set the chart title and label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()