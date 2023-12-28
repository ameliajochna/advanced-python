class Fraction:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"{self.a}/{self.b}"

    @staticmethod
    def euclid_gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    def reduce(self) -> "Fraction":
        gcd = self.euclid_gcd(self.a, self.b)
        return Fraction(self.a // gcd, self.b // gcd)

    def __add__(self, x: "Fraction") -> "Fraction":
        return (self + x).reduce()

    def __sub__(self, x: "Fraction") -> "Fraction":
        return (self - x).reduce()

    def __mul__(self, x: "Fraction") -> "Fraction":
        return (self * x).reduce()

    def __truediv__(self, x: "Fraction") -> "Fraction":
        return (self / x).reduce()


def main() -> None:
    print(Fraction(1, 2) + Fraction(1, 3))
    print(Fraction(2, 3) + Fraction(1, 3))
    print(Fraction(3, 4) * Fraction(1, 3))
    print(Fraction(5, 1) / Fraction(10, 1))


if __name__ == "__main__":
    main()
