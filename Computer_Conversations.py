import random as r

jokes = ["Why didn't the skeleton cross the road?\nBecause it didn't have the guts to do it."]
songs = ["Despacito", "Fireflies", "Happy Birthday"]
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