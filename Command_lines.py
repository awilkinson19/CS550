import sys

user_input = sys.argv
path = user_input.pop(0)
x = [print("Hello, "+i+"!") for i in user_input]
