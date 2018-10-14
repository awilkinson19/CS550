
def gcd(a, b):
	if a < b:
		a, b = b, a
	while a >= b:
		a -= b
		if a == 0:
			return a
	a, b = b, a
	gcd(a, b)

print(gcd(1071, 462))

