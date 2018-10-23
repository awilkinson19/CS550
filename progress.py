import time

t = time.time()
p = 0
def progress(total, r=20, decimal=2, start=""):
	global p
	p += 1
	percent = int((10**decimal)*100*p/total)/10**decimal
	bar = ''
	for i in range(r):
		if percent/(100/r) > i:
			bar += '='
		else:
			bar += '-'
	print(f"{start} Progress: |{bar}|{percent}% Time: {time.time()-t}\r", end='')
