from zad2 import doable, use_letters


def make_dict():
    pol_dict = {}
    with open("../tasks6/popular_words.txt") as file:
        for line in file:
            word = line.strip()
            if word not in pol_dict:
                pol_dict[word] = 0
    return pol_dict


def find_puzzle(name, pol_dict):
    name = name.replace(" ", "").lower()
    for word in pol_dict:
        if doable(name, word):
            new_base = use_letters(name, word)
            for other_word in pol_dict:
                if all(
                    [
                        word < other_word,
                        doable(new_base, other_word),
                        use_letters(new_base, other_word) == "",
                    ]
                ):
                    print(word, other_word)


def main():
    pol_dict = make_dict()
    find_puzzle("Albert Einstein", pol_dict)


if __name__ == "__main__":
    main()
