import sys
import random
# Create a minesweeper board of width x, height y, and bombs

# arguments in the terminal
user_input = sys.argv[1:]

height = int(user_input[0])
width = int(user_input[1])
bombs = int(user_input[2])

class Minesweeper:

	def __init__(self, height, width, bombs):
		self.board = []
		self.bomb = '*'
		self.initialize(height, width, bombs)

	def initialize(self, height, width, bombs):
		remaining_area = height * width
		bomb_locations = []
		# Creates the board with bombs
		for h in range(height):
			self.board.append([])
			for w in range(width):
				bomb_chance = 100 * bombs / remaining_area
				if random.randrange(0, 100) < bomb_chance:
					self.board[h].append(self.bomb)
					bomb_locations.append((h, w))
					bombs -= 1
				else:
					self.board[h].append(0)
				remaining_area -= 1
		# Adds the bomb values
		surrounding = (1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)
		for h, w in bomb_locations:
			for a, b in surrounding:
				if not (h == 0 and a == -1 or w == 0 and b == -1):
					try:
						if self.board[h+a][w+b] != self.bomb:
							self.board[h+a][w+b] += 1
					except IndexError:
						pass

	def draw(self):
		to_print = ''
		for row in self.board:
			for item in row:
				to_print += str(item) + ' '
			to_print += '\n'
		print(to_print)

game = Minesweeper(height, width, bombs)
game.draw()