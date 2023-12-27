import math


def czy_pierwsza(n):
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            return False
    return True


def czy_szczesliwa(liczba, cyfra, podrzad):
    if not czy_pierwsza(liczba):
        return False
    licz = 0
    for c in str(liczba):
        if int(c) == cyfra:
            licz += 1
        else:
            licz = 0
        if licz == podrzad:
            return True

    return False


def sprawdz(zakres):
    licz = 0
    for i in range(zakres + 1):
        if czy_szczesliwa(i, 4, 2):
            print(i)
            licz += 1

    print(licz)


def main():
    sprawdz(100000)


if __name__ == "__main__":
    main()
