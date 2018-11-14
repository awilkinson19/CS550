from PIL import Image
from PIL import ImageFilter, ImageDraw, ImageFont
from pillow import Im
import random as r
import os

dirname = "water_lilly"

def filter(path):
	im = Im(path)

	draw = ImageDraw.Draw(im.im)
	font = ImageFont.truetype('Sofye Demo.ttf', size=50)
	draw.text((-30, im.height-70), "#ChoateMoments !", font=font, color=(255, 255, 0))

	for i in range(100):
		if i % 2 == 0:
			color = (0, 0, 255)
		else:
			color = (255, 255, 0)
		width, length = [r.randrange(2, 6), r.randrange(5, 20)]
		im.streamer(r.randrange(0, im.width-width), r.randrange(0, im.height-length), width, length, color=color)

	im.save()
	im.show()

for file in os.listdir(dirname):
	print(file)
	filter(dirname+'/'+file)





