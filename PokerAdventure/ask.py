def sprint(statement, t=0.03, end_time=0.5):
	lines = statement.split('\n')
	for line in lines:
		to_print = ''
		for c in line:
			to_print += c
			print(f"{to_print}\r", end='')
			time.sleep(t)
		print('')
	time.sleep(end_time)

def sask(question):
	sprint(question)
	return input('>>> ')

def ask(question, options=None, double_check=False, option_type=None):
	asking = True
	while asking:
		answer = sask(question)
		if answer == "Quit":
			quit()
		if options != None:
			if answer not in options:
				sprint("I'm sorry, but that's not a valid answer")
				asking = True
		if option_type != None:
			if type(answer) != option_type:
				sprint(f"I'm sorry, you need to respond with the data type {option_type}.\nTry again.")
				asking = True
		if double_check:
			keep = sask(f"You response: {answer}\nDo you want to keep that response?\nRespond with either Yes or No")
			asking = True
			if keep == "Yes":
				pass
			elif keep == "No":
				sprint("OK, from the top!")
				asking = True
			else:
				sprint("This isn't rocket science, I gave you two options: Yes or No\nYet, you just refused to pick one.\nLet's start from the top!")
				asking = True
		asking = False
	return answer


