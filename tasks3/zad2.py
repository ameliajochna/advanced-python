import math


def czy_pierwsza(n):
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            return False
    return True


def sprawdz(numbers):
    licz = 0
    all = []
    for num in numbers:
        if czy_pierwsza(num):
            all.append(num)
        licz += int(czy_pierwsza(num))
    print(all)
    return licz


def generuj_liczby(dlugosc, cyfra, podrzad):
    podstawa = str(cyfra) * podrzad
    liczby = []
    pozostalo = dlugosc - podrzad + 1
    for liczba in range(0, 10**pozostalo):
        strliczba = str(liczba)
        if len(str(liczba)) != pozostalo:
            strliczba = "0" * (pozostalo - len(strliczba)) + str(liczba)

        for pt in range(len(strliczba) + 1):
            l1 = strliczba[0:pt]
            l2 = strliczba[pt:]
            nowaliczba = int(l1 + podstawa + l2)
            if len(str(nowaliczba)) == dlugosc + 1:
                liczby.append(nowaliczba)

    liczby = list(dict.fromkeys(liczby))
    return liczby


def main():
    print(sprawdz(generuj_liczby(9, 7, 7)))


if __name__ == "__main__":
    main()
