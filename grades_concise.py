import sys
'''
Sept. 17 2018
This tries to be as concise as possible
'''
top, grades = 0, {4.85:"A+",4.7:"A",4.5:"A-",4.2:"B+",3.85:"B",3.5:"B-",3.2:"C+",2.85:"C",2.5:"C-",2:"D+",1.5:"D",0:"F"}
try:
	grade = float(sys.argv[1])
	print(f"The grade {grade} is a {grades[[i for i in grades if grade >= i][-1]]}.")
except ValueError:
	print("Next time, input a number from 0 to 5.")
