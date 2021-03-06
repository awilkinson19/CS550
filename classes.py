
class Dog:

	def __init__(self, name, weight="Heavy", mood="Happy", size="Big", age=5, energy=100, hunger=100):
		self.name = name
		self.weight = weight
		self.mood = mood
		self.size = size
		self.age = age
		self.energy = energy
		self.food = food
		self.status = None

	def play(self):
		if self.energy > 10 and self.food > 2:
			self.energy -= 10
			self.food -= 2
			self.mood = "happy"
			self.status = "playing"
		else:
			self.status = f"{self.name} is too tired to play"

	def sleep(self):
		if self.energy <= 90:
			self.status = f"{self.name} is sleeping"
		else:
			self.status = f"{self.name} is too excited to sleep"

	def stats(self):
		return 	f"Name: {self.name}\nWeight: {self.weight}\nMood: {self.mood}\nSize: {self.size}\nAge: {self.age}\nEnergy: {self.energy}\nFood: {self.food}\nStatus: {self.status}"

fido = Dog("Fido")
tetris = Dog("Tetris")

while True:
	choice = input("What do you want to do?\n>>> ")
	if choice == "play":
		pass
	if choice == "sleep":
