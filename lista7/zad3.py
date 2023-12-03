FILE_PATH = 'popularne_slowa2023.txt'


def get_words():
    f = open(FILE_PATH)
    return dict.fromkeys(f.read().split())


def longest_seg_without_polish_chars(text, polish_words):
    cur_seg = ''
    longest_seg = ''
    polish_chars = set('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ')
    text = text.replace('\n', ' ').split(' ')

    for word in text:
        if len(longest_seg) < len(cur_seg):
            longest_seg = cur_seg
            print(cur_seg, '\n')

        word_ok = True
        only_letters = ''
        for char in word:
            if char in polish_chars:
                word_ok = False
            if (char > 'a' and char < 'z') or (char > 'A' and char < 'Z'):
                only_letters += char

        if only_letters not in polish_words:
            word_ok = False

        if not word_ok:
            cur_seg = ''
        else:
            cur_seg += word + ' '

    if len(longest_seg) < len(cur_seg):
        longest_seg = cur_seg
        if cur_seg not in longest_seg:
            print(
                'NOWY ',
            )

    return longest_seg


def read_file(path, polish_words):
    with open(path, encoding='utf-8') as file:
        content = file.read()
        print(longest_seg_without_polish_chars(content, polish_words))


read_file('lalka.txt', get_words())
