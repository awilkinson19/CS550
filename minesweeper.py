import random
import printing as p
# Create a minesweeper board of width x, height y, and bombs

# Testing modes, anything in the functions with "if testing:" is purely for debugging
testing = False
draw_testing = False
initialize_testing = False
play_testing = False
expand_testing = False

# Gets the height width and bombs values from the user
def get_parameters():
	if testing:
		print("Getting Parameters")
	user_input = []
	height = p.ask("Height", ending=': ', option_type=int, num_range=(2, max_height + 1))
	width = p.ask("Width", ending=': ', option_type=int, num_range=(2, max_width + 1))
	bombs = p.ask("Bombs", ending=': ', option_type=int, num_range=(1, height*width))
	return height, width, bombs

# Maximum height and width values
max_height = 100
max_width = 100

# Parameters
parameters = get_parameters()
height = parameters[0]
width = parameters[1]
bombs = parameters[2]

# Create board variables and strings to substitute in for bombs or flagged tiles
board = []
bomb = -1

# These strings are shown for bombs, flags, and zeroes respectively
bomb_char = '*'
flag_char = '!'
empty_char = ' '

# Represents the values of the eight surrounding tiles
surrounding = (1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)

# Represents all the zero values already 'expanded'
expanded = []

# Sets up the game
def initialize(height, width, bombs):
	if testing:
		print("Initializing")
		print("Height =", height, "Width =", width, "Bombs =", bombs)
	global expanded
	expanded = []
	global board
	board = []
	remaining_area = height * width
	bomb_locations = []
	# Creates the board with bombs
	for h in range(height):
		board.append([])
		for w in range(width):

			# As the code goes along creating bombs, it uses this function to randomly place bombs
			# bombs -= 1 when a bomb is placed, and remaining area -= 1 whenever an item's added to the array
			bomb_chance = 100 * bombs / remaining_area

			# In each tile there is (int, bool, bool)
			# These represent the values (number of bombs surrounding the tile or bomb (-1 represents a bomb), revealed, flagged)

			if random.randrange(0, 100) < bomb_chance:
				# Setting Bombs
				board[h].append([bomb, False, False])
				bomb_locations.append((h, w))
				bombs -= 1
			else:
				# Setting Tiles
				board[h].append([0, False, False])
			remaining_area -= 1

	# Adds the bomb values
	for h, w in bomb_locations:
		for a, b in surrounding:
			# This gigantic if statement makes sure that it's not checking for higher values at the end of the board or things like that
			if not (h == 0 and a == -1 or w == 0 and b == -1) and not (h == height - 1 and a == 1 or w == width - 1 and b == 1):
				# If there's not a bomb there, add one to the tile
				if board[h+a][w+b][0] != bomb:
					board[h+a][w+b][0] += 1
	if initialize_testing:
		print(board)

def expand(zero):
	if testing:
		print("Expanding")
	# Shows nearby spaces when user reveals a zero
	y, x = zero
	# List of zero values already revealed
	expanded.append((y, x))
	if expand_testing:
		print("Expanded:", expanded)
	# For each surrounding value, reveal it and then expand it if it's a zero that hasn't already been expanded
	for a, b in surrounding:
		if not (y == 0 and a == -1 or x == 0 and b == -1) and not (y == height - 1 and a == 1 or x == width - 1 and b == 1):
			if expand_testing:
				print("Revealing:", y+a, x+b, board[y+a][x+b][0] == 0, (y+a, x+b) not in expanded)
			board[y+a][x+b][1] = True
			if board[y+a][x+b][0] == 0 and (y+a, x+b) not in expanded:
				if expand_testing:
					print(y+a, x+b)
				expand([y+a, x+b])

def reveal():
	if testing:
		print("Revealing")
	# Prints each item in the 2-D list to reveal the board
	to_print = ''
	for row in board:
		for item in row:
			# Replaces 0 with ' '
			if item[0] == 0:
				to_print += empty_char
			# Replaces bombs with either a flag or bomb character depending on whether they're flagged or not
			elif item[0] == bomb:
				if item[2] == False:
					to_print += bomb_char
				else:
					to_print += flag_char
			# Prints the numbers as is
			else:
				to_print += str(item[0])
			to_print += ' '
		to_print += '\n'
	print(to_print)

def draw():
	'''Serves dual purpose of printing the game board and checking for completion'''
	game_ended = False

	# The tapped value will increment for each space the user reveals or flags
	# The tapped and completed values are used in calculating completion
	tapped = 0
	completed = 0
	
	if testing:
		print("Drawing")
	# Prints top barrier
	to_print = '  ---' + '--' * width + '\n'
	if draw_testing:
		print(board)
	# Prints the game board
	for h, row in enumerate(board):
		# Adds numbers along Y axis
		to_print += str(height - h) + ' | '
		# Prints each number in the row
		for item in row:
			# Puts a flag where user flagged item
			if item[2]:
				to_print += flag_char
				tapped += 1
			# If item is revealed, print the item
			elif item[1]:
				# replace 0 with ' '
				if item[0] == 0:
					to_print += empty_char
					tapped += 1
				else:
					to_print += str(item[0])
					tapped += 1
			# print an X for spaces that aren't revealed
			else:
				to_print += 'X'
			to_print += ' '
		if draw_testing:
			print(to_print)
		to_print += '|\n'
	# Print bottom barrier
	to_print += '  ---' + '--' * width + '\n'
	to_print += '    '
	# Add labels to X axis
	for w in range(width):
		to_print += str(w + 1) +  ' '
	# Print
	print(to_print)

	# If the entire board is either revealed or flagged, check for completion
	total = width * height
	if tapped == total:
		# Tell the user if they won or lost
		if check():
			print("You won!")
		else:
			print("You lost!")
		game_ended = True

	# Show user how close they are to completing the game because I already have the tapped and total values
	completed = 100 * tapped // total
	if testing:
		print("Tapped =", tapped, "Completed =", completed)
	print(f"{completed}% Completed")
	return game_ended

def check():
	# Checks if user correctly completed the game
	won = True
	for row in board:
		for item in row:
			# If it's flagged and not a bomb, the user loses the game
			if item[2]:
				if item[0] != bomb:
					won = False
	return won

def play():
	# This is the main loop of the game that runs everything
	if testing:
		print("Playing")
	# Set up the game
	initialize(height, width, bombs)
	lost = False
	playing = True
	turn_one = True

	# Start the game
	while playing:
		# Draw the board and if the player won or lost, stop playing
		if draw():
			break

		# Make user choose values
		choosing = True
		while choosing:
			user_choice = []

			# Make sure user choices are integers between 1 and the height/width of the board
			user_choice.append(height - p.ask("Y", option_type=int, ending=': ', end='', num_range=(1,height + 1)))
			user_choice.append(p.ask("X", option_type=int, ending=': ', end='', num_range=(1,width + 1)) - 1)
			
			# If the user revealed or flagged the value already, make the user choose again, else continue
			choice = board[user_choice[0]][user_choice[1]]
			if choice[1] or choice[2]:
				print("\nYou already chose this value, please choose again.\n")
			else:
				choosing = False

		# User picks between clear or flag if it's not the first turn
		if not turn_one:
			user_action = p.ask("Clear or Flag (c/f)", options=['c','f'])
			if user_action == 'f':
				board[user_choice[0]][user_choice[1]][2] = True
				if play_testing:
					print(board[user_choice[0]][user_choice[1]][2])
				print('')
				continue

		# To clear the space
		print('')
		# Reveal the item
		choice[1] = True
		# If it's a zero, show nearby numbers
		if choice[0] == 0:
			expand(user_choice)
		if testing:
			print(board[user_choice[0]][user_choice[1]])
		# If it's a bomb and not the first turn, user loses the game, else recreate the board until there's not a bomb at that spot
		if choice[0] == bomb:
			if turn_one:
				dead = True
				while dead:
					# Recreates board
					initialize(height, width, bombs)
					choice = board[user_choice[0]][user_choice[1]]
					# If the choice isn't a bomb, make that the new board
					if choice[0] != bomb:
						dead = False
						choice[1] = True
			else:
				# If it isn't the first turn, the user loses the game
				lost = True
		# If you lost, reveal the board and tell the user
		if lost:
			print("You lost!")
			reveal()
			playing = False
		turn_one = False

