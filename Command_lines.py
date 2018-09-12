import sys
# Got help from: https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
'''
1: What is the value at position 0?
Position 0 is the first item
2: How can you tell how many arguments have been passed?
Use the function len()
3: What happens if you pass more arguments or fewer arguments than the program expects?
it returns an error
'''
x = [print("Hello, "+i+"!") for i in sys.argv[1:]]
