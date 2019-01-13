import pygal
import os
from dice import Dice 
results = [] #list of results
num_sides = 6
dice = Dice(num_sides)
for dice_num in range(1000):
	result = dice.roll()
	results.append(result)
print(results)
#analyze frequencies
frequencies = []
for value in range(1,num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)
#making a histogram
hist = pygal.Bar() #creating an instance of pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_title = "Result"
hist.y_title = "Frequency of results"
x_labels = []
max_result = num_sides
for count in range(1,max_result+1):
	x_labels.append(str(count))
hist.x_labels = x_labels
#hist.x_labels = ['1','2','3','4','5','6']
hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
os.open("dice_visual.svg", os.O_RDWR)