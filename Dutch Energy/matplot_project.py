import os
import csv
import numpy as np
import matplotlib.pyplot as plt

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

testing = False

# Standard header is what should appear in the data and head is the formal version for graphs
std_header = ['net_manager', 'purchase_area', 'street', 'zipcode_from', 'zipcode_to', 'city', 'num_connections', 'delivery_perc', 'perc_of_active_connections', 'type_conn_perc', 'type_of_connection', 'annual_consume', 'annual_consume_lowtarif_perc', 'smartmeter_perc']

head = ['Net Manager', 'Purchase Area', 'Street', 'Zipcode From', 'Zipcode To', 'City', 'Num Connections', 'Delivery Percent', 'Percent of Active Connections', 'Type of Connection Percent', 'Type of Connection', 'Annual Consume', 'Annual Consume Lowtarif Percent', 'Smartmeter Percent']

# This turns lists of strings like Dog, Dog, Cat into Dog, Cat and 2, 1 for graphing purposes
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
			output[i] = 1
		else:
			output[i] += 1
	return list(output.keys()), list(output.values())

# This reads all the data from the csv and returns it in arrays
def get_csv(path):
	file = open(path, newline='')
	reader = csv.reader(file)
	header = next(reader)

	data = {}
	for i in std_header:
		data[i] = []

	if len(header) != len(std_header):
		print(len(header), path)

	for row in reader:
		for i, x in enumerate(row):
			data[std_header[i]].append(x)

	for i in range(len(std_header)):
		# There were a lot of swapped columns in the data that needed to be fixed
		if header[i] != std_header[i]:
			if header[i+1] == std_header[i] and std_header[i+1] == header[i]:
				data[header[i]], data[header[i+1]] = data[header[i+1]], data[header[i]]

	# This returns the data as a float if it's numerical and a string if it's categorical
	for title in std_header[6:9] + std_header[11:14]:
		for i, x in enumerate(data[title]):
			if x == '':
				data[title][i] = -1.0
			else:
				try:
					data[title][i] = float(x)
				except ValueError:
					print(title, x)
		data[title] = np.array(data[title])

	t = std_header[9]
	for i, x in enumerate(data[t]):
		# Dealing with Europeans using , instead of . to mark decimal place
		if type(x) == str:
			if ',' in x:
				new = x.split(',')
				data[t][i] = float(new[0]+'.'+new[1])
			elif x == '':
				data[t][i] = -1.0
			else:
				data[t][i] = float(x)
		elif x == None:
			data[t][i] = -1.0
	data[t] = np.array(data[t])

	for title in std_header[0:6]:
		for idx, item in enumerate(data[title]):
			if item == '':
				data[title][idx] = None

	return [data[i] for i in data]

path = 'dutch-energy/'
data = []
for directory in os.listdir(path):
	if directory[0] != '.':
		directory += '/'
		print(directory)
		data.append([])
		for i, file in enumerate(os.listdir(path+directory)):
			print(file)
			data[-1].append(get_csv(path+directory+file))
			if testing:
				break
			if input('Enter to continue...') != '':
				break

output = [[] for i in range(len(std_header))]
for directory in data:
	for file in directory:
		for index, column in enumerate(file):
			output[index].append(column)

# separated = [[] for i in range(14)]
# for i, x in enumerate(output):
# 	for j in x:
# 		separated[i] += j

# Separated is separated only by header

# Output is an list separated by:
# Header (0-13)
# File (num files)
# Data = output[header#][file#]

# data is separated by:
# directory (2)
# file (many)
# data by header (13)

# Numerical data categories
numerical = [6, 7, 8, 9, 11, 12, 13]
categorical = [0, 1, 2, 3, 4, 5, 10]
colors = 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'magenta', 'cyan', 'black', 'gray'

units = 'code of the regional network manager','code of the area where the energy is purchased','Name of the street','the range of zipcodes covered','the range of zipcodes covered', 'Name of the city','Number of connections in the range of zipcodes','Percentage of the net consumption of electricity or gas','Percentage of active connections in the zipcode range','principal type of connection in the zipcode range','percentage of presence of the principal type of connection in the zipcode range, Kwh for electricity, m3 for gas','Consumption percentage during the low tarif hours','percentage of smartmeters in the zipcode ranges'

# This is a list separated by header
separated = [[] for i in range(14)]

graphing = False

# Displaying data for all the files
for directory in data:
	for file in directory:

		# Completing the separated list
		for i, x in enumerate(file):
			separated[i].append(x)

		if graphing:
			f, axs = plt.subplots(2, 7, sharey=True)
			plt.suptitle("Numerical and Categorical Data")
			for i, x in enumerate(numerical):
				axs[0][i].hist(file[x], color=colors[i], label=head[i])
				axs[0][i].set_title(head[i])
				axs[0][i].set_xlabel(units[i], fontsize=5)
			if testing:
				plt.show()
			for i, x in enumerate(categorical):
				names, values = count(file[x])
				axs[1][i].bar(names, values)
				axs[1][i].set_title(head[i])
				axs[1][i].set_xlabel(units[i], fontsize=5)
			plt.show()
		if not testing and graphing:
			if input('Enter to continue...') != '':
				graphing = False

for i, title in enumerate(separated):
	if i in numerical:
		plt.hist([x for x in title], stacked=True, color='magenta')
	else:
		counted = np.array([count(x) for x in title])
		names, values = [], []
		for a, b in counted:
			names.append(a), values.append(b)
		plt.bar(names, values, width=0.5)
	plt.set_title(head[i])
	plt.set_xlabel(units[i])
	plt.show()




