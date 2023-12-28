def divide(s: str) -> list:
    words = []
    current_word = ""

    for char in s:
        if char.isspace():
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    return words


def main() -> None:
    sentence = "This is an example sentence."
    result = divide(sentence)
    print(result)


if __name__ == "__main__":
    main()
