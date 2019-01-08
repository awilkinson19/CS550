'''
You are a game show contestant. There are three boxes in front of you to choose from, 2 of which hold pennies and one of which holds keys to a brand new car!! You will play by first picking a box at random. The host will then reveal pennies in one of the doors you didn't choose. Then, when there are 2 options left, you can choose to switch your chosen box, if you want, before your prize is revealed.

Before coding a simulation, consider whether you think it is better to switch your chosen box or not, or if it even matters. Write your thoughts down in comments at the top of your program.

Then, code a simulation that runs 1000 times, where you don't switch your choice. How many times do you win the car?

Next, code a variation on the simulation where you always switch your choice, and run it 1000 times. How many times do you win the car?

Explain the results of this simulation in the comments at the bottom of your code. What is happening? Is this what you expected? At this point, you may look up the Monty Hall simulation if you need some help understanding this. 

Put your code on github, and submit a link to your code here on Canvas.
'''
import random as r

def montyhall(switch):
	car = r.randrange(3)
	# Don't need to randomize choice, because the car is randomized
	choice = 2
	if choice == car:
		revealed = r.randrange(2)
	else:
		# this works because car will always be 1 or 0 if it's not choice
		revealed = 1 - car
	result = choice == car
	if switch:
		return not result
	return result

def run(switch, num):
	result = {True:0, False:0}
	for i in range(num):
		result[montyhall(switch)] += 1
	return result[True], result[False]

no_switch = run(False, 1000)
switch = run(True, 1000)
print(f"Switch: {switch}\nNo Switch: {no_switch}")

'''
every time, switching wins 2/3 and not switching wins 1/3.

I saw explanations for this problem before, so it is what I expected.
If the car is placed behind one of the doors I didn't pick (2/3 chance), then I'm going to win if I switch because the revealed door never has a car behind it.
'''







