import players as p

players = p.players
bet_on_table = False
bet = 0
user = p.user
table = []

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
		self.num_str = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K", 14: "A"}
		self.strength_str = {1:"High Card", 2:"Pair", 2:"Two Pairs", 3:"Straight", 4:"Flush", 5:"Full House", 6:"Four of a Kind", 7:"Straight Flush", 8:"Royal Straight"}

	def build(self):
		for number in range(2, 15):
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
		playing[-2].bet(self.blind)
		playing[-1].bet(self.blind * 2)

	def declare_winner(self, hands):
		pass

	def action(self):
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
		bet_on_table = False

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

