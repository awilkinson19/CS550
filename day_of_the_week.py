import sys

day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

user_input = [int(i) for i in sys.argv[1:]]
y = user_input[2]
d = user_input[1]
m = user_input[0]

y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0  =  m  +  12  *  ((14 - m) // 12) - 2
d0 = (d + x + (31 * m0) // 12) % 7

print("...was", day[d0])
