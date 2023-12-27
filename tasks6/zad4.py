def divide(s):
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


sentence = "This is an example sentence."
result = divide(sentence)
print(result)
