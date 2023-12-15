class fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + '/' + str(self.b)

    def euklid_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def reduce(self):
        gcd = fraction.euklid_gcd(self.a, self.b)
        return fraction(int(self.a / gcd), int(self.b / gcd))

    def __add__(self, x):
        return fraction.reduce(fraction(self.a * x.b + self.b * x.a, self.b * x.b))

    def __sub__(self, x):
        return self + fraction(-x.a, x.b)

    def __mul__(self, x):
        return fraction.reduce(fraction(self.a * x.a, self.b * x.b))

    def __truediv__(self, x):
        return self * fraction(x.b, x.a)


print(fraction(1, 2) + fraction(1, 3))
print(fraction(2, 3) + fraction(1, 3))
print(fraction(3, 4) * fraction(1, 3))
print(fraction(5, 1) / fraction(10, 1))
