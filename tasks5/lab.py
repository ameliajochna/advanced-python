def single_diamond(height, word):
    arr = []
    for i in range(1, height + 1, 2):
        cur_arr = []
        for j in range((height - i) // 2):
            cur_arr += [" "]
        for j in range(i):
            cur_arr += [word[j % (len(word))]]
        for j in range((height - i) // 2):
            cur_arr += [" "]
        cur_arr += [" "]
        arr += [cur_arr]

    for i in range(height - 2, 0, -2):
        cur_arr = []
        for j in range((height - i) // 2):
            cur_arr += [" "]
        for j in range(i):
            cur_arr += [word[j % (len(word))]]
        for j in range((height - i) // 2):
            cur_arr += [" "]
        cur_arr += [" "]
        arr += [cur_arr]

    return arr


def merge(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3 += [arr1[i] + arr2[i]]
    return arr3


def word_diamonds(height, sentence):
    result = []
    for w in sentence:
        if result == []:
            result = single_diamond(height, w)
        else:
            result = merge(result, single_diamond(height, w))

    for w in result:
        for x in w:
            print(x, end="")
        print(" ")


def character_diamonds(height, count, char):
    arr = []
    for _ in range(count):
        arr += [char]
    word_diamonds(height, arr)


def main():
    word_diamonds(11, ["diamond", "d", "word"])

    character_diamonds(11, 4, "*")


if __name__ == "__main__":
    main()
