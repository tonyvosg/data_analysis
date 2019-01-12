import pygal
import matplotlib.pyplot as plt
from dice import Dice
from appscript import *
#create two D6 dice
dice_ns1 = int(input("Number of side in dice 1: "))
dice_ns2 = int(input("Number of side in dice 2: "))
roll_num = int(input("How many times you wanna roll: "))
dice_1 = Dice(dice_ns1)
dice_2 = Dice(dice_ns2)
#make some rolls and store result in a list
results = []
for dice_num in range(roll_num):
	result = dice_1.roll()*dice_2.roll()
	results.append(result)
x_data = list(range(1,roll_num+1))
y_data = results
#plt.plot(x_data, y_data, linewidth=5)
plt.scatter(x_data, y_data, c=y_data, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()
#analyze results
frequencies = []
max_result = dice_1.num_sides*dice_2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)
#making a histogram
hist = pygal.Bar() #creating an instance of pygal.Bar()
hist.title = "Results of rolling two D6 and multiply them for " +  str(roll_num) + " times."
hist.x_title = "Result"
hist.y_title = "Frequency of results"
x_labels = []
for count in range(1,max_result+1):
	x_labels.append(str(count))
hist.x_labels = x_labels
hist.add('D6+D6', frequencies)
hist.render_to_file('two_die_visual.svg')
#open file
safari = app("Safari")
safari.make(new = k.document, with_properties={k.URL:"file:///Users/tungvo/Desktop/data_analysis/two_die_visual.svg"})
#safari.windows.first.current_tab.close()
