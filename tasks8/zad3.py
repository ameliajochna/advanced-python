from zad2 import doable, use_letters


def make_dict():
    pol_dict = {}
    for x in open("popular_words.txt"):
        x = x.strip()
        pol = x
        if pol not in pol_dict:
            pol_dict[pol] = 0
    return pol_dict


def find_puzzle(name, pol_dict):
    name = name.replace(" ", "").lower()
    for w in pol_dict:
        if doable(name, w):
            new_base = use_letters(name, w)
            for d in pol_dict:
                if w < d and doable(new_base, d) and use_letters(new_base, d) == "":
                    print(w, d)


def main():
    pol_dict = make_dict()
    find_puzzle("Albert Einstein", pol_dict)


if __name__ == "__main__":
    main()
