from lista8zad2 import doable, use_letters

pol_dict = {}


def make_dict():
    for x in open('popularne_slowa2023.txt'):
        x = x.strip()
        pol = x
        sorted_pol = ('').join(sorted(pol))
        if sorted_pol not in pol_dict:
            pol_dict[sorted_pol] = [pol]
        else:
            pol_dict[sorted_pol] += [pol]


def find_puzzle(name):
    name = name.replace(' ', '').lower()
    for w in pol_dict:
        if doable(name, w):
            new_base = use_letters(name, w)
            for d in pol_dict:
                if doable(new_base, d):
                    last_word = use_letters(new_base, d)
                    if last_word in pol_dict:
                        for w1 in pol_dict[w]:
                            for d1 in pol_dict[d]:
                                for l2 in pol_dict[last_word]:
                                    if w1 < d1 and d1 < l2:
                                        print(w1, d1, l2)


make_dict()
find_puzzle('Bolek i lolek')
