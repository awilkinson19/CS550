import sys
import math

P = int(sys.argv[1])
r = float(sys.argv[2])
t = int(sys.argv[3])

print(P * math.e ** (r * t))