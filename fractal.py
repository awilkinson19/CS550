from pillow import Image
import math
import progress as p
import sys
import math

'''
10/25/18
Alex Wilkinson
It uses colorsys with the Julia and the Mandelbrot sets to create colored images of those sets.
On my honor, I have neither given nor received unauthorized aid.
'''

testing = True
s = False
i = False

xa, xb = .4, .37
ya, yb = .25, .35

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

imgx, imgy = 1000, 1000
max_depth = 256
m = Image("mandelbrot", imgx, imgy)
j = Image("julia", imgx, imgy)

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

# for h in range(m.height):
# 	y = h * (yb - ya) / (m.height - 1) + ya
# 	for w in range(m.width):
# 		p.progress(m.height*m.width, name="Mandelbrot")
# 		x = w * (xb - xa) / (m.width - 1) + xa
# 		c = complex(x, y)
# 		man = mandelbrot(c)+1
# 		r, g, b = 0, 0, 0

# 		m.put((w, h), (r, g, b), color_type="hsv")

# m.save()
# m.show()

# Julia vals
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
		r, g, b = 240, 100, 50

		# Hue, picks color
		r = 179/jul%4

		# Saturation
		g = 256

		# Brightness Values
		b = 256 / 2

		j.put((int(w), int(h)), (r, g, b), color_type="hsv")


j.save()
j.show()
