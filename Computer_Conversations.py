import random as r
'''
Sept. 10, 2018
Computer Conversations
	It's an unpolished electronic assistant. It has its
store of bad jokes and songs to select for you, and can
write down a list for you as well.

Overview:
- sets joke and song libraries, turns on, and gets name.
- asks for a choice of activity and then...
	if keyword 'list' is said
	- makes a list by splitting the sentence at the commas, 
	then it removes the beginning of the sentence and the 
	'and' and '.'. Then it prints the sentence

	if keyword 'song' is said
	- selects a song from the library for you to play

	if keyword 'joke' is said
	- selects a joke from the library to tell

	if keywords 'off' or 'quit' are said
	- asks if you want to quit and then quits if answer is yes

	if nothing, or after anything but a quit command
	- start loop over again at asking for a choice
'''

jokes = ["Why didn't the skeleton cross the road?\nBecause it didn't have the guts to do it."]
songs = ["Despacito", "Fireflies", "Happy Birthday", "Africa"]
on = True
name = input("Hello, I'm your electronic assistant.\nWhat's your name?\n> ").capitalize()
print("Hello, "+name+"!")
while on:
	choice = input("What do you want to do, "+name+"?\nExamples include: making a list, selecting a song, or telling a joke.\n> ")
	if "list" in choice:
		user_list = input("Make your list.\n> ").split(', ')
		final_list = []
		for idx, item in enumerate(user_list):
			if idx == 0:
				item = item.split(' ')[-1]
			elif idx+1 == len(user_list):
				if "and" in item:
					item = item[4:]
				if "." in item:
					item = item[0:-1]
			final_list.append(item)
		print("Okay, "+name+", here's your list: "+str(final_list))
	if "song" in choice:
		song = r.choice(songs)
		print("Okay, play this song: ", song)
	if "joke" in choice:
		joke = r.choice(jokes)
		print(joke)
	if "off" in choice or "quit" in choice:
		if input("Do you want to quit? (Y/N)\n> ") == "Y":
			on = False
			print("Quitting now.")