'''
Challenge: create an unbreakable program that takes in two arguments (a and b) and then print a^1, a^2, ... a^b
'''

undefined = True
while undefined:
	try:
		user_input = input("Enter two numbers separated by a space: a base and exponent:\n>>> ")
		user_input = user_input.split(' ')
		user_input = [int(i) for i in user_input]
		if len(user_input) > 1:
			undefined = False
		else:
			print("You didn't follow directions, try again.")
	except ValueError:
		print("You didn't follow directions, try again.")

for i in range(1, 1 + user_input[1]):
	print(user_input[0] ** i, ' ', end='')

print('')
