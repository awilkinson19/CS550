import random as r
import numpy as np
import matplotlib.pyplot as plt

'''
What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?
- 22

Please explain your solution at the top of the code, to demonstrate understanding.
- I created a checking algorithm that looped through numbers, returning the percentage that I could walk home, to find the answer.

What are Monte Carlo simulations?
- Monte Carlo simulations use randomness to simulate real events or to approximate solutions to problems.

What can they be used for?
- Calculating risk, pi, or any problems with input uncertainty

How do they work?
- Inputs are generated randomly over and over and then used to simulate or calculate solutions to problems with a high degree of accuracy
'''

def walk(blocks):
	# Set home
	x, y = 0, 0
	for i in range(blocks):
		# Choose to modify x or y, then modify that variable by one unit
		if r.choice([True, False]):
			x += r.choice([1, -1])
		else:
			y += r.choice([1, -1])
	# Return distance to home
	return abs(x) + abs(y)

def check(n, num=10000, limit=5):
	data = np.array([walk(n) for i in range(num)])
	# np.where(condition)[0] is a list of all the indices in a numpy array where the condition is met
	prob = len(np.where(data < limit)[0])/num
	return f"{n}: {prob*100}%"

num = 0
while input(check(num)) == '':
	num += 1

def throw(darts, r):
	board = []
	for i in range(darts):
		board.append(np.array([r.uniform(-1*r, r), r.uniform(-1*r, r)]))
	return np.array(board)

def on_target(darts, radius=1.0):
	# Get an array of darts thrown
	data = throw(darts, radius)
	# Find all darts less than 1 unit away from the center
	result = 4*len(np.where((data[:, 0]**2 + data[:, 1]**2) <= radius**2)[0])/darts
	return result

print(on_target(100))
print(on_target(1000))
print(on_target(10000))
print(on_target(100000))
print(on_target(1000000))
# The values approach pi




# data = np.asarray([walk(100) for i in range(10000)])
# bin = [i for i in range(0, 101, 2)]

# plt.hist(data, bins=bin)
# plt.show()

