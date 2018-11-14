from PIL import Image as i
import random as r
import sys
import os
import colorsys as c
from PIL import ImageFilter, ImageDraw, ImageFont

# Image class
class Im:
	def __init__(self, name, file_type="jpg", color_type="RGB", s=False):
		if s:
			self.name, self.file_type = sys.argv[1].split('.')
		else:
			self.name, self.file_type = name.split('.')
		self.file_type = file_type
		self.path = self.name + "." + self.file_type.lower()
		self.color_type = color_type
		self.im = i.open(self.path)
		self.save()
		self.width = self.im.width
		self.height = self.im.height


	# Returns random color
	def randcolor():
		return (r.randrange(0, 256), r.randrange(0, 256), r.randrange(0, 256))

	# Returns a random point
	def randpt():
		return (r.randrange(0, 512), r.randrange(0, 512))

	# Saves image
	def save(self):
		self.im.save(self.path)

	# Places a color at a certain pixel
	def put(self, coordinate, color=(0, 0, 0), color_type=None):
		if color_type == "hsv":
			maximum = [0, 0, 0]
			minimum = maximum
			color = c.hsv_to_rgb(color[0], color[1], color[2])
		elif color_type == "yiq":
			color = c.yiq_to_rgb(color[0], color[1], color[2])
		try:
			self.im.putpixel(coordinate, color)
		except TypeError:
			color = tuple([int(i) for i in color])
			self.im.putpixel(coordinate, color)
		except IndexError:
			pass

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

	# Creates streamers
	def streamer(self, start_width, start_height, width, length, color=(0, 0, 0)):
		w = start_width
		self.put((w, start_height), color)
		for height in range(start_height, start_height+length):
			choice = r.randint(0, 3)
			if choice == 0 and width != 0:
				w -= 1
			elif choice == 2 and width != self.width-1-width:
				w += 1
			for i in range(0, width):
				self.put((w+i, height), color=color)


