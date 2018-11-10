import csv
'''
Sources:
help on __add__() method
http://www.marinamele.com/2014/04/modifying-add-method-of-python-class.html
__iter__() help:
https://docs.python.org/3/tutorial/classes.html#method-objects
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

def print_vals():
  print(data_header)
  for i in range(0, len(data)):
    print(data[i])

class Element:
	def __init__(self, var, quantity=1):
		self.name = var[0]
		self.number = int(var[1])
		self.symbol = var[2]
		self.weight = self.assign(var[3])
		self.boil = self.assign(var[4])
		self.melt = self.assign(var[5])
		self.density_vapour = self.assign(var[6])
		self.fusion = self.assign(var[7])
		self.quantity = quantity
	
  def assign(self, var):
  	if var == '':
  		return None
  	else:
  		return float(var)

	def __str__(self):
		if self.quantity > 1:
			return str(self.quantity)+self.symbol
		else:
			return self.symbol

	def __add__(self, other):
		return Molecule([self, other])

	def __mul__(self, num):
		self.quantity *= num
		return self

class Molecule:
	def __init__(self, elements, quantity=1):
		self.index = 0
		self.elements = elements
		self.itemized = self.itemize()
		self.quantity = quantity

	def itemize(self):
		return [str(i) for i in self.elements]

	def __iter__(self):
		self.index = -1
		return self

	def __next__(self):
		if self.index == len(self.itemized)-1:
			raise StopIteration
		self.index += 1
		return self.itemized[self.index]

	def __str__(self):
		r = ''
		if self.quantity != 1:
			r += str(self.quantity)
		for i in self.elements:
			r += i.symbol
			if i.quantity != 1:
				r += str(i.quantity)
		return r

	def __mul__(self, num):
		self.quantity *= num
		return self

	def __add__(self, other):
		elements = self.elements+other.elements
		return Molecule(elements)

class PeriodicTable:
	def __init__(self, csv_path):
	  # Get Data
    data_path = open("elements.csv")
    data_reader = csv.reader(data_path)
    data_header = next(data_reader)
    data = [row for row in data_reader]
    for i in data:
	    while len(i) < len(data_header):
		  i.append('')
    element = [Element(row) for row in data]
    elements = {}
    for i in element:
	    elements[str(i)] = i
	  self.elements = elements

water = Molecule([elements['H']*2, elements['O']])
print([i for i in water])
print(water*3)

def userloop():
  class Temporary:
    def __init__(self,coeff,atom,number):
      self.coeff = coeff
      self.atom = atom
      self.number = number
  #clear()
  print("Please enter a molecular formula. (Eg. H2O for water)")
  userget = input('>>> ')
  for i in range(userget):
    # Method from StackOverflow - https://stackoverflow.com/questions/15558392/how-to-check-if-character-in-string-is-a-letter-python
    # Check for a coefficient (number in front of capital)
    if userget[i].isdigit() == 1:
    	if userget[i+1].isupper() == 1:
    	  if i == 0:
    	    tempcoeff = userget[i]
        elif userget[i-1] == "+":
          tempcoeff = userget[i]
        else:
          tempcoeff = 1
          tempnumber = 1
    # Check for an element (capital letter)
    if userget[i].isupper() == 1:
      try:
        if userget[i+1].islower() == 1:
          print(userget[i] + userget[i+1] + " is an element!")
          tempatom = userget[i] + userget[i+1]
        else:
          print(userget[i] + " is an element!")
          tempatom = userget[i]
    if userget[i].isdigit() == 1:
      print(userget[i] + " is a quantity!")
    if "(" in userget[i]:
      print("Charge:")
      print(userget[userget.find("(")+1 : userget.find(")")])
      break
  print(tempcoeff)
  print(tempatom)
  print(tempnumber)
  userloop()
