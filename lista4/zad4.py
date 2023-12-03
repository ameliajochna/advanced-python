MAXN = 1001
PRIME = [True] * MAXN


def erastotenes():
    PRIME[0] = False
    PRIME[1] = False
    for i in range(2, MAXN):
        if PRIME[i]:
            for k in range(2, (MAXN + 1) // i):
                PRIME[k * i] = False


def czy_palindrom(n):
    rev_n = str(n)[::-1]
    return str(n) == rev_n


def palindromy(a, b):
    licz = 0
    for i in range(a, b + 1):
        licz += int(PRIME[i] and czy_palindrom(i))
        if PRIME[i] and czy_palindrom(i):
            print(i)

    return licz


erastotenes()
palindromy(0, 1000)
