import random

def create_pol_eng():
    pol_eng = {}

    with open("pol_eng.txt") as file:
        for x in file:
            x = x.strip()
            L = x.split("=")
            if len(L) != 2:
                continue

            pol, eng = L
            if pol in pol_eng:
                pol_eng[pol].append(eng)
            else:
                pol_eng[pol] = [eng]
    return pol_eng

def create_word_count():
    word_count = {}
    with open("brown.txt") as file:
        for x in file:
            for w in x.replace("\n", " \n").replace("'", "").replace('"', "").split(" "):
                w = w.strip().lower()

                ok = False
                for c in w:
                    if c >= "a" and c <= "z":
                        ok = True

                if not ok:
                    continue

                if w in word_count.keys():
                    word_count[w] += 1
                else:
                    word_count[w] = 1
    return word_count

def most_popular(word, pol_eng, word_count):
    max_cnt = 0
    for w in pol_eng[word]:
        if w in word_count and word_count[w] > max_cnt:
            max_cnt = word_count[w]

    max_list = []
    for w in pol_eng[word]:
        if w in word_count and word_count[w] == max_cnt:
            max_list += [w]

    n = random.randint(0, len(max_list) - 1)

    return max_list[n]

def translate(polish_words, pol_eng, word_count):
    result = []
    for word in polish_words:
        if word in pol_eng:
            result.append(most_popular(word, pol_eng, word_count))
        else:
            result.append("[" + word + "]")
    return result

def main():
    pol_eng = create_pol_eng()
    word_count = create_word_count()

    sentence = "chłopiec i dziewczynka pójść do sklepu".split()

    print(" ".join(translate(sentence, pol_eng, word_count)))

if __name__ == "__main__":
    main()
