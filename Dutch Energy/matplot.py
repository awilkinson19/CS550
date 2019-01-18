import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import printing as p

std_header = 'net_manager', 'purchase_area', 'street', 'zipcode_from', 'zipcode_to', 'city', 'num_connections', 'delivery_perc', 'perc_of_active_connections', 'type_conn_perc', 'type_of_connection', 'annual_consume', 'annual_consume_lowtarif_perc', 'smartmeter_perc'

head = 'Net Manager', 'Purchase Area', 'Street', 'Zipcode From', 'Zipcode To', 'City', 'Num Connections', 'Delivery Percent', 'Percent of Active Connections', 'Type of Connection Percent', 'Type of Connection', 'Annual Consume', 'Annual Consume Lowtarif Percent', 'Smartmeter Percent'

units = 'code of the regional network manager','code of the area where the energy is purchased','Name of the street','the range of zipcodes covered','the range of zipcodes covered', 'Name of the city','Number of connections in the range of zipcodes','Percentage of the net consumption of electricity or gas','Percentage of active connections in the zipcode range','principal type of connection in the zipcode range','percentage of presence of the principal type of connection in the zipcode range, Kwh for electricity, m3 for gas','Consumption percentage during the low tarif hours','percentage of smartmeters in the zipcode ranges'

numerical = [6, 7, 8, 9, 11, 12, 13]
categorical = [0, 1, 2, 3, 4, 5, 10]

class Data:
	def __init__(self):
		self.length = 0
		self.maximum = 0
		self.files = 0

d = Data()

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

def get_csv(path):
	file = open(path, newline='')
	reader = csv.reader(file)
	header = next(reader)

	data = [[] for i in range(14)]

	print("Getting data from csv file...", end='')
	for row in reader:
		for i, x in enumerate(row):
			data[i].append(x)

	d.length = len(data[0])
	if d.maximum == 0:
		d.maximum = p.ask(f"\rThere are many data points ({d.length}), how many do you want to use?", option_type=int, num_range=(1, d.length), double_check=True)

	# Spaces are to clear previous print statement completely
	print("\rHeader errors...               ", end='')
	for i in range(14):
		# There were a lot of swapped columns in the data that needed to be fixed
		if header[i] != std_header[i]:
			if header[i+1] == std_header[i] and std_header[i+1] == header[i]:
				data[i], data[i+1] = data[i+1], data[i]

	print("\rComma errors...             ", end='')
	for i, x in enumerate(data[9]):
		print(f"\rComma errors {int(100*i/(d.length-1))}% complete...", end='')
		# Dealing with Europeans using , instead of . to mark decimal place
		if type(x) == str:
			if ',' in x:
				new = x.split(',')
				data[9][i] = new[0]+'.'+new[1]
		if i == d.maximum:
			break

	# This returns the data as a float if it's numerical and a string if it's categorical
	for num in numerical:
		for i, x in enumerate(data[num]):
			print(f"\rNumerical data being returned as floats header: {num}, {int((i+1)/d.maximum)}% complete", end='')
			if x != '':
				data[num].append(float(x))
			if i == d.maximum-1:
				break

	print(f"\rCategorical data returned as strings...{' '*30}", end='')
	for num in categorical:
		for i, item in enumerate(data[num]):
			if item != '':
				data.append(item)
			if i == d.maximum:
				break

	print('\r', path, '                        ')
	return [np.array(i) for i in data]

def get_data():
	path = 'dutch-energy/'
	data = [[], []]
	for dir_idx, directory in enumerate(os.listdir(path)):
		if directory[0] != '.':
			directory += '/'
			if d.files == 0:
				d.files = p.ask(f"How many files do you want out of 28?", option_type=int, num_range=(1, 30), double_check=True)
			for i, file in enumerate(os.listdir(path+directory)):
				data[dir_idx - 1].append(get_csv(path+directory+file))
				if i + 1 == d.files:
					break
	print("data gotten")
	return data

#############
#	Graphs	#
#############

# Pie chart of whether data has same zip code
# For reference: pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)
# Above from: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html
def pie(data):
	# Exact zip, same general zip, different zip
	slice = [0, 0, 0]
	names = ["Exact zipcode", "Same area code", "Different zip codes"]
	zip_from, zip_to = data
	for directory in range(len(zip_from)):
		for file in range(len(zip_from[0])):
			for i in range(len(zip_from[directory][file])):
				if zip_from[directory][file][i] == zip_to[directory][file][i]:
					slice[0] += 1
				elif zip_from[directory][file][i][0:5] == zip_to[directory][file][i][0:5]:
					slice[1] += 1
				else:
					slice[2] += 1

	total = slice[0]+slice[1]+slice[2]
	plt.pie([i/total for i in slice], labels=names, colors=('y', 'g', 'b'), autopct='%1.1f%%')
	plt.show()

































