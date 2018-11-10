import pygame as p
import random as r
import numpy as np
import csv

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
		self.size = self.get_size()

	def get_size(self):
		size = None
		rows = [(1, 2), (3, 10), (11, 18), (19, 36), (37, 54), (55, 86), (87, 103)]
		for a, b in rows:
			if self.number in range(a, b+1):
				size = a + b - self.number
		return size
	
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
		self.elements = elements
		self.element = element

Table = PeriodicTable("elements.csv")

p.init()
win_height = 750
win_width = 1250
win = p.display.set_mode((win_width, win_height))
ball_num = 25

p.display.set_caption("Element simulation")

class Object:
	def __init__(self, direction=(0, 0), speed=5, radius=50, postion=(int(win_width/2), int(win_height/2)), color=(255, 0, 0), mass=1, element=None):
		self.x, self.y = postion
		self.radius = radius
		self.dx, self.dy = direction
		self.mass = mass
		self.speed = speed
		self.color = color
		if element != None:
			self.element = element
			self.e_init()

	def e_init(self):
		self.mass = self.element.weight
		self.radius = int(self.element.size / 2)

	def v(self):
		return np.sqrt((self.x*self.speed)**2 + (self.y*self.speed)**2)

	def draw(self):
		p.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)

	def move(self):
		self.x += self.dx * self.speed / self.mass
		self.y += self.dy * self.speed / self.mass

	def auto(self):
		self.move()
		self.collisions()

	def collisions(self):
		# with boundaries
		if self.x - self.radius <= 0:
			self.x = self.radius
			self.dx *= -1
		elif self.x + self.radius >= win_width:
			self.x = win_width - self.radius
			self.dx *= -1
		if self.y - self.radius <= 0:
			self.y = self.radius
			self.dy *= -1
		elif self.y + self.radius >= win_height:
			self.y = win_height - self.radius
			self.dy *= -1

	def __add__(self, other):
		distance = np.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
		xdiff = self.x-other.x
		ydiff = self.y-other.y
		x_force = (xdiff / distance) * other.mass
		y_force = (ydiff / distance) * other.mass
		self.dx = (self.dx+x_force)/2
		self.dy = (self.dy+y_force)/2

balls = []
for i in Table.element:
	dx = r.random()
	dy = np.sqrt(1 - dx**2)
	dx *= r.choice([-1, 1])
	dy *= r.choice([-1, 1])
	balls.append(Object(direction=(dx, dy), element=i))


# Main loop
run = True
while run:
	p.time.delay(100)
	board = np.array([np.arange(0, win_height) for i in range(win_width)])

	for event in p.event.get():
		if event.type == p.QUIT:
			run = False


	keys = p.key.get_pressed()
	[b.auto() for b in balls]

	for ball in balls:
		collided = False
		for other in balls:
			if other != ball:
				distance = np.sqrt((ball.x - other.x)**2+(ball.y - other.y)**2)
				if distance <= ball.radius + other.radius:
					ball + other
					collided = True
		if collided:
			ball.color = (255, 150, 150)
		else:
			ball.color = (255, 0, 0)

	win.fill((0, 0, 0))
	[b.draw() for b in balls]
	p.display.update()

p.quit()
