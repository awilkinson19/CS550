from pillow import Image

triangle = Image("Triangle", 1000, 1000)

triangle.triangle((100, 500), 100, 50, color=(255, 0, 0))
triangle.fill((255, 255, 255))

def sierpinski(image, start, side, height, testing=False):
	boo = True
	x, y = start
	color = [255, 0, 0]
	image.triangle((x, y), side, height, color=(0, 255, 0), up=boo, increment=1.5)
	for i in range(3):
		x += side//3
		y -= side // 3
		side = side // 3
		height = side//2
		color[2] += 50
		color[0] -= 50
		if testing:
			print(x, y, side, height)
		boo = not boo
		image.triangle((x, y), side, height, color=tuple(color), up=boo, increment=2)

sierpinski(triangle, (0, 999), 1000, 750, testing=True)


triangle.save()
triangle.show()
