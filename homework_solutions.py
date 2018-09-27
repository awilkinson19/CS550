import random
'''
Generate  a  list  of  10  random  numbers  between  0  and  100.  Get  them  inorder  from  largest  to  smallest,  removing  numbers  divisible  by  3.  (Ms.  Healey)
'''
def problem_one():
	solution = []
	for i in range(10):
		solution.append(random.randint(0, 100))
	for i in solution:
		if i % 3 == 0:
			solution.remove(i)
	solution.sort()
	return f"Problem one: {solution}"
'''
Generate  a  list  of  100  numbers,  1  to  100,  without  using  a  traditional  looping  technique  (investigate  list  comprehensions).  Shuffle  the  list  up  so  the  numbers  are  not  in  order.  (Ms.  Healey)
'''
def problem_two():
	temp, solution = [i for i in range(1, 101)], []
	while len(temp) != 0:
		solution.append(temp.pop(random.randrange(0, len(temp))))
	return f"Problem two: {solution}"
'''
Create  a  list  of  15  random  numbers  from  0-100.  Ask  the  user  for  one  input  from  0-100.  Append  this  input  to  the  list.  Sort  the  list  into  descending  order.  (Anjali,  Sonali,  Mia)
'''
def problem_three():
	solution = [random.randint(0, 100) for i in range(15)]
	getting_input = True
	while getting_input:
		try:
			user_input = int(input("Add something to the list from 0 to 100.\n>>> "))
			if not 0 <= user_input <= 100:
				print("Try again.")
			else:
				getting_input = False
		except ValueError:
			print("Try again.")
	solution.append(user_input)
	solution.sort()
	return f"Problem three: {solution[::-1]}"
'''
The  task  is  to  eliminate  all  strings  that  include  the  letter  "a"  in  the  list.  For  example,  if  you  have  [Afeifj,  bsfkd,  lksjdflkjds,  aiowerf],  then  your  program  should  print  out  [bsfkd,  lksjdflkjds]  (Leo,  Ryan,  Roshni)
'''
def problem_four(user_input):
	return f"Problem four: {[i for i in user_input if 'a' not in i]}"
'''
Allow  10  random  integers  to  be  entered  as  arguments.  Catch  any  potential  errors.  Print  them  sorted  from  small  to  large,  then  large  to  small,  and  then  print  the  sum.  (Kevin,  Knute,  Mitchell?) 
'''
def problem_five():
	undefined = True
	while undefined:
		try:
			user_input = input("Enter ten integers separated by a space:\n>>> ")
			user_input = user_input.split(' ')
			user_input = [int(i) for i in user_input]
			if len(user_input) == 10:
				undefined = False
			else:
				print("You didn't follow directions, try again.")
		except ValueError:
			print("You didn't follow directions, try again.")
	user_input.sort()
	return f"Problem five: {user_input, user_input[::-1]}" # ascending, descending

print(problem_one())
print(problem_two())
print(problem_three())
print(problem_four(input("List here: ").split(' ')))
print(problem_five())
