from zad1 import ceasar, ALPHABET

FILE_PATH = '../tasks6/popular_words.txt'

def make_polish_dict() -> dict:
    polish_dict = {}
    with open(FILE_PATH) as f:
        content = f.read().splitlines()
        for line in content:
            polish_dict[line] = 0
    return polish_dict


def ceasar_matches(polish_dict: dict, word: str) -> list:
    matched_words = []
    for k in range(1, len(ALPHABET)):
        shifted_word = ceasar(word, k)
        if shifted_word in polish_dict.keys():
            matched_words += [shifted_word]
    return matched_words
            
    

def main() -> None:
    polish_dict = make_polish_dict()
    print(ceasar_matches(polish_dict, 'aw'))
    print(ceasar_matches(polish_dict, 'bal'))
    print(ceasar_matches(polish_dict, 'wol'))


if __name__ == '__main__':
    main()