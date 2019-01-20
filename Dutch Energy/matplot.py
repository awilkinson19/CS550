import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import printing as p
import matplotlib

'''
On my honor, I have neither given nor received unauthorized aid.

Sources:
For csv code: https://www.youtube.com/watch?v=Xi52tx6phRU&t=409s

Matplotlib helpful resources:
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
https://matplotlib.org/gallery/lines_bars_and_markers/stackplot_demo.html#sphx-glr-gallery-lines-bars-and-markers-stackplot-demo-py
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
https://stackoverflow.com/questions/46710546/matplotlib-expand-legend-vertically
'''

# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
matplotlib.rcParams.update({'font.size': 6})

# This is to check whether the headers in the csv are ordered correctly
std_header = 'net_manager', 'purchase_area', 'street', 'zipcode_from', 'zipcode_to', 'city', 'num_connections', 'delivery_perc', 'perc_of_active_connections', 'type_conn_perc', 'type_of_connection', 'annual_consume', 'annual_consume_lowtarif_perc', 'smartmeter_perc'

# Display version of above
head = 'Net Manager', 'Purchase Area', 'Street', 'Zipcode From', 'Zipcode To', 'City', 'Num Connections', 'Delivery Percent', 'Percent of Active Connections', 'Type of Connection Percent', 'Type of Connection', 'Annual Consumption', 'Lowtarif Consumption %', 'Smartmeter Percent'

# Units for the above list
units = 'code of the regional network manager','code of the area where the energy is purchased','Name of the street','the range of zipcodes covered','the range of zipcodes covered', 'Name of the city','Number of connections in the range of zipcodes','Percentage of the net consumption of electricity or gas','Percentage of active connections in the zipcode range','principal type of connection in the zipcode range','percentage of presence of the principal type of connection in the zipcode range, Kwh for electricity, m3 for gas','Consumption percentage during the low tarif hours','percentage of smartmeters in the zipcode ranges'

# Marking which columns have numerical and categorical data
numerical = [6, 7, 8, 9, 11, 12, 13]
categorical = [0, 1, 2, 3, 4, 5, 10]

if p.ask("There's a lot of data to go through, I have prepared a set that takes a moderate amount of time (20 files and 80,000 lines each, less than two minutes), but you can choose the amounts of data yourself. So, do you want to pick the amount of data to process? Note, the cities in some of the graphs are chosen because they have over 10000 data points.", boolean=True, double_check=True):
	self.maximum = 0
	self.files = 0

# Holds info for above input()
class Data:
	def __init__(self):
		self.length = 80000
		self.maximum = 80000
		self.files = 10

d = Data()

# Gets a specific column of data
def get_column(num, data, floating=False):
	if floating:
		return [np.float(i) for i in data[:, :, num].flatten()]
	return data[:, :, num].flatten()

# Counts the mentions of items in a list
def count(data):
	output = {}
	for i in data:
		# Exception case for None
		if i == None:
			if 'No Data' not in output:
				output['No Data'] = 1
			else:
				output['No Data'] += 1
			continue
		if i not in output:
			output[i] = 0
		output[i] += 1
	return list(output.keys()), list(output.values())

# Returns data
def get_csv(path):
	if d.maximum == 0:
		d.maximum = p.ask(f"\rThere are many data points ({d.length}), how many do you want to use?", option_type=int, num_range=(1, d.length), double_check=True)
	progress = False
	testing = False
	file = open(path, newline='')
	reader = csv.reader(file)
	header = next(reader)

	data = [[] for i in range(14)]

	if progress:
		print("Getting data from csv file...", end='')
	for i, row in enumerate(reader):
		for idx, x in enumerate(row):
			data[idx].append(x)
		if i+1 == d.maximum:
			break
	if testing:
		print(len(data), len(data[0]))

	# Spaces are to clear previous print statement completely
	if progress:
		print("\rHeader errors...               ", end='')
	for i in range(14):
		# There were a lot of swapped columns in the data that needed to be fixed
		if header[i] != std_header[i]:
			if header[i+1] == std_header[i] and std_header[i+1] == header[i]:
				data[i], data[i+1] = data[i+1], data[i]
	if testing:
		print(len(data), len(data[0]))

	if progress:
		print("\rComma errors...             ", end='')
	for i, x in enumerate(data[9]):
		if progress:
			print(f"\rComma errors {int(100*i/(d.length-1))}% complete...", end='')
		# Dealing with Europeans using , instead of . to mark decimal place
		if type(x) == str:
			if ',' in x:
				new = x.split(',')
				data[9][i] = new[0]+'.'+new[1]
		if i == d.maximum:
			break
	if testing:
		print(len(data), len(data[0]))

	# This returns the data as a float if it's numerical and a string if it's categorical
	for num in numerical:
		for i, x in enumerate(data[num]):
			if progress:
				print(f"\rNumerical data being returned as floats header: {num}, {int((i+1)/d.maximum)}% complete", end='')
			if x != '':
				data[num][i] = float(x)
			if i == d.maximum-1:
				break
	if testing:
		print(len(data), len(data[13]))

	if progress:
		print(f"\rCategorical data returned as strings...{' '*30}", end='')
	for num in categorical:
		for i, item in enumerate(data[num]):
			if item != '':
				data[num][i] = item
			if i == d.maximum:
				break
	if testing:
		print(len(data), len(data[0]))

	print('\r', path, '                        ')
	return [np.array(d) for d in data]

# Gets data from csv files
def get_data():
	testing = False
	path = 'dutch-energy/'
	data = [[], []]
	dir_idx = -1
	for directory in os.listdir(path):
		if directory[0] != '.':
			dir_idx += 1
			directory += '/'
			if d.files == 0:
				d.files = p.ask(f"How many files do you want out of 28?", option_type=int, num_range=(1, 30), double_check=True)

			for i, file in enumerate(os.listdir(path+directory)):
				data[dir_idx].append(get_csv(path+directory+file))
				if testing:
					print(len(data), len(data[0]), len(data[0][0]))
				if i + 1 == d.files:
					break
	if testing:
		print("data gotten")
		print(len(data), len(data[0]), len(data[1]))
	return np.array(data)

#############
#	Graphs	#
#############

# Pie chart of whether data has same zip code
# For reference: pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)
# Above from: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
def pie(data, plot):
	testing = False
	# Exact zip, same general zip, different zip
	slice = [0, 0, 0]
	names = ["Exact same zipcode", "Same area", "Different areas"]
	zip_from, zip_to = np.array(data[0]), np.array(data[1])
	if testing:
		print(zip_from.shape, zip_to.shape)

	# zips have a 4 number area code and a two letter specific code
	for i in range(len(zip_from)):
		if zip_from[i] == zip_to[i]:
			slice[0] += 1
			if testing:
				print(zip_from[i], zip_to[i])
		elif zip_from[i][0:4] == zip_to[i][0:4]:
			slice[1] += 1
			if testing:
				print(zip_from[i][0:4], zip_to[i][0:4])
		else:
			slice[2] += 1

	total = sum(slice)
	if testing:
		print(slice)
	# For autopct help: https://stackoverflow.com/questions/14171021/matplotlib-pie-chart-how-to-replace-auto-labelled-relative-values-by-absolute-v
	plot.set_title("Where is the energy received from?")
	plot.pie([i/total for i in slice], labels=names, labeldistance=1.0, pctdistance=0.5, colors=('y', 'g', 'b'), autopct=lambda p: '{:.1f}% {:.0f}'.format(p, p * total / 100))

# Prints a stacked histogram of lowtarif and total consumption
def consumption_per_city(data, plot, second=None, gas=False):
	testing = True
	city_list = get_column(5, data)
	consumption_list = get_column(11, data)
	cities = {}
	for i, city in enumerate(city_list):
		if city not in cities:
			cities[city] = [0, 0]
		cities[city][0] += 1
		cities[city][1] += float(consumption_list[i])
	cities, values = np.array(list(cities.keys())), np.array(list(cities.values()))

	# Cutting down the number of cities (there are about 1000+)
	shortlist = np.where(values[:, 0] > 10000)[0]
	cities, points, values = [cities[i] for i in shortlist], np.array([values[i][0] for i in shortlist]), np.array([values[i][1] for i in shortlist])
	width = 0.3
	plot.bar(cities, values/1000000, width, align='center', color='r')
	plot.set_xticklabels(cities, fontsize=4)

	# I need to separate labels by graph and then decided to put the data point graph in this so it would only happen once
	if gas == True:
		plot.set_title("Consumption of gas by city")
		plot.set_ylabel("Energy consumed in millions m3 of gas")
		second.set_title("Data points per city")
		second.set_ylabel("Data points")
		second.bar(cities, points, width, align='center', color='g')
		second.set_xticklabels(cities, fontsize=4)
	else:
		plot.set_title("Consumption of electricity by city")
		plot.set_ylabel("Energy consumed in millions of Kwh")

	# This should help with spacing
	plot.autoscale(tight=True)

def consumption(data, plot, gas=False):
	print("Preparing data", end='\r')
	annual = np.array(data[0])
	lowtarif = np.array(data[1])*annual/100
	bins = [i for i in range(1,int(max(annual)+100), 100)]
	print("Setting titles", end='\r')
	plot.set_title('Consumption percentages per annum in general and at lowtarif times')
	if gas:
		plot.set_xlabel('m3 of gas')
	else:
		plot.set_xlabel('Kwh')
	plot.legend([head[11], head[12]])
	plot.set_ylabel('Count')
	print("Building graph", end='\r')
	plot.hist([annual, lowtarif], bins, stacked=True)

data = np.array(get_data())

# # Directories
# print(len(data))
# # Files
# print(len(data[0]))
# # Categories
# print(len(data[0][0]))
# # Data
# print(len(data[0][0][0]))


f, axs = plt.subplots(2, 3)
a = axs[0][0]
b = axs[0][1]
c = axs[1][0]
d = axs[1][1]
e = axs[0][2]
f = axs[1][2]

print("First plot")
zipcode_data = get_column(3, data), get_column(4, data)
pie(zipcode_data, a)

print("Second and third plots")
consume = get_column(11, data, floating=True), get_column(12, data, floating=True)
consumption(consume, b)
consumption(consume, e, gas=True)

print("Fourth and fifth plots")
gas = np.array([data[0]])
electricity = np.array([data[1]])
consumption_per_city(gas, d, gas=True, second=f)
print("Sixth plot")
consumption_per_city(electricity, c)

print("Finishing")
plt.title("Graphs on Dutch Energy")
plt.tight_layout(pad=10, w_pad=10, h_pad=10)
plt.show()































