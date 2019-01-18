import matplot as m

data = m.get_data()

# # Directories
# print(len(data))
# # Files
# print(len(data[0]))
# # Categories
# print(len(data[0][0]))
# # Data
# print(len(data[0][0][0]))

zipcode_data = []
for directory in data:
	for file in directory:
		zipcode_data.append([file[3], file[4]])
m.pie(zipcode_data)


