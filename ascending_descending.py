import sys

user_input = [float(i) for i in sys.argv[1:]]

def is_ascending_or_descending(x):
	is_ascending = True
	previous = x[0]
	for i in x[1:]:
		if i < previous:
			is_ascending = False
			break
		previous = i
	is_descending = True
	for i in x[1:]:
		if i > previous:
			is_descending = False
			break
		previous = i
	if is_ascending or is_descending:
		return True

if is_ascending_or_descending(user_input):
	print("True")
else:
	print("False")
