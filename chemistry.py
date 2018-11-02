import csv
'''
Sources:
help on __add__() method
http://www.marinamele.com/2014/04/modifying-add-method-of-python-class.html
'''

# Clears screen depending on OS
def clear(): 
	# for windows 
	if name == 'nt':
		_ = system('cls') 
	# for mac and linux(here, os.name is 'posix') 	else: 
		_ = system('clear')
	header()

# Pauses excecution until user inputs key
def pause():
	input("Press ENTER to continue...")

# Get Data
data_path = open("elements.csv")
data_reader = csv.reader(data_path)data_header = next(data_reader)
data = [row for row in data_reader]

def print_vals():
	print(data_header)
	for i in range(0, len(data)):
		print(data[i])

for i in data:
	while len(i) < len(data_header):
		i.append('')

def assign(var):
	if var == '':
		return None
	else:
		return float(var)

class Element:
	
	def __init__(self, var, quantity=1):
		self.name = var[0]
		self.number = int(var[1])
		self.symbol = var[2]
		self.weight = assign(var[3])
		self.boil = assign(var[4])
		self.melt = assign(var[5])
		self.density_vapour = assign(var[6])
		self.fusion = assign(var[7])
    self.quantity = quantity
    
  def __str__(self):
    return self.symbol+str(self.quantity)

	def __add__(self, other):
    return str(self)+str(other)

P = Element(data[14])
print(data[14])

def parse():
	pass

def userloop():
  print("Please enter a molecular formula. (Eg. )")
