FILE_PATH = "../tasks6/popular_words.txt"


def get_words():
    with open(FILE_PATH, 'r') as file:
        return set(file.read().split())


def find_paired_words():
    unique_words = get_words()
    paired_words = set()

    for word in unique_words:
        reversed_word = word[::-1]
        if reversed_word in unique_words and word not in paired_words:
            paired_words.add(word)

    print(sorted(list(paired_words)))


def main():
    find_paired_words()


if __name__ == "__main__":
    main()
