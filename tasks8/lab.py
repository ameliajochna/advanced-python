def divisors(n):
    return [i for i in range(1, n) if n % i == 0]


def prime(n):
    return [i for i in range(1, n) if len(divisors(i)) == 1]


def composite(n):
    return [i for i in range(1, n) if len(divisors(i)) > 1]


def div_sum(n):
    return sum(divisors(n))


def perfect(n):
    return [i for i in range(1, n) if div_sum(i) == i]


def deficient(n):
    return [i for i in range(1, n) if div_sum(i) < i]


def abundant(n):
    return [i for i in range(1, n) if div_sum(i) > i]


def isperfect(n):
    return div_sum(n) == n


def isdeficient(n):
    return div_sum(n) < n


def isabundant(n):
    return div_sum(n) > n


def gen_list(n, fun):
    return [i for i in range(1, n) if fun(i)]


def pythagorean_triplets(n):
    return [
        (i, j, k)
        for k in range(1, n)
        for i in range(1, n)
        for j in range(1, n)
        if i < j and i * i + j * j == k * k
    ]


def main():
    print("dzielniki 60: ", divisors(60))
    print("dzielniki 37: ", divisors(37))
    print("pierwsze mniejsze od 25: ", prime(25))
    print("zlozone mniejsze od 20", composite(20))
    print("liczby perfekcyjne do 15:", perfect(15))
    print("liczby deficytowe do 15:", deficient(15))
    print("liczby nadmiarowe do 15:", abundant(15))
    print("liczby perfekcyjne do 15:", gen_list(15, isperfect))
    print("liczby deficytowe do 15:", gen_list(15, isdeficient))
    print("liczby nadmiarowe do 15:", gen_list(15, isabundant))
    print("pitagorasowe do 30: ", pythagorean_triplets(30))


if __name__ == "__main__":
    main()
