import random

events = []
turn = 2
players = []
wrong_inputs = 0
wrong_inputs_per_turn = wrong_inputs / turn

class Poker:
	def __init__(self):
		self.deck = []
		self.table = []
		self.build()
		self.blind = 1
		self.pot = 0
		self.top_contribution = 0
		self.last_raiser = None
		self.suit_str = {1:'C', 2:"D", 3:"H", 4:"S"}
		self.num_str = {1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}
	def build(self):
		for number in range(1, 14):
			for suit in range(1, 5):
				self.deck.append((number, suit))
	def shuffle(self):
		shuffled = []
		while len(self.deck) > 0:
			shuffled.append(self.deck.pop(random.randrange(0, len(self.deck))))
		self.deck = shuffled
	def get(self, num):
		to_return = []
		for x in range(0, num):
			to_return.append(self.deck.pop(-1))
		return to_return
	def deal(self):
		for player in players:
			player.cards = self.get(2)
		print("The cards are dealt, your cards are: " + self.card_str(user.cards))
		self.action()
	def flop(self):
		self.table = self.get(3)
		print("The flop is: ", self.card_str(self.table))
		self.action()
	def turn(self):
		self.table.append(self.deck.pop(-1))
		print("The turn is: " + self.card_str(self.table[3]))
		self.action()
	def river(self):
		self.table.append(self.deck.pop(-1))
		print("The river is: " + self.card_str(self.table[4]))
		self.action()
	def ante(self):
		playing[-2].chips -= self.blind
		playing[-1].chips -= self.blind * 2
		self.pot += self.blind * 3
	def declare_winner(self):
		# winner = playing[0]
		# winner.chips += self.pot
		# self.pot = 0
		pass
	def action(self):
		# for p in playing:
		# 	choice = p.choose_action()
		# 	if choice[0] == "Fold":
		# 		playing.remove(p)
		# 		print(p.name, "folds.")
		# 	else:
		# 		bet = self.top_contribution - p.contribution
		# 		self.pot += bet
		# 		p.chips -= bet
		# 		p.contribution += bet
		# 		if choice[0] == "Call":
		# 			print(p.name, "calls.")
		# 		elif choice[0] == "Raise":
		# 			r = choice[1]
		# 			self.pot += r
		# 			p.chips -= r
		# 			print(p.name, "raises by", r, "chips.")
		# 			self.top_contribution += r
		# 			self.last_raiser = p
		pass
	def reset(self):
		playing = players
		for i in players:
			i.hand = []
		players.append(players.pop(0))
		self.table = []
		self.deck = []
		self.build()
		self.shuffle()
	def card_str(self, input):
		to_return = ""
		if type(input) == list:
			for n, s in input[:-1]:
				to_return += self.num_str[n] + self.suit_str[s] + ", "
			to_return += self.num_str[input[-1][0]] + self.suit_str[input[-1][1]]
		elif type(input) == tuple:
			to_return = self.num_str[input[0]] + self.suit_str[input[1]]
		return to_return

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []
		self.chips = 1000
		self.contribution = 0
		players.append(self)

class Bot(Player):
	def choose_action(self):
		actions = ["Fold", "Call", "Raise"]
		return random.choice(actions), random.randint(0, self.chips // 100)

class User(Player):
	def choose_action(self):
		actions = ["Fold", "Call", "Raise"]
		return random.choice(actions), random.randint(0, self.chips // 100)

class Event:
	def __init__(self, turns=None, turn_conditions=None, chance=None, comment=None):
		self.comment = comment
		self.chance = chance
		if turns == None:
			self.turns = (0, 100)
		else:
			self.turns = turns
		self.turn_conditions = turn_conditions
		events.append(self)
	def check(self):
		if self.conditions_met():
			self.run()
	def conditions_met(self):
		result = True
		if self.turns != None:
			if turn not in range(self.turns[0], self.turns[1]):
				result = False
			if self.turn_conditions != None:
				if self.turn_conditions[0] == "%":
					if turn % int(self.turn_conditions[1]) != 0:
						result = False
		if type(self.chance) == float:
			if random.randint(0, 100) > self.chance * 100:
				result = False
		return result

class Comment(Event):
	def run(self):
		print(self.comment)

class GuessingGame(Event):
	def run(self):
		low, high = 1, 10
		try:
			guess = int(input(f"Guess a number between {low} and {high}.\n>>> "))
		except ValueError:
			pass
		computer = random.randint(low, high)
		if guess == computer:
			print(f"Congratulations! You chose {guess} and it was {computer}")
		elif guess > computer:
			print(f"Sorry! You were too high, you guessed {guess} and it was {computer}")
		else:
			print(f"Sorry! You were too low, you guessed {guess} and it was {computer}")

def ask(question, options=None, double_check=False):
	asking = True
	while asking:
		answer = input(question)
		if options != None:
			if answer not in options:
				print("I'm sorry, but that's not a valid answer")
		if double_check:
			keep = input(f"You responded {answer}, do you want to keep that response?\nRespond with either Yes or No\n>>> ")
			if keep == "Yes":
				break
			elif keep != "No":
				print("This isn't rocket science, I gave you two options: Yes or No\nYet, you just refused to pick one, let's start from the top.")
				continue
		asking = False
	return answer

print("Hello and welcome to the Poker Championships!\n\nYou're carrying a bag of chips as you enter a dimly lit room with a large poker table in the center. The players look at you. \"Have a seat\" one says, you sit down and start playing.")


player1 = Bot("Daniel Heredia")
player2 = Bot("Kevin Xie")
player3 = Bot("Knute Broady")

name = ask(f"{player1.name}: I haven't seen you here before, what's your name?\nEnter your name here:\n>>> ", double_check=True)

user = User(name)

start_turn = Comment(comment="It's the start of the turn.")
every_other_turn = Comment(comment="It's an even turn.", turn_conditions="%2")
chance = Comment(comment="It's your lucky day!", chance=0.3)
guessing_game = GuessingGame()
end_turn = Comment(comment="It's the end of the turn.")
poker = Poker()

playing = players

for i in range(0, 10):
	poker.reset()
	start_turn.check()
	poker.ante()
	poker.deal()
	poker.flop()
	poker.turn()
	poker.river()
	poker.declare_winner()
	end_turn.check()
	turn += 1
