from PIL import Image as i
import random as r
import sys

testing = False
progress = True

# Image class
class Image:
	def __init__(self, name, height, width, file_type="PNG", color_type="RGB", s=False):
		if s:
			self.name = sys.argv[1]
			self.height = int(sys.argv[2])
			self.width = int(sys.argv[3])
		else:
			self.name = name
			self.height = height
			self.width = width
		self.file_type = file_type
		self.path = self.name + "." + self.file_type.lower()
		self.color_type = color_type
		self.im = i.new(self.color_type, (self.width, self.height))
		self.save()

	# Returns random color
	def randcolor():
		return (r.randrange(0, 256), r.randrange(0, 256), r.randrange(0, 256))

	# Returns a random point
	def randpt():
		return (r.randrange(0, 512), r.randrange(0, 512))

	# Saves image
	def save(self):
		self.im.save(self.path, self.file_type)

	# Places a color at a certain pixel
	def put(self, coordinate, color=(0, 0, 0)):
		self.im.putpixel(coordinate, color)

	# Fills the image
	def fill(self, color):
		for x in range(self.width):
			for y in range(self.height):
				self.put((x, y), color)

	# Shows the image
	def show(self):
		self.im.show()

	# Draws an isosceles triangle
	def triangle(self, start_point, side_length, height, color=(0, 0, 0), testing=True, range_testing=False, up=True, increment=1):
		x, y = start_point
		h = 0
		base = y
		rising = True
		for a in range(side_length):
			for b in range(int(h)):
				if range_testing:
					print(x+a, int(y-b), end=' ')
				self.put((x+a, int(y-b)), color)
			if range_testing:
				print('')
			if up:
				if h < height and rising:
					h += increment
				if h >= height and rising:
					if testing:
						print(rising)
					rising = False
					if testing:
						print(rising)
				if y-h < base and not rising:
					h -= increment
			else:
				pass

		# rising = True
		# x, y = start_point
		# h = 0
		# going = True
		# base = y
		# first_time = True
		# for a in range(side_length):
		# 	self.put((x, y), color)
		# 	if up:
		# 		print(rising, end=' ')
		# 		if not rising or h != 0:
		# 			for b in range(int(h)):
		# 				if range_testing:
		# 					print(x, y-b, end=' ')
		# 				self.put((x, y-b), color)
		# 			if range_testing:
		# 				print('')
		# 	else:
		# 		for b in range(int(h)):
		# 			self.put((x, y+b), color)
		# 	if h != 0 or first_time:
		# 		if rising:
		# 			h -= increment
		# 		if h == height:
		# 			rising = False
		# 		if not rising:
		# 			h += increment
		# 	x += 1
		# 	first_time = False
		# 	if testing:
		# 		print(f"X: {x}, Y: {y}, H: {h}")

	# Draws a square on the image
	def square(self, w, h, color=(0, 0, 0)):
		for x in range(w[0], w[1]):
			for y in range(h[0], h[1]):
				self.put((x, y), color)

	# Draws a circle on the image
	def circle(self, center, radius, color=(0, 0, 0)):
		for x in range(self.width):
			for y in range(self.height):
				if radius ** 2 >= (x - center[0]) ** 2 + (y - center[1]) ** 2:
					self.put((x, y), color)

	# Draws a checkerboard
	def checkerboard(self, side, color1=(255, 0, 0), color2=(0, 0, 0)):
		first = True
		band = self.width // side
		bands = [i for i in range(0,self.width+1, band)]
		if testing:
			print(bands)
		for a in range(side):
			first = not first
			for b in range(side):
				if first:
					c = color1
				else:
					c = color2
				self.square((bands[a], bands[a+1]), (bands[b], bands[b+1]), c)
				if testing:
					print(bands[a], bands[a+1], bands[b], bands[b+1], c)
					print(first)
				first = not first

	# Creates streamers
	def streamer(self, start_width, color=(0, 0, 0)):
		width = start_width
		self.put((width, 0), color)
		for height in range(1, self.height):
			choice = r.randint(0, 3)
			if choice == 0 and width != 0:
				width -= 1
			elif choice == 2 and width != self.width-1:
				width += 1
			self.put((width, height), color=color)


