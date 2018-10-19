from pillow import Image
import math

testing = False

# Mandelbrot: Zn+1 = Zn^2 + c
def mandelbrot(z, c):
	return z**2 + c

# Counting recursion depth for the mandelbrot calculations
def recursion(x, y):
	c = complex(x, y)
	num = mandelbrot(c, c)
	depth = -1
	while abs(num) <= 2 and depth < 255:
		num = mandelbrot(num, c)
		depth += 1
	return depth

# for x in range(-2, 3):
# 	for y in range(-2, 3):
# 		print("R:", recursion(x, y), "P:", (x, y))

m = Image("", 0, 0, s=True)

signs = (1, -1), (1, 1), (-1, -1), (-1, 1)
for s in signs:
	for a in range(0, m.height-m.height//2):
		x = (2/(m.height//2))*a
		if testing:
			print(a, x)
		for b in range(0, m.width-m.width//2):
			y = (2/(m.width//2))*b
			if x != 0 or y != 0:
				# Trying to transform the numbers I'm using to calculate into points on the image
				print((x*s[0], y*s[1]), recursion(x*s[0], y*s[1]))
				print((int((x*s[0]/4+0.5)*m.height), int((y*s[1]/4 + 0.5)*m.height)))

# Adding in the zero
if m.height % 2 != 0:
	m.put((0, 0), color=(255, 0, 0))
