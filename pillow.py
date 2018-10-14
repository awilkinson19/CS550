from PIL import Image as i
import random as r

# Returns random color
def randcolor():
	return (r.randrange(0, 256), r.randrange(0, 256), r.randrange(0, 256))

# Returns a random point
def randpt():
	return (r.randrange(0, 512), r.randrange(0, 512))

# Image class
class Image:
	def __init__(self, name, height, width, file_type="PNG", color_type="RGB"):
		self.name = name
		self.height = height
		self.width = width
		self.file_type = file_type
		self.path = self.name + "." + self.file_type.lower()
		self.color_type = color_type
		self.im = i.new(self.color_type, (self.width, self.height))
		self.save()
		# self.bands = []

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

	# def line(self, m, point, color=(0, 0, 0), height=(0, self.height), width=(0, self.width)):
	# 	for x in range(width[0], width[1]):
	# 		for y in range(height[0], height[1]):
	# 			if y == m * (x - point[0]) + point[1]:
	# 				self.put((x, y), color)

	# def banded(self, pattern, color=(0, 0, 0)):
	# 	if pattern == 1:
	# 		for a, b in self.bands:
	# 			c = color
	# 			for x in range(a, b):
	# 				for y in range(0, self.height):
	# 					self.put((x, y), tuple(c))
	# 					new_c = []
	# 					for i in c:
	# 						if i < 255:
	# 							new_c.append(i + 1)
	# 					c = new_c

# Create an image of name image that's 512 x 512
image = Image("image", 512, 512)
# Paints it red
image.fill((255, 0, 0))
# image.bands = [(0, 100), (100, 200), (200, 400), (400, 511)]
# image.banded(1, color=(255, 0, 0))

# Puts 50 randomly placed, colored, and sized circles onto the image
for i in range(50):
	image.circle(randpt(), r.randrange(5, 20), randcolor())
image.save()
image.show()





