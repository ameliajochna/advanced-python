def make_dictionary(word):
    ans = dict()
    for c in word:
        key = c
        if key in ans:
            ans[key] = ans[key] + 1
        else:
            ans[key] = 1
    return ans


def use_letters(base, word):
    with_letters_count = make_dictionary(base)

    for c in word:
        key = c
        with_letters_count[key] -= 1

    ans = ""
    for c, count in with_letters_count.items():
        ans += c * count

    return ans


def doable(base, word):
    with_letters_count = make_dictionary(base)

    for c in word:
        key = c
        if key in with_letters_count and with_letters_count[key] > 0:
            with_letters_count[key] -= 1
        else:
            return False
    return True


def main():
    print(doable("promotion", "nopro"))
    print(doable("promotion", "lotion"))


if __name__ == "__main__":
    main()
