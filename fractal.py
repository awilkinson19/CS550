from pillow import Image
import math
import progress as p
import sys
import math

'''
10/25/18
Alex Wilkinson
It uses colorsys with the Julia and the Mandelbrot sets to create colored images of those sets.
Each of the three images is generated in a similar way, with the values modified and then passed in as hsv values through the pillow file.

On my honor, I have neither given nor received unauthorized aid.
'''

testing = True
s = False
i = False

xa, xb = 2, -2
ya, yb = 2, -2

if s:
	xa, xb = float(sys.argv[1]), float(sys.argv[2])
	ya, yb = float(sys.argv[3]), float(sys.argv[4])
	c = float(sys.argv[5])

if i:
	xa = float(input("Xa: "))
	xb = float(input("Xb: "))
	ya = float(input("Ya: "))
	yb = float(input("Yb: "))
	c = float(input("C: "))

imgx, imgy = 1024, 1024
max_depth = 256

# Julia:
def julia(z, c):
	z = z**2 + c
	depth = 0
	while abs(z) <= 1.5 and depth < max_depth:
		z = z**2 + c
		depth += 1
	return depth

# Counting recursion depth for the mandelbrot calculations
def mandelbrot(c):
	z = c**2 + c
	depth = 0
	while abs(z) <= 2 and depth < max_depth:
		z = z**2 + c
		depth += 1
	return depth

# First Mandelbrot

# Create the image through the pillow file
m = Image("mandelbrot", imgx, imgy)

# Pick Values for the image
xa, xb = .4, .37
ya, yb = .25, .29

# Iterate through the image while calculating the Mandelbrot function
for h in range(m.height):
	y = h * (yb - ya) / (m.height - 1) + ya
	for w in range(m.width):

		# Progress bar function
		p.progress(m.height*m.width, name="Mandelbrot")

		x = w * (xb - xa) / (m.width - 1) + xa
		c = complex(x, y)
		man = mandelbrot(c)+1

		# Initializes hsv values (h was set to height, so it's now a)
		a, s, v = 0, 0, 0

		# Modifies values to make it interesting
		a = (man/4)%4 * 1
		s = man%4 * 60
		v = (man%4 * 6)**2

		# Puts in a pixel with the specified color
		m.put((w, h), (a, s, v), color_type="hsv")

# Saves and shows the image
m.save()
m.show()

# Second Mandelbrot
m2 = Image("mandelbrot2", imgx, imgy)

xa, xb = -1.2, -1.5
ya, yb = .18, 0.07

for h in range(m2.height):
	y = h * (yb - ya) / (m2.height - 1) + ya
	for w in range(m2.width):
		p.progress(m2.height*m2.width, name="Mandelbrot")
		x = w * (xb - xa) / (m2.width - 1) + xa
		c = complex(x, y)
		man = mandelbrot(c)+1
		a, s, v = 0, 0, 0

		a = man**0.5 * 6
		s = man%4**5
		v = math.log(man)**6

		m2.put((w, h), (a, s, v), color_type="hsv")

m2.save()
m2.show()

# Julia
j = Image("julia", imgx, imgy)

xa, xb = .6, .4
ya, yb = .15, .35
c = -.75

for h in range(j.height):
	y = h * (yb - ya) / (j.height - 1) + ya
	for w in range(j.width):
		p.progress(j.height*j.width, name="Julia")
		x = w * (xb - xa) / (j.width - 1) + xa
		z = complex(x, y)
		jul = julia(z, c) + 1
		a, s, v = 0, 0, 0

		a = 179/jul%4
		s = 256
		v = 256 / 2

		j.put((w, h), (a, s, v), color_type="hsv")


j.save()
j.show()
