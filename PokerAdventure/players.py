import ask as a

players = []

class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.chips = 1000
		self.contribution = 0
		players.append(self)

	def get_actions(self):
		to_return = []
		if bet_on_table:
			to_return.append("Fold")
			if self.chips >= bet:
				to_return.append("Call")
				if self.chips > bet * 2:
					to_return.append("Raise")
			to_return.append("All-In")
		else:
			to_return.append("Check")
			to_return.append("Bet")
			to_return.append("All-In")
			return to_return

	def strength(self):
		hand = table + self.hand
		return s.score(hand)

	def bet(self, amount):
		self.chips -= amount
		poker.pot += amount
		if bet_on_table == False:
			bet_on_table == True
			bet = amount
		if bet_on_table == True:
			if bet < amount:
				bet += amount

class Bot(Player):
	def choose_action(self):
		actions = self.get_actions()
		return random.choice(actions), random.randint(0, self.chips // 100)

class User(Player):
	def choose_action(self):
		options = self.get_actions()
		action = ask(f"What do you want to do?\nYour options are: {options}\n>>> ", options=options)
		if action == "Raise":
			value = ask("Write the amount you want to raise by:\n>>> ", option_type=int)
		else:
			value = 0
		return action, value

player1 = Bot("Daniel Heredia")
player2 = Bot("Kevin Xie")
player3 = Bot("Knute Broady")

name = a.ask(f"{player1.name}: I haven't seen you here before, what's your name?\nEnter your name here:", double_check=True)

user = User(name)
