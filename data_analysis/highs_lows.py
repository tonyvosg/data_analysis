import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'death_valley_2014.csv'
#open a file
with open(filename) as f:
	reader = csv.reader(f)
	#next function read the next row
	header_row = next(reader)
	print(header_row)
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	dates, highs, lows = [], [], []
	#iterate each row
	for row in reader:
		try:
			date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1]) #for each row, the high temperature is in index 1 (second position)
			low = int(row[2])
		except:
			print(str(date) + "misising data")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)
	f.close()
#plot data
figure = plt.figure(dpi=128, figsize=(10,6))
#the alpha argument is the opaqueness of the line
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
#facecolor is the color of shaded/ fill-between region
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#formate figure
plt.title("Daily high and low temperature of Death Valley CA, 2014", fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature (F) ", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
figure.autofmt_xdate()
plt.show()