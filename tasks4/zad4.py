def erastotenes(max_n, prime):
    prime[0] = False
    prime[1] = False
    for i in range(2, max_n):
        if prime[i]:
            for k in range(2, (max_n + 1) // i):
                prime[k * i] = False


def czy_palindrom(n):
    rev_n = str(n)[::-1]
    return str(n) == rev_n


def palindromy(a, b, prime, max_n):
    licz = 0
    for i in range(a, b + 1):
        licz += int(prime[i] and czy_palindrom(i))
        if prime[i] and czy_palindrom(i):
            print(i)

    return licz


def main():
    max_n = 1001
    prime = [True] * max_n
    erastotenes(max_n, prime)
    palindromy(0, 1000, prime, max_n)


if __name__ == '__main__':
    main()
