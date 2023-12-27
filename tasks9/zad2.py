from lista9.letters import doable, use_letters


def make_dict():
    pol_dict = {}
    for x in open("popular_words.txt"):
        x = x.strip()
        pol = x
        sorted_pol = ("").join(sorted(pol))
        if sorted_pol not in pol_dict:
            pol_dict[sorted_pol] = [pol]
        else:
            pol_dict[sorted_pol] += [pol]
    return pol_dict


def find_puzzle(pol_dict, name):
    name = name.replace(" ", "").lower()
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


def main():
    pol_dict = make_dict()
    find_puzzle(pol_dict, "Bolek i lolek")


if __name__ == "__main__":
    main()
