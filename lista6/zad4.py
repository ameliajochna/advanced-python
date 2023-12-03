def podziel(s):
    s += ' '
    arr = []
    cur_word = ''
    for c in s:
        if c == ' ':
            if cur_word != '':
                arr.append(cur_word)
                cur_word = ''
        else:
            cur_word += c

    return arr
