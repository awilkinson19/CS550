import random

low, high = 1, 10

def play():
	guess = int(input(f"Guess a number between {low} and {high}.\n>>> "))
	computer = random.randint(low, high)
	if guess == computer:
		print(f"Congratulations! You chose {guess} and it was {computer}")
	elif guess > computer:
		print(f"Sorry! You were too high, you guessed {guess} and it was {computer}")
	else:
		print(f"Sorry! You were too low, you guessed {guess} and it was {computer}")
	again = input("Do you want to play again? (Y/N)\n>>> ")
	if again == "Y" or again == "y":
		play()

play()
