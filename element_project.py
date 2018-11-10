import pygame as p
p.init()
p.font.init()
import random as r
import numpy as np
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

class Variables:
	def __init__(self):
		self.win_height = 750
		self.win_width = 1250
		self.win = None
		self.yellow = (255, 255, 0)
		self.red = (255, 0, 0)
		self.blue = (0, 0, 255)
		self.green = (0, 255, 0)
		self.purple = (255, 0, 255)
		self.orange = (255, 128, 0)
		self.turquoise = (0, 255, 255)
var = Variables()

class Element:
	def __init__(self, var, quantity=1):
		self.name = var[0]
		self.number = int(var[1])
		self.symbol = var[2]
		self.weight = self.assign(var[3])
		self.boil = self.assign(var[4])
		self.melt = self.assign(var[5])
		self.density_vapor = self.assign(var[6])
		self.fusion = self.assign(var[7])
		self.quantity = quantity
		self.size = self.get_size()
		self.color = self.get_color()

	def get_size(self):
		ranges = [(1, 2), (3, 10), (11, 18), (19, 36), (37, 54), (55, 86), (87, 103)]
		for a, b in ranges:
			if self.number in range(a, b+1):
				return int(a + b - self.number)

	def get_color(self):
		ranges = [(1, 2), (3, 10), (11, 18), (19, 36), (37, 54), (55, 86), (87, 103)]
		for idx, (a, b) in enumerate(ranges):
			if self.number in range(a, b+1):
				if self.number == b:
					return var.blue
				elif idx > 0 and self.number == a:
					return var.yellow
				elif idx > 0 and self.number == a+1:
					return var.green
				elif 2 < idx < 5 and self.number < a + 10:
					return var.turquoise
				elif 4 < idx and self.number < a + 16:
					return var.purple
				elif 0 < idx and self.number > b - (6-idx):
					return var.orange
				else:
					return var.red
	
	def set_name(string):
	  self.name = string
	
	def get_name():
	  return self.name
	
	def set_number(flt):
	  self.number = flt
	  
	def get_number():
	  return self.number
	
	def set_symbol(string):
	  self.symbol = string
	
	def get_symbol():
	  return self.symbol
	
	def set_weight(flt):
	  self.weight = flt
	
	def get_weight():
	  return self.weight
	
	def set_boil(flt):
	  self.boil = flt
	
	def get_boil():
	  return self.boil

	def set_melt(flt):
		self.melt = flt
	
	def get_melt():
		return self.melt

	def set_density_vapor(flt):
		self.density_vapor = flt

	def get_density_vapor():
		return self.density_vapor
	
	def set_fusion(flt):
	  self.name = flt
	
	def get_fusion():
	  return self.fusion
	
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
		self.weight = self.get_weight()
	
	def get_weight(self):
		weight = 0
		for i in self.elements:
			weight += self.weight
		return weight

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
		data_path = open(csv_path)
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
		self.element_dict = elements
		self.element_list = element

Table = PeriodicTable("elements.csv")

class Object:
	def __init__(self, direction=(0, 0), speed=7, radius=50, postion=(int(var.win_width/2), int(var.win_height/2)), color=(255, 0, 0), mass=1, element=None):
		self.x, self.y = postion
		self.radius = radius
		self.dx, self.dy = direction
		self.mass = mass
		self.speed = speed
		self.color = color
		if element != None:
			self.element = element
			self.e_init()
			self.font_size = int(self.element.size/2)
		self.font = p.font.SysFont('Arial', self.font_size)
		self.text = self.font.render(self.make_text(), False, (0, 0, 0))

	def e_init(self):
		self.mass = self.element.weight
		self.radius = int((self.element.size + 20) / 4)
		self.color = self.element.color

	def make_text(self):
		return str(self.element)

	def v(self):
		return np.sqrt((self.x*self.speed)**2 + (self.y*self.speed)**2)

	def draw(self):
		p.draw.circle(var.win, self.color, (int(self.x), int(self.y)), self.radius)
		var.win.blit(self.text, (self.x, self.y))


	def move(self):
		self.x += self.dx * self.speed / self.mass
		self.y += self.dy * self.speed / self.mass

	def auto(self):
		self.move()
		self.collisions()

	def collisions(self):
		# bounces against boundaries
		if self.x - self.radius <= 0:
			self.x = self.radius
			self.dx *= -1
		elif self.x + self.radius >= var.win_width:
			self.x = var.win_width - self.radius
			self.dx *= -1
		if self.y - self.radius <= 0:
			self.y = self.radius
			self.dy *= -1
		elif self.y + self.radius >= var.win_height:
			self.y = var.win_height - self.radius
			self.dy *= -1

	def __add__(self, other):
		distance = np.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
		if distance == 0:
			other.x -= other.dx / other.mass
			other.y -= other.dy / other.mass
			distance = np.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
			assert distance > 0
		xdiff = self.x-other.x
		ydiff = self.y-other.y
		x_force = (xdiff / distance) * other.mass * 2
		y_force = (ydiff / distance) * other.mass * 2
		self.dx = (self.dx+x_force)/2
		self.dy = (self.dy+y_force)/2


def run_game(elements):
	atoms = []
	for i in elements:
		dx = r.random()
		dy = np.sqrt(1 - dx**2)
		dx *= r.choice([-1, 1])
		dy *= r.choice([-1, 1])
		atoms.append(Object(direction=(dx, dy), element=i))
	# Game program
	game_font = p.font.SysFont('Calibri', 12)
	text = game_font.render('Simulation', False, (255, 255, 255))
	var.win = p.display.set_mode((var.win_width, var.win_height))

	p.display.set_caption("Element simulation")
	# Main loop
	run = True
	while run:
		p.time.delay(25)
		board = np.array([np.arange(0, var.win_height) for i in range(var.win_width)])

		for event in p.event.get():
			if event.type == p.QUIT:
				run = False

		keys = p.key.get_pressed()
		# put autopilot on for all atoms
		[a.auto() for a in atoms]

		for atom in atoms:
			for other in atoms:
				if other != atom:
					distance = np.sqrt((atom.x - other.x)**2+(atom.y - other.y)**2)
					if distance <= atom.radius + other.radius:
						atom + other

		keys = p.key.get_pressed()
		if keys[p.K_SPACE]:
			p.time.delay(100)
		var.win.fill((255, 255, 255))
		[a.draw() for a in reversed(atoms)]
		p.display.update()

	p.quit()

run_game(Table.element_list)

