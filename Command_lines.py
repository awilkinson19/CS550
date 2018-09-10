import sys

# Got help from: https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments

user_input = sys.argv
path = user_input.pop(0)
x = [print("Hello, "+i+"!") for i in user_input]
