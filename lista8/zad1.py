######################################
#  pol_ang.py
######################################

import random

pol_ang = {}

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue

    pol, ang = L
    if pol in pol_ang:
        pol_ang[pol].append(ang)
    else:
        pol_ang[pol] = [ang]

word_count = {}
for x in open('brown.txt'):
    for w in x.replace('\n', ' \n').replace("'", '').replace('"', '').split(' '):
        w = w.strip().lower()

        ok = False
        for c in w:
            if c >= 'a' and c <= 'z':
                ok = True

        if not ok:
            continue

        if w in word_count.keys():
            word_count[w] += 1
        else:
            word_count[w] = 1


def najpopularniejsze(slowo):
    max_cnt = 0
    for w in pol_ang[slowo]:
        if w in word_count and word_count[w] > max_cnt:
            max_cnt = word_count[w]

    max_list = []
    for w in pol_ang[slowo]:
        if w in word_count and word_count[w] == max_cnt:
            max_list += [w]

    n = random.randint(0, len(max_list) - 1)

    return max_list[n]


def tlumacz(polskie):
    wynik = []
    for p in polskie:
        if p in pol_ang:
            wynik.append(najpopularniejsze(p))
        else:
            wynik.append('[' + p + ']')
    return wynik


zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

print(' '.join(tlumacz(zdanie)))
