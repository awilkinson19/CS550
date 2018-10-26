
class Account:

	def __init__(self, number, PIN=None, balance=0):
		self.number = number
		self.PIN = PIN
		self.balance = balance
		self.status = ""

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.status = None
		else:
			self.status = "You need to deposit a positive number."

	def withdraw(self, amount):
		if amount > 0:
			if self.amount < self.balance:
				self.balance -= amount
				self.status = None
			else:
				self.status = f"You can only withdraw {self.balance}."
		else:
			self.status = "You need to withdraw a positive number."

	def transfer(self, amount, other_account):
		if amount > 0:
			if self.amount < self.balance:
				other_account.balance += amount
				self.balance -= amount
				self.status = None
			else:
				self.status = f"You can only withdraw {self.balance}."
		else:
			self.status = "You need to transfer a positive number."

	def stats(self):
		to_return = ""
		to_return += f"Balance: {self.balance}\n"
		return to_return

one = Account(1)

one.PIN = int(input("Enter your PIN value here: "))
one.balance = int(input("Enter your starting balance here: "))

options = ["depositDeposit", "withdrawWithdraw", "Quitquit"]
while True:
	if int(input("Enter your PIN please: ")) == one.PIN:
		choice = input("What action do you want to take?\n>>> ")
		if choice in options[0]:
			amount = float(input("How much do you want to deposit?\n>>> "))
			one.deposit(amount)
			if one.status != None:
				print(one.status)
		elif choice in options[1]:
			amount = float(input("How much do you want to withdraw?\n>>> "))
			one.withdraw(amount)
			if one.status != None:
				print(one.status)
		elif choice in options[-1]:
			choice = input("Do you want to quit this program?\n>>> ")
			if choice in "Yesyes":
				quit()
		else:
			print("Please enter your PIN and choose an action or quit the program by typing 'quit'.")
	else:
		print("You entered your PIN incorrectly, Please enter your PIN and choose an action or quit the program by typing 'quit'.")
	print(one.stats())
