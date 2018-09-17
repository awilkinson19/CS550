import sys

grade = float(sys.argv[1])
if grade >= 3.5:
	if grade >= 4.7:
		if grade >= 4.85:
			letter = "A+"
		else:
			letter = "A"
	else:
		letter = "A-"

	if grade >= 3.85:
		if grade >= 4.2:
			letter = "B+"
		else:
			letter = "B"
	else:
		letter = "B-"
else:
	if grade >= 2.85:
		if grade >= 3.2:
			letter = "C+"
		else:
			letter = "C"
	else:
		letter = "C-"

	if grade >= 1.5:
		if grade >= 2:
			letter = "D+"
		else:
			letter = "D"
	else:
		if grade >= 1:
			letter = "D-"
		else:
			letter = "F"
print(f"The grade {grade} is a {letter}.")
