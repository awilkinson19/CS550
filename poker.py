import random
import time
import score as s

'''Alex Wilkinson Sept. 24 2018, this is a poker game simulator.'''
# Poker hand scoring code from: https://github.com/omarshammas/pyPoker-Texas-HoldEm/blob/master/holdem.py

# A dramatic slow print function
def sprint(statement, t=0.05, end_time=0.1):
	lines = statement.split('\n')
	for line in lines:
		to_print = ''
		for c in line:
			to_print += c
			print(f"{to_print}\r", end='')
			time.sleep(t)
		print('')
	time.sleep(end_time)

# a dramatic slow ask function
def sask(question):
	sprint(question)
	return input('>>> ')

# My version of the input statement, but with some added commands.
def ask(question, options=None, double_check=False, option_type=None):
	asking = True
	while asking:
		asking = False
		# get answer from user
		answer = sask(question)
		# look for other functions the user might want
		if answer == "Pot":
			try:
				print(f"The pot size is {poker.pot} chips.")
			except NameError:
				print("Were you trying to break the code?")
		if answer == "View table":
			try:
				print(poker.card_str(poker.table))
			except NameError:
				print("Were you trying to break the code?")
		if answer == "Chip count":
			try:
				for p in players:
					print(f"{p.name}: {p.chips}")
			except NameError:
				print("Were you trying to break the code?")
		if answer == "Quit":
			quit()
		if answer == "Hand strength":
			try:
				user.hand_strength()
			except NameError:
				print("Were you trying to break the code?")

		# Additional functions of ask that allow for me to ask from a set of options or option type.
		if options != None:
			if answer not in options:
				print("I'm sorry, but that's not a valid answer")
				asking = True
		if option_type != None:
			if option_type == int:
				try: 
					answer = int(answer)
				except ValueError:
					print(f"I'm sorry, you need to respond with the data type {option_type}.\nTry again.")
					asking = True

		# double checks with user
		if double_check:
			keep = sask(f"You response: {answer}\nDo you want to keep that response?\nRespond with either Yes or No")
			asking = True
			if keep == "Yes":
				return answer
			elif keep == "No":
				sprint("OK, from the top!")
				asking = True
			else:
				sprint("This isn't rocket science, I gave you two options: Yes or No\nYet, you just refused to pick one.\nLet's start from the top!")
				asking = True
	return answer




players = []
playing = players

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.chips = 1000
		self.contribution = 0
		players.append(self)
		self.score_str = {0: f"High Card", 1: "Pair", 2: "Two Pairs", 3: "Three of a Kind", 4: "Straight", 5: "Flush", 6: "Full House", 7: "Four of a Kind", 8: "Straight Flush", 9: "Royal Flush"}

	# Gives players options depending on whether there's a bet on the table or not
	def get_actions(self):
		to_return = []
		if self.contribution < poker.top_contribution:
			to_return.append("Fold")
			to_return.append("Call")
			to_return.append("Raise")
		else:
			to_return.append("Check")
			to_return.append("Bet")
		return to_return

	# sees the strength of the user's hand
	def score(self):
		poker_hand = poker.table + self.hand
		return s.score(poker_hand)

	# puts an amount into the pot from a user
	def bet(self, amount):
		self.chips -= amount
		poker.pot += amount
		self.contribution += amount
		if self.contribution > poker.top_contribution:
			poker.top_contribution = self.contribution
		print("The pot now has",poker.pot,"chips.")

# creates bot subclass for other players
class Bot(Player):
	# chooses a random action and random values for that action
	def choose_action(self):
		options = self.get_actions()
		action = random.choice(options)
		value = 0
		if action == "Raise":
			value = poker.top_contribution - self.contribution + random.randint(1, self.chips // 70)
		elif action == "Bet":
			value = random.randint(1, self.chips // 70)
		elif action == "Call":
			pass
		elif action == "Fold":
			pass
		return action, value

class User(Player):
	# asks player for option and amount
	def choose_action(self):
		options = self.get_actions()
		value = 0
		action = ask(f"What do you want to do?\nYour options are: {options}", options=options)
		if action == "Raise":
			value = poker.top_contribution - self.contribution + int(ask(f"You need to bet {poker.top_contribution - self.contribution} to call.\nHow much do you want to raise by?", option_type=int))
		elif action == "All-In":
			value = self.chips
		elif action == "Bet":
			value = int(ask("How much?", option_type=int))
		elif action == "Call":
			pass
		elif action == "Fold":
			pass
		return action, value

	# gives player a sense of their hand strength
	def hand_strength(self):
		if len(self.hand) < 2:
			print("I'm sorry, but you don't have enough cards in your hand for this function.")
		else:
			strength = self.score()
			print(f"You have a {self.score_str[strength[0]]}, with a {poker.num_str[strength[1]]} as a kicker")

# creates bots
player1 = Bot("Daniel Heredia")
player2 = Bot("Kevin Xie")
player3 = Bot("Knute Broady")

# creates user
print("While playing, you can use these functions: Pot, Chip count, Quit, Hand strength, and View table")
name = ask(f"What's your name?\nEnter your name here:", double_check=True)

user = User(name)



# creates the game
class Poker:
	def __init__(self):
		self.deck = []
		self.table = []
		self.turn_going = True
		self.build()
		self.blind = 1
		self.pot = 0
		self.top_contribution = 0
		self.suit_str = {1:'C', 2:"D", 3:"H", 4:"S"}
		self.num_str = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K", 14: "A"}
		self.score_str = {0: "High Card", 1: "Pair", 2: "Two Pairs", 3: "Three of a Kind", 4: "Straight", 5: "Flush", 6: "Full House", 7: "Four of a Kind", 8: "Straight Flush", 9: "Royal Flush"}

	# builds the deck
	def build(self):
		for number in range(2, 15):
			for suit in range(1, 5):
				self.deck.append((number, suit))
	# shuffles
	def shuffle(self):
		shuffled = []
		while len(self.deck) > 0:
			shuffled.append(self.deck.pop(random.randrange(0, len(self.deck))))
		self.deck = shuffled
	# gets cards our of the deck
	def get(self, num):
		to_return = []
		for x in range(0, num):
			to_return.append(self.deck.pop(-1))
		return to_return
	# deals cards to players
	def deal(self):
		for player in players:
			player.hand = self.get(2)
		print("The cards are dealt, your cards are: " + self.card_str(user.hand))
	# gets the ante from players
	def ante(self):
		print(f"{playing[-2].name} bet {self.blind} in the small blind.")
		playing[-2].bet(self.blind)
		print(f"{playing[-1].name} bet {self.blind * 2} in the big blind.")
		playing[-1].bet(self.blind * 2)
	# starts the betting round
	def action(self):
		first_round = True
		i = 0
		bet_on_table = False
		b = 0
		while first_round or bet_on_table:
			if i == len(playing) - 1:
				first_round = False
				i = -1
			player = playing[i]
			if len(playing) == 1:
				self.declare_winner()
				break
			action = player.choose_action()
			if action[0] == "Check":
				print(f"{player.name} {action[0]}s")
			if action[0] == "Fold":
				print(f"{player.name} {action[0]}s")
				playing.remove(player)
				i -= 1
			if action[0] == "Call":
				print(f"{player.name} {action[0]}s")
				player.bet(self.top_contribution - player.contribution)
			if action[0] == "Bet":
				print(f"{player.name} {action[0]}s {action[1]} chips.")
				player.bet(action[1])
				bet_on_table = True
				b = len(playing)
			if action[0] == "Raise":
				print(f"{player.name} {action[0]}s to {action[1]} chips.")
				player.bet(action[1])
				bet_on_table = True
				b = len(playing)
			if b > 0:
				b -= 1
			if b == 0:
				bet_on_table = False
			i += 1
			if len(playing) == 1:
				self.declare_winner()
				break
	# does the 'flop' (first 3 cards on the table)
	def flop(self):
		self.table = self.get(3)
		print("The flop is: ", self.card_str(self.table))
	# does the 'turn'
	def turn(self):
		self.table.append(self.deck.pop(-1))
		print("The turn is: " + self.card_str(self.table[3]))
	# does the 'river'
	def river(self):
		self.table.append(self.deck.pop(-1))
		print("The river is: " + self.card_str(self.table[4]))
	# finds the winner and awards them the pot
	def declare_winner(self):
		# if one person's left, they win
		if len(playing) == 1:
			winner = [playing[0]]
		# otherwise, go through the type of hand (pair, straight...) and the 'kicker' (extra card) until a winner or winners is/are found
		else:
			top_score = 0
			for player in playing:
				print(f"{player.name} has a {self.score_str[player.score()[0]]} with a {player.score()[1]} as a kicker and {self.card_str(player.hand)}")
				if player.score()[0] > top_score:
					top_score = player.score()[0]
			top_scores = []
			for player in playing:
				if player.score()[0] == top_score:
					top_scores.append(player)
			if len(top_scores) == 1:
				winner = top_scores
			else:
				top_kicker = 0
				for player in top_scores:
					if player.score()[1] > top_kicker:
						top_kicker = player.score()[1]
				top_kickers = []
				for player in top_scores:
					if player.score()[1] == top_kicker:
						top_kickers.append(player)
				winner = top_kickers
		# splits the pot for multiple winners
		amount = self.pot // len(winner)
		for i in winner:
			print(f"{i.name} wins {amount} chips!")
			i.chips += amount
			self.pot -= amount
		self.pot = 0
		print('\n')
		self.turn_going = False
	# turns the hand into a readable form
	def card_str(self, input):
		to_return = ""
		if type(input) == list:
			for n, s in input[:-1]:
				to_return += self.num_str[n] + self.suit_str[s] + ", "
			to_return += self.num_str[input[-1][0]] + self.suit_str[input[-1][1]]
		elif type(input) == tuple:
			to_return = self.num_str[input[0]] + self.suit_str[input[1]]
		return to_return

poker = Poker()

# goes through all the parts of a poker turn
for turn in range(0, 10):
	for i in players:
		i.hand = []
		i.contribution = 0
	players.append(players.pop(0))
	poker.table = []
	poker.deck = []
	poker.top_contribution = 0
	players = [user, player1, player2, player3]
	playing = players
	poker.turn_going = True

	poker.build()
	poker.shuffle()
	poker.deal()
	user.hand_strength()
	poker.ante()
	poker.action()
	if poker.turn_going == False:
		continue
	poker.flop()
	poker.action()
	if poker.turn_going == False:
		continue
	poker.turn()
	poker.action()
	if poker.turn_going == False:
		continue
	poker.river()
	poker.action()
	if poker.turn_going == False:
		continue
	poker.declare_winner()

