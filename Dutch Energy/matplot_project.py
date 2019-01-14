import os
import csv
import numpy as np
import matplotlib.pyplot as plt

std_header = ['net_manager', 'purchase_area', 'street', 'zipcode_from', 'zipcode_to', 'city', 'num_connections', 'delivery_perc', 'perc_of_active_connections', 'type_conn_perc', 'type_of_connection', 'annual_consume', 'annual_consume_lowtarif_perc', 'smartmeter_perc']

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
		if header[i] != std_header[i]:
			if header[i+1] == std_header[i] and std_header[i+1] == header[i]:
				data[header[i]], data[header[i+1]] = data[header[i+1]], data[header[i]]

	for title in std_header[6:9] + std_header[11:14]:
		for i, x in enumerate(data[title]):
			if x == '':
				data[title][i] = -1.0
			else:
				data[title][i] = float(x)
		data[title] = np.array(data[title])

	t = std_header[9]
	for i, x in enumerate(data[t]):
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

organized_data = {}
for i in std_header:
	output = [[] for i in range(len(std_header))]
	for directory in data:
		for file in directory:
			for index, column in enumerate(file):
				output[index].append(column)

	numerical = [None for i in range(len(std_header))]
	for i in [6, 7, 8, 9, 11, 12, 13]:
		output[i] = np.array(output[i])
		numerical[i] = True
	for i in [0, 1, 2, 3, 4, 5, 10]:
		numerical[i] = False

	organized_data[i] = output

# plt.hist(organized_data[std_header[6]], bins=[i for i in range(int(min(organized_data[std_header[6]])), int(max(organized_data[std_header[6]]))+1)])
# plt.show()

# Stacked bar
def stacked():
	













