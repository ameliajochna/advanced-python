from zad2 import doable, use_letters

pol_dict = {}


def make_dict():
    for x in open('popularne_slowa2023.txt'):
        x = x.strip()
        pol = x
        if pol not in pol_dict:
            pol_dict[pol] = 0


def find_puzzle(name):
    name = name.replace(' ', '').lower()
    for w in pol_dict:
        if doable(name, w):
            new_base = use_letters(name, w)
            for d in pol_dict:
                if w < d and doable(new_base, d) and use_letters(new_base, d) == '':
                    print(w, d)


make_dict()
find_puzzle('Albert Einstein')
