from pillow import Image
import math
import progress as p

testing = False

xa, xb = -2.0, 2.0
ya, yb = -2.0, 2.0
imgx, imgy = 512, 512
max_depth = 256
m = Image("", 0, 0, s=True)

# Mandelbrot: Zn+1 = Zn^2 + c
def mandelbrot(z, c):
	return z**2 + c

# Counting recursion depth for the mandelbrot calculations
def recursion(x, y):
	c = complex(x, y)
	num = mandelbrot(c, c)
	depth = 0
	while abs(num) <= 2 and depth < max_depth:
		num = mandelbrot(num, c)
		depth += 1
	return depth

for h in range(m.height):
	y = h * (yb - ya) / (m.height - 1) + ya
	for w in range(m.width):
		p.progress(m.height*m.width)
		x = w * (xb - xa) / (m.width - 1) + xa
		c = complex(x, y)
		z = 0
		r, g, b = 1*recursion(z, c), 0*recursion(z, c), 0*recursion(z, c)

		m.put((w, h), (r, g, b))

m.save()
m.show()
