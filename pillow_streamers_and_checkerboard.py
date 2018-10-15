from PIL import Image as i
import random as r
import sys

testing = False

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

# Create a checkerboard
side = int(sys.argv[1])
num_streamers = int(sys.argv[2])
checkerboard = Image("Checkerboard", side * 64, side * 64)
checkerboard.checkerboard(side)
checkerboard.save()
checkerboard.show()

# Create an image of streamers
streamers = Image("Streamers", 512, 512)
for i in range(num_streamers):
	streamers.streamer(r.randrange(0, 512), color=randcolor())
streamers.save()
streamers.show()





