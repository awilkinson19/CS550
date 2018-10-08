import minesweeper
import printing as p

'''
October 8 2018
by Alex Wilkinson
Healey CS550

On my honor, I have neither given nor received unauthorized aid.
'''

# This file runs the code, minesweeper.py contains the main code for the game and printing.py contains the code for user inputs

# Purely for debugging, anything starting with if testing is for debugging
testing = True

# Runs code
playing = True
while playing:
	# Plat one round
	minesweeper.play()
	# Ask the player if it wants to play again, if the answer is no then stop playing
	playing = p.ask("Do you want to continue playing?", boolean=True)
