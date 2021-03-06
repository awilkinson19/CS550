import pygame as p
import random as r
import numpy as np
import re
import csv

'''
Description:
There are three main classes. The Periodic Table class turns the rows of the csv file into an Element class. The element class has many built in functions, like multiplication and addition. The Molecule class returns an object very similar to an element, except it returns values for the entire molecule, like the total weight. The Variables class is meant to be a repository for variables I can use across classes and functions, just because I don't like the global statement. The main thing we added was a pygame simulation of how various atoms would interact. This is done by using the run_game function and the Object class, which creates a circle with attributes like velocity, radius, color, and what to display on it.

All of the above is made available to the user through the userloop function, which parses input into the parts of the input (so the parts of H + H would be the molecule/element, the operation, and the second molecule/element) and elements of a molecule (so H2O would become [H2, O]). The user can also call functions like simulate, set variable, etc.


Sources:
help on __add__ method
http://www.marinamele.com/2014/04/modifying-add-method-of-python-class.html
__iter__ help:
https://docs.python.org/3/tutorial/classes.html#method-objects
pygame help from:
https://www.youtube.com/watch?v=i6xMBig-pP4 and the next few episodes in the series


Honor Code:
On my honor, I have neither given nor received unauthorized aid.
Alex Wilkinson
Daniel Heredia
'''

# Stores variables I need later on
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

# Creates an Element class to store all the data from the csv files
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

  # Setters and Getters
  def get_size(self):
    # In the periodic table, size goes (from small to large) top to bottom, then right to left
    ranges = [(1, 2), (3, 10), (11, 18), (19, 36), (37, 54), (55, 86), (87, 103)]
    for a, b in ranges:
      if self.number in range(a, b+1):
        return int(a + b - self.number)

  def get_color(self):
    # The color coding is for use with pygame and it replicates color coding on the periodic table
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
  
  def set_name(self, string):
    self.name = string
  
  def get_name(self):
    return self.name
  
  def set_number(self,flt):
    self.number = flt
    
  def get_number(self):
    return self.number
  
  def set_symbol(self,string):
    self.symbol = string
  
  def get_symbol(self):
    return self.symbol
  
  def set_weight(self,flt):
    self.weight = flt
  
  def get_weight(self):
    return self.weight
  
  def set_boil(self,flt):
    self.boil = flt
  
  def get_boil(self):
    return self.boil

  def set_melt(self,flt):
    self.melt = flt
  
  def get_melt(self):
    return self.melt

  def set_density_vapor(self,flt):
    self.density_vapor = flt

  def get_density_vapor(self):
    return self.density_vapor
  
  def set_fusion(self,flt):
    self.name = flt
  
  def get_fusion(self):
    return self.fusion
  
  def assign(self, var):
      if var == '':
        return None
      else:
        return float(var)

  # Built-ins
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

# Molecule class, it's useful for linking multiple elements and for finding things like their combined weight
class Molecule:
  def __init__(self, elements, quantity):
    self.index = 0
    self.elements = [(i[0], int(i[1])) for i in elements]
    self.quantity = int(quantity)
    self.weight = self.get_weight()
  
  def get_weight(self):
    weight = 0
    for element, quantity in self.elements:
      weight += element.weight * quantity
    return weight*self.quantity

  # Iteration returns each element in the list, but not the quantity
  def __iter__(self):
    self.index = -1
    return self

  def __next__(self):
    if self.index == len(self.elements)-1:
      raise StopIteration
    self.index += 1
    return self.elements[self.index][0]

  def __str__(self):
    r = ''
    if self.quantity != 1:
      r += str(self.quantity)
    for i, quantity in self.elements:
      r += i.symbol
      if quantity != 1:
        r += str(quantity)
    return r

  # Other Built-ins
  def __mul__(self, num):
    self.quantity *= num
    return self

  def __add__(self, other):
    elements = self.elements+other.elements
    return Molecule(elements)

# Periodic table class
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
    self.list = [Element(row) for row in data]
    self.dict = {}
    for i in self.list:
      self.dict[str(i)] = i
    
    # Started using element_dict and element_list, but they were cumbersome so I switched to dict and list
    # These are left in because of code already written with element_dict and element_list
    self.element_dict = self.dict
    self.element_list = self.list
    self.index = -1
  
  # Iteration returns each element in the table
  def __iter__(self):
    self.index = -1
    return self
  def __next__(self):
    self.index += 1
    if self.index == len(self.list):
      raise StopIteration
    return self.list[self.index]

Table = PeriodicTable("elements.csv")

# This is a class for a ball in the pygame simulation, meant to represent 1 atom
class Object:
  def __init__(self, direction=(0, 0), speed=1, radius=50, postion=(int(var.win_width/2), int(var.win_height/2)), color=(255, 0, 0), mass=1, element=None):
    self.x, self.y = postion
    self.radius = radius
    # dx and dy are the change in x and y between frames
    self.dx, self.dy = direction
    # I didn't want the masses to be too different for the simulation, especially because the sizes are being scaled down
    self.mass = int(np.log(mass))
    self.speed = speed
    self.color = color
    if element != None:
      self.element = element
      self.e_init()
      self.font_size = int(self.radius)
    self.font = p.font.SysFont('Arial', self.font_size)
    self.text = self.font.render(self.make_text(), False, (0, 0, 0))

  def e_init(self):
    self.mass = self.element.weight
    # Size is scaled so you can actually see H
    self.radius = int(np.log(self.element.size) * 30)
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

  # This is the collision function, I just liked that I could use a built-in for collisions
  def __add__(self, other):
    distance = np.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
    # If the distance is 0, push the objects away from eachother
    if distance == 0:
      other.x -= other.dx / other.mass
      other.y -= other.dy / other.mass
      distance = np.sqrt((self.x - other.x)**2+(self.y - other.y)**2)
    # These are to show the direction of the hit
    xdiff = self.x-other.x
    ydiff = self.y-other.y
    # I didn't use actual physics, this was guessing what felt right to have as the new forces
    x_force = (xdiff / distance) * other.mass/self.mass * 2
    y_force = (ydiff / distance) * other.mass/self.mass * 2
    # Average new force with previous trajectory
    self.dx = (self.dx+x_force)/2
    self.dy = (self.dy+y_force)/2

# Runs pygame simulation
def run_game(elements):
  p.init()
  p.font.init()
  # Give each atom a random initial trajectory
  atoms = []
  for i in elements:
    # Pick sin
    dx = r.random()
    # Calculate corresponding cos
    dy = np.sqrt(1 - dx**2)
    # Pick directions
    dx *= r.choice([-1, 1])
    dy *= r.choice([-1, 1])
    # Add to Object class
    atoms.append(Object(direction=(dx, dy), element=i))
  # Game program
  small_font = p.font.SysFont('Calibri', 24)
  big_font = p.font.SysFont('Calibri', 72)
  small_text = small_font.render('[SPACE] slows the simulation. [ENTER] ends the simulation.', False, (0, 0, 0))
  big_text = big_font.render('Simulation Ended. Return to the Terminal.', False, (0, 0, 0))
  var.win = p.display.set_mode((var.win_width, var.win_height))

  p.display.set_caption("Element Simulation")
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
            # If two points are closer than the sum of their radii to eachother, then they collide
            atom + other

    # Slow simulation
    keys = p.key.get_pressed()
    if keys[p.K_SPACE]:
      p.time.delay(100)
    # End simulation
    if keys[p.K_ESCAPE] or keys[p.K_RETURN]:
      run = False
    # Add background color
    var.win.fill((255, 255, 255))
    # Add corner text
    var.win.blit(small_text, (0, 0))
    # Draw atoms
    [a.draw() for a in reversed(atoms)]
    # Update display
    p.display.update()

  # End of sim text
  textpos = big_text.get_rect()
  textpos.centerx = var.win.get_rect().centerx
  textpos.centery = 50
  var.win.blit(big_text, textpos)
  p.display.update()
  p.quit()

class Terminal:
  def __init__(self):
    pass
  
  # Introductory statement
  def userhelp(self):
    print("Possible functions:\ninfo (molecule) [summation...] - to display data for a specific molecular formula\ntable - to list all elements on the Periodic Table\nset (parameter) (element symbol) (new value) - to change an element's value\nget (parameter) (element symbol)\nsimulate - to run a simulation of the atoms in various molecules\nhelp - to display this prompt\nquit - to exit the terminal")
  
  # Parses CeH4... into [Ce, H4, ...] by looking for uppercase letters  
  def parse(self,string):
    chunks = []
    chunk = ''
    for i in string:
      if i.isupper() == 0:
        chunk += i
      else:
        chunks.append(chunk)
        chunk = i
    chunks.append(chunk)
    return chunks
  
  # Gets a parameter from an element
  def get_param(self, usersplit):
    try:
      if len(usersplit) < 3:
        raise KeyError
      element = Table.dict[usersplit[2]]
    except KeyError:
      # Value Errors in get_param, set_param, and info are to tell the self.run() function that the user inputed something that didn't work
      raise ValueError
    try:
      if usersplit[1] == "weight":
        print("The mass of",element.name,"is",element.get_weight(),"amu.")

      elif usersplit[1] == "boil":
        print("The boiling point of",element.name,"is",element.get_boil(),"°C.")

      elif usersplit[1] == "melt":
        print("The melting point of",element.name,"is",element.get_melt(),"°C.")

      elif usersplit[1] == "density":
        print("The vapor density of",element.name,"is",element.get_density_vapor(),".")

      elif usersplit[1] == "fusion":
        print("The fusion point of",element.name,"is",element.get_fusion(),"°C.")

      elif usersplit[1] == "name":
        print("The name of",element.name,"is",element.get_name(),".")
      else:
        raise ValueError
    except ValueError:
      return ValueError    

  def set_param(self, usersplit):
    try:
      if len(usersplit) < 4:
        raise KeyError
      element = Table.dict[usersplit[2]]
    except KeyError:
      raise ValueError
    try:
      if usersplit[1] == "weight":
        element.set_weight(float(usersplit[3]))
        print("The mass of",element.name,"has been changed to",element.get_weight(),"amu.")

      elif usersplit[1] == "boil":
        element.set_boil(float(usersplit[3]))
        print("The boiling point of",element.name,"has been changed to",element.get_boil(),"°C.")

      elif usersplit[1] == "melt":
        element.set_melt(float(usersplit[3]))
        print("The melting point of",element.name,"has been changed to",element.get_melt(),"°C.")

      elif usersplit[1] == "density":
        element.set_density_vapor(float(usersplit[3]))
        print("The vapor density of",element.name,"has been changed to",element.get_density_vapor(),".")

      elif usersplit[1] == "fusion":
        element.set_fusion(float(usersplit[3]))
        print("The fusion point of",element.name,"has been changed to",element.get_fusion(),"°C.")

      elif usersplit[1] == "name":
        print("The name of",element.name,"has been changed to",str(usersplit[3]),".")
        element.set_name(str(usersplit[3]))
        # I need to put that before because it needs to reference the old name and the new name!!!
        # Unless you want to make a temp variable...
      else:
        raise ValueError
    except ValueError:
      return ValueError
 
  # Returns info on chemical formulas and simulates atoms
  def info(self, usersplit, simulate=0):
    try:
      if len(usersplit) < 2:
        raise ValueError
      # Regular expression to check type of input is correctly formatted
      if bool([re.match("^[A-Za-z0-9\+\-\(\) ]*$", i) for i in usersplit]) == False:
        raise ValueError
    except ValueError:
      raise ValueError
    tempcaption = ""
    for i,x in enumerate(usersplit):
      tempcaption += x[i]
    parsed = []
    proton = 0
    for x in usersplit[1:]:
      parsed.append(self.parse(x))
      if "(" in x:
        tempcharge = x[x.find("(")+1 : x.find(")")]
        if tempcharge == "+":
          proton += 1
    tempmolecule = []
    for i, x in enumerate(parsed):
      if x[0] == "":
        tempcoeff = 1
      else:
        tempcoeff = x[0]
      for chunk in x:
        templetter = tempdigit = ''
        for letter in chunk:
          if letter.isalpha() == 1:
            templetter += letter
          else:
            if templetter != '':
              break
            templetter = ''
        for number in chunk:
          if number.isdigit() == 1:
            tempdigit += number
          else:
            if tempdigit != '':
              break
        if templetter != '' and tempdigit != '':
          tempmolecule.append((templetter,tempdigit))
        elif templetter != '' and tempdigit == '':
          tempmolecule.append((templetter,1))

    # Debug user input and standard output
    print("Detected Elements:")
    molecule_elements = []
    try:
      for i, x in enumerate(tempmolecule):
        print(str(x[0]) + " * " + str(x[1]))
        molecule_elements.append((Table.element_dict[x[0]], x[1]))
    except KeyError:
      print(str(x[0]) + " is not a valid element.")
      raise ValueError
    molecule = Molecule(molecule_elements, tempcoeff)
    print(f"Coefficient: {molecule.quantity}")
    print(f"Elements with Atomic Numbers, Symbols, and Atomic Mass:")
    [print(f"{i.name}({i.symbol}) - {i.number}, {i.weight}amu") for i in molecule]
    print(f"Total Mass of Molecule: {molecule.weight + proton}amu")

    # If simulating, put all the elements info was gathered on into a list and then simulate
    if simulate == 1:
      game_list = []
      for element, quantity in molecule.elements:
        for i in range(quantity):
          game_list.append(element)
      run_game(game_list)
 
  # Prints all the items in the table
  def table(self):
    for i in Table:
      print(f"{i.name}({i}) - {i.weight}amu")

  # Quits
  def quit(self):
    print("Goodbye.")
    quit()
  
  # The main loop for the user
  def run(self):
    while True:
      userget = input('>>> ')
      usersplit = userget.split(' ')
      try:
        if userget == "" or usersplit[0] == "quit":
          self.quit()
        elif usersplit[0] == "table":
          self.table()
        elif usersplit[0] == "help":
          self.userhelp()
        elif usersplit[0] == "info":
          self.info(usersplit)
        elif usersplit[0] == "get":
          self.get_param(usersplit)
        elif usersplit[0] == "set":
          self.set_param(usersplit)
        elif usersplit[0] == "simulate":
          self.info(usersplit, 1)
        else:
          raise ValueError
      except ValueError:
        print("You have entered an invalid statement. Please try again.")

try:
  terminal = Terminal()
  print("Welcome to the Periodic Terminal®.")
  terminal.userhelp()
  terminal.run()
except KeyboardInterrupt:
  print("Goodbye...")
  terminal.quit()






