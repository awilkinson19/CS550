
def Person:

	def __init__(self, name, hunger, energy, sleep):
		self.name = name
		self.hunger = hunger
		self.energy = energy
		self.sleep = sleep
		self.status = ""

	def status_set(self, status):
		self.status = f"{self.name} is {status}."

	def sleep(self, hours):
		self.sleep = hours*10
		self.status_set("sleeping")

	def run(self, minutes):
		self.energy -= 1 * minutes
		self.hunger += 0.75 * minutes
		self.status_set("running")

	def talk(self, minutes):
		self.energy += 0.5 * minutes
		self.status_set("talking with friends")

while True:
	choice = input("What would you like to do?\n>>> ")
	if choice == "sleep":
		pass