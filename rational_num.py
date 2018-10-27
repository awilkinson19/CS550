testing = False

class Fraction:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		self.simplify()
		return Fraction(n, d)

	def __sub__(self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d
		self.simplify()
		return Fraction(n, d)

	def __mul__(self, other):
		n = self.n * other.n
		d = self.d * other.d
		self.simplify()
		return Fraction(n, d)

	def __truediv__(self, other):
		n = self.n * other.d
		d = self.d * other.n
		self.simplify()
		return Fraction(n, d)

	def __str__(self):
		return str(self.n)+'/'+str(self.d)

	def factor(self):
		n_fac = [i for i in range(2, int(self.n//2)) if self.n % i == 0]+[self.n]
		d_fac = [i for i in range(2, int(self.d//2)) if self.d % i == 0]+[self.d]
		if testing:
			print(n_fac, d_fac)
		common_fac = []
		for i in n_fac:
			if i in d_fac:
				common_fac.append(i)
		if testing:
			print(common_fac)
		return n_fac, d_fac, common_fac

	def simplify(self):
		common_fac = self.factor()[2]
		if common_fac == []:
			return self.n, self.d
		self.n /= common_fac[-1]
		self.d /= common_fac[-1]
		self.n = int(self.n)
		self.d = int(self.d)
		if testing:
			print(self.n, self.d)
		self.simplify()


	__repr__ = __str__

def main():
	a = Fraction(2, 10)
	b = Fraction(1, 3)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2

c = Fraction(8, 64)
c.simplify()
print(c)
main()





