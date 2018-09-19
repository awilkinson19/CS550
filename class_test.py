num = 0
while True:
	try:
		num = int(input("Pick a number between 1 and 5 "))
		if 1<=num<=5:
			print("Success")
			break
		else:
			print("not between 1 and 5")
	except ValueError:
		print("Type in a number")
