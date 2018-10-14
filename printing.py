# Testing mode, anything starting with if testing is for debugging only
testing = False

# The ultimate user input function
def ask(question, options=None, double_check=False, option_type=None, end='\n', ending='\n>>> ', num_range=None, boolean=False):
	'''
	If you do nothing other than ask(Hows your day?) it will act as input(hows your day?/n>>> )
	The other options are for ease of use
	'''
	if testing:
		print("Asking")
	asking = True
	while asking:
		# Ask the question with chosen ending
		answer = input(question + ending)

		# Whenever a continue is used, it asks the user the question again and starts from the top

		# If the answer is Quit, quit the game
		if answer == "Quit":
			quit()

		# If a true/false response is wanted, make sure a yes or no is received and return a bool
		if boolean:
			if answer in ["Yes", 'yes', 'Y', 'y']:
				return True
			elif answer in ["No", 'no', 'N', 'n']:
				return False
			else:
				print("You need to respond with yes or no.")
				continue

		# If there are specified options, make sure the user answers one of the specified options
		if options != None:
			if answer not in options:
				print("I'm sorry, but that's not a valid answer")
				continue

		# If there's a specified option type, make sure the user answers with the specified data type
		if option_type != None:
			# If the specified type is an integer, try to return an integer, else return to the top
			try:
				if option_type == int:
					answer = int(answer)

					# If there's a specified range, make sure the number's within that range
					if num_range != None:
						if answer not in range(num_range[0], num_range[1]):
							print("I'm sorry, your number is out of range.")
							continue

			except ValueError:
				if option_type == int:
					option_type_str = 'integer'
				print(f"I'm sorry, you need to respond with the data type {option_type_str}.\nTry again.")
				continue

		# If there's a double check, require user confirmation		
		if double_check:
			keep = input(f"You response: {answer}\nDo you want to keep that response?\nRespond with either Yes or No")
			if keep == "Yes":
				pass
			elif keep == "No":
				print("OK, from the top!")
				continue
			else:
				print("You didn't respond with Yes or No.\nLet's start from the top!")
				continue

		# If everything worked, stop asking and return the answer
		asking = False
	return answer
