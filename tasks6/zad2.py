FILE_PATH = "./popular_words.txt"


def get_words():
    f = open(FILE_PATH)
    return dict.fromkeys(f.read().split())


def find_paired_words():
    ans = []
    arr = get_words()
    for word in arr:
        reversed_word = word[::-1]
        if reversed_word in arr:
            if word not in ans:
                ans.append(word)

    print(sorted(ans))


def main():
    find_paired_words()


if __name__ == "__main__":
    main()
