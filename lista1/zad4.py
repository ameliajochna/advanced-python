from losowanie_fragmentow import losuj_fragment


def generuj_haslo(n: int) -> str:
    if n == 0:
        return ''

    frag = losuj_fragment()
    while len(frag) > n or n - len(frag) == 1:
        frag = losuj_fragment()
    return generuj_haslo(n - len(frag)) + frag


n = 17
print(generuj_haslo(n))
