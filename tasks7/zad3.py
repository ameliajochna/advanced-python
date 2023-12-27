FILE_PATH = "../tasks6/popular_words.txt"


def get_words():
    with open(FILE_PATH, encoding="utf-8") as f:
        return set(f.read().split())


def contains_polish_chars(word):
    polish_chars = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
    return any(char in polish_chars for char in word)


def longest_seg_without_polish_chars(text, polish_words):
    cur_seg = ""
    longest_seg = ""

    for word in text.split():
        if len(longest_seg) < len(cur_seg):
            longest_seg = cur_seg

        if contains_polish_chars(word) or word.lower() not in polish_words:
            cur_seg = ""
        else:
            cur_seg += word + " "

    if len(longest_seg) < len(cur_seg):
        longest_seg = cur_seg

    return longest_seg


def read_file(path, polish_words):
    with open(path, encoding="utf-8") as file:
        content = file.read()
        print(longest_seg_without_polish_chars(content, polish_words))


def main():
    polish_words = get_words()
    read_file("lalka.txt", polish_words)


if __name__ == "__main__":
    main()
