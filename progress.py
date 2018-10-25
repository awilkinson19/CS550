import time

i = time.time()
def t(decimal=2):
	global i
	return int(10**decimal*(time.time()-i))/10**decimal

p = 0
def progress(total, r=20, decimal=2, name=""):
	global p
	p += 1
	percent = int((10**decimal)*100*p/total)/10**decimal
	bar = ''
	for i in range(r):
		if percent/(100/r) > i:
			bar += '='
		else:
			bar += '-'
	print(f"{name} Progress: |{bar}|{percent}% Time: {t()}s\r", end='')

def reset(name=''):
	global i
	i = time.time()
	global p
	p = 0
	print(f"{name} Completed")
