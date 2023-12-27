from lista1.generate_fragments import generate_fragment


def generuj_haslo(n: int) -> str:
    if n == 0:
        return ''

    frag = generate_fragment()
    while len(frag) > n or n - len(frag) == 1:
        frag = generate_fragment()
    return generuj_haslo(n - len(frag)) + frag


def main():
    n = 17
    print(generuj_haslo(n))


if __name__ == '__main__':
    main()
