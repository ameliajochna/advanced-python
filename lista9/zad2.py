from lista8zad2 import doable, use_letters

pol_dict = {}


def make_dict():
    for x in open('popularne_slowa2023.txt'):
        x = x.strip()
        pol = x
        sorted_pol = ('').join(sorted(pol))
        if pol not in pol_dict:
            pol_dict[sorted_pol] = pol


def find_puzzle(name):
    name = name.replace(' ', '').lower()
    for w in pol_dict:
        word1 = pol_dict[w]
        if doable(name, word1):
            new_base = use_letters(name, word1)
            for d in pol_dict:
                word2 = pol_dict[d]
                if word1 < word2 and doable(new_base, word2):
                    last_word = use_letters(new_base, word2)
                    if last_word in pol_dict:
                        print(word1, word2, pol_dict[last_word])


make_dict()
find_puzzle('Bolek i lolek')
