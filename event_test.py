import random

events = []
turn = 2
playing = []
players = []
table = []
wrong_inputs = 0
wrong_inputs_per_turn = wrong_inputs / turn
name = input("What's your name?")
suit_str = {1:'-8o', 2:"<3", 3:"<>", 4:"<3-"}
num_str = {1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}

class Poker:
	def __init__(self):
		self.deck = []
		self.build()
		print(len(self.deck))
	def build(self):
		for number in range(1, 14):
			for suit in range(1, 5):
				self.deck.append((number, suit))
	def shuffle(self):
		shuffled = []
		while len(self.deck) > 0:
			shuffled.append(self.deck.pop(r.randrange(0, len(self.deck))))
		self.deck = shuffled
	def get(self, num):
		to_return = []
		for x in range(0, num):
			to_return.append(self.deck.pop(-1))
	def deal(self):
		for player in players:
			player.cards = self.get(2)
		print("The cards are dealt, your cards are:", user.cards)
		self.action()
	def flop(self):
		table = self.get(3)
		print("The flop is: ", table)
		self.action()
	def turn(self):
		table.append(self.deck.pop(-1))
		print("The turn is: ", table)
		self.action()
	def river(self):
		table.append(self.deck.pop(-1))
		print("The river is: ", table)
		self.action()
	def declare_winner(self):
		pass
	def action(self):
		pass

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = []
		players.append(self)

class User(Player):
	pass

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

user = User(name)
player1 = Player("Daniel Heredia")
player2 = Player("Kevin Xie")
player3 = Player("Knute Broady")

start_turn = Comment(comment="It's the start of the turn.")
every_other_turn = Comment(comment="It's an even turn.", turn_conditions="%2")
chance = Comment(comment="It's your lucky day!", chance=0.3)
guessing_game = GuessingGame()
end_turn = Comment(comment="It's the end of the turn.")
poker = Poker()

for i in range(0, 10):
	start_turn.check()
	poker.deal()
	poker.flop()
	poker.turn()
	poker.river()
	poker.declare_winner()
	end_turn.check()
	turn += 1
