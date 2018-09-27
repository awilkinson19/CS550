
def bi_to_dec(bi):
	to_return = 0
	for i, num in enumerate(bi[::-1]):
		to_return += int(num) * 2 ** i
	return to_return

def rec_fib(n):
	if n == 0 or n == 1:
		return 1
	return rec_fib(n-1) + rec_fib(n-2)

def fib(n):
	a = 0
	b = 0
	c = 0
	for i in range(0, n + 1):
		if i == 0:
			a = 1
		else:
			c = a + b
		b = a
		a = c
	return a + b

print(bi_to_dec("1111"))

for x in range(0, 10):
	print(fib(x))

for x in range(0, 10):	
	print(rec_fib(x))
