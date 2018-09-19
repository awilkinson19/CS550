import random as r

deck = []
playing = []
table = []
revealed = []
numbers = {}
suits = {}

class Deck:
	def __init__(self):
		self.deck = []
	def build(self):
		for number in range(1, 14):
			numbers[number] = 0
			for suit in range(1, 5):
				suits[suit] = 0
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
			print("get")
	def set(self):
		self.build()
		self.shuffle()
	def deal(self, players):
		for player in playing:
			player.get(2)
	def flop(self):
		table = self.get(3)


class Player:
	def __init__(self, name):
		self.name = name
		self.hand = []
	def set(self):
		self.numbers = numbers
		self.suits = suits
	def playing(self):
		playing.append(self)
	def get(self, num):
		self.hand = deck.get(num)
		print("get", num)
	def strength(self):
		sum = 0
		for n, s in self.hand:
			sum += n
		return sum

Heredia = Player("Heredia")
Heredia.playing()
You = Player("You")
You.playing()

deck = Deck()
deck.set()
deck.deal(playing)

print(playing)
for i in playing:
	print(i.hand)





