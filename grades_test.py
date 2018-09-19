import sys

x = float(sys.argv[1])
grade = ["F", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
value = [0, 1.5, 2, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85, 5]
y = 0
z = False

if x >= 5 or x <= 0:
    print("Invalid input!")

while not value[y] < x < value[y+1]:
	print(y, grade[y])
	y = y + 1
	print(y, value[y])
	if value[y] < x < value[y+1]:
		print("Your grade is " + str(grade[y]))
		break
