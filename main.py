from pillow import Image
import math as m

height = 866
width = 1000
triangle = Image("triangle", height, width)

triangle.fill((255, 255, 255))

def sierpinski(image, start, side, testing=False):
	boo = True
	width, height = start
	x, y = width, height
	s = side
	color = [255, 0, 0]
	image.triangle((x, y), side, color=(0, 255, 0), up=boo, increment=m.sqrt(3))
	for i in range(2):
		y -= side * m.sqrt(3) / 4
		x += side / 4
		s = s // 2
		color[2] += 50
		color[0] -= 50
		if testing:
			print(x, y, s)
		boo = not boo
		image.triangle((int(x), int(y)), s, color=tuple(color), up=boo, increment=2)

sierpinski(triangle, (0, height-1), width, testing=True)


triangle.save()
triangle.show()
