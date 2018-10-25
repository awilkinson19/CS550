from pillow import Image
import math
import progress as p
import sys

testing = True
s = True

xa, xb = -2.0, 2.0
ya, yb = -2.0, 2.0
if s:
	xa, xb = float(sys.argv[1]), float(sys.argv[2])
	ya, yb = float(sys.argv[3]), float(sys.argv[4])
imgx, imgy = 1000, 1000
max_depth = 256
m = Image("mandelbrot", imgx, imgy)
j = Image("julia", imgx, imgy)
c = -.75

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
# 		p.progress(m.height*m.width, name=m.name)
# 		x = w * (xb - xa) / (m.width - 1) + xa
# 		c = complex(x, y)
# 		r, g, b = 1*mandelbrot(c), 0*mandelbrot(c), 0*mandelbrot(c)

# 		m.put((w, h), (r, g, b))

# m.save()
# m.show()

for h in range(j.height):
	y = h * (yb - ya) / (j.height - 1) + ya
	for w in range(j.width):
		# p.progress(j.height*j.width, name="Julia")
		x = w * (xb - xa) / (j.width - 1) + xa
		z = complex(x, y)
		jul = julia(z, c)
		r, g, b = jul, jul, jul

		j.put((int(w), int(h)), (r, g, b), color_type="hsv")

j.save()
j.show()
