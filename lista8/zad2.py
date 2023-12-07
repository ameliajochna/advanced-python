def make_dictionary(word):
    ans = dict()
    for c in word:
        key = c
        if key in ans.keys():
            ans.update({key: ans[key] + 1})
        else:
            ans.update({key: 1})
    return ans


def use_letters(base, word):
    b_count = make_dictionary(base)

    for c in word:
        key = c
        b_count.update({key: b_count[key] - 1})

    ans = ''
    for c in b_count.keys():
        for i in range(b_count[c]):
            ans += c

    return ans


def doable(base, word):
    b_count = make_dictionary(base)

    for c in word:
        key = c
        if key in b_count.keys() and b_count[key] > 0:
            b_count.update({key: b_count[key] - 1})
        else:
            return False
    return True


print(doable('promotion', 'nopro'))
print(doable('promotion', 'lotion'))
