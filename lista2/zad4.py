from duze_cyfry import daj_cyfre


def scal_cyfry(liczba, cyfra):
    for i in range(len(liczba)):
        liczba[i] += ' ' + cyfra[i]
    return liczba


liczby_str = '21345'
liczby = []
for l in liczby_str:
    liczby.append(int(l))

wynik = daj_cyfre(liczby[0])
for i in range(1, len(liczby)):
    wynik = scal_cyfry(wynik, daj_cyfre(liczby[i]))

for w in wynik:
    print(w)
