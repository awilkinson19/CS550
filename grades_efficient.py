import sys
'''
Sept. 17 2018
This uses as few comparisons as possible to determine the grade
'''
try:
	grade = float(sys.argv[1])
	if 0 <= grade <= 5:
		if grade >= 3.5:
			if grade >= 4.5:
				if grade >= 4.7:
					if grade >= 4.85:
						letter = "A+"
					else:
						letter = "A"
				else:
					letter = "A-"
			elif grade >= 3.85:
				if grade >= 4.2:
					letter = "B+"
				else:
					letter = "B"
			else:
				letter = "B-"
		else:
			if grade >= 2.5:
				if grade >= 2.85:
					if grade >= 3.2:
						letter = "C+"
					else:
						letter = "C"
				else:
					letter = "C-"
			elif grade >= 1.5:
				if grade >= 2:
					letter = "D+"
				else:
					letter = "D"
			else:
				letter = "F"
		print(f"The grade {grade} is a {letter}.")
except ValueError:
	print("Next time, input a number from 0 to 5.")
