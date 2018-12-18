import random as r
''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
 
faveNums = [1, 2, 3]
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
 holidays = ["New Years","Christmas","July 4th","MLK Day","President's day","Holiday 6","Holiday 7", "Holiday 8","Holiday 9","Holiday 10","Holiday 11","Holiday 12","Holiday 13","Holiday 14" ]
 
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
 
grades = [i for i in 'ABCDE']
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or no t. 
'''
funny= [r.choice(True,False) for b in range(18)]

''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
 
salaries = [0.0 for i in range(numEmployees)]
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
 
value = [0 for i in range(x*y)]
 
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''

children_and_siblings = ['' for i in range(noSiblings+2*oneSibling+3*twoSiblings+4*threeSiblings)]
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
 months = ["January","Febuary","March","April","May","June","July","August","September","October","November","December" ]

 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
 
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 possible =[True,False]
 
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
 
dorms = ['Mem', 'Nichols', 'Pitman', 'Squire']
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
 a = r.randrange(0,2)
 b = r.randrange(0,2)
 c = r.randrange(0,2)

 random =[a,b,c]
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''

deck = []
for num in range(1, 14):
   for suit in ['C', 'D', 'H', 'S']:
      deck.append(str(num)+suit)
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
a = r.randrange(1,7)
b = r.randrange(1,7)
c = r.randrange(1,7)

dice =[a,b,c]

if dice[0] == dice[1] and dice[0]== dice[2] and dice[2]==dice[1]:
   print("Yahzee!")
else:
   print("Try Again")
 
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''

special = []
for i, num in enumerate(numbers):
   if num % 3 == 0:
      if numbers[i-1] % 2 == 0 and numbers[i+1] % 2 == 1:
         special.append(i)
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
 for x in range(5):
   for y in range(5):
      for a in range(5):
         saddle= True 
         if number[x][y] < number[a][y]:
            saddle = False
         break  
      for i in range(5): 
         if number[x][y] > number[x][i]:
            Saddle= False 
         break 
      if Saddle == True:
         print(x,y)
      else: 
         print("No Saddle")


 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
 
queens = [r.randrange(0, 8) for i in range(4)]
chessboard[queens[0]][queens[1]], chessboard[queens[2]][queens[3]] = 1, 1
positions = []
for a, row in enumerate(chessboard):
   for b, column in enumerate(row):
      if row == 1:
         positions.append((a, b))
attack = False
for a, b in [(0, 0), (1, 1)]
   if position[0][a] == position[1][b]:
      attack = True
if positions[0][0] - positions[1][0] == positions[0][1] - positions[1][1]:
   attack = True

''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
animals=["dog","cat"]
animals.reverse()
print(animals)
#https://stackoverflow.com/questions/13530798/python-reverse-order-of-list

''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
 
if len(doorknobs) >= 4:
   doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1] 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
largest= (max(numbers))
numbers.remove(largest)
numbers.append(largest) 
 
 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
 
two_dimensions = [[] for i in len(w)]
for i, h in enumerate(w):
   for b in h:
      if b % 2 == 1:
         if b < 10:
            two_dimensions[i].append(2)
         else:
            two_dimensions[i].append(22)
      else:
         two_dimensions[1].append(b)

 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
 
 new_two = [[] for i in range(len(two_dimensions))]
 for i, a in enumerate(two_dimensions):
   for b in a:
      new_two[i].append(255-b)
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
 
random_list = [r.randrange(0, 100) for i in range(r.randrange(10, 100))]
shifted = [random_list[i-1] for i in range(len(random_list))]
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''

count = 0
for i, a in enumerate(grid):
   for j, b in enumerate(a):
      if a[j-1] < b and a[j+1] < b and grid[i+1][j] < b and grid[i-1][j]:
         count += 1
 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
 
sum = 0
for i in list_rankings:
   sum += i
avg = sum / list_rankings
list_rankings = [i for i in list_rankings if i > avg]
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
 
 def check(putin):
   putout = True
   for i in range(1, 9):
      if i not in putin:
         putout = False
         return putout
   return putout

valid = True
for a in sudoku:
   if not check(a):
      valid = False
      break
 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
 
hundred_nums = [r.randint(1, 10) for i in range(100)]
num_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
for i in hundred_nums:
   num_dict[i] += 1
new_list = num_dict.elements()
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''
