import unicodedata

ALPHABET = unicodedata.normalize('NFC', 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż')

def get_position(char: str) -> int:
    char = char.lower()

    return ALPHABET.find(char)


def ceasar(s: str, k: int) -> str:
    s = unicodedata.normalize('NFC', s)
    k = k % (len(ALPHABET))
    encrypted = ''

    for char in s:
        pos = get_position(char)
        new_char = ALPHABET[(pos + k) % (len(ALPHABET))]

        if char.isupper():
            new_char = new_char.upper()
            
        encrypted += new_char
    
    return encrypted


def main() -> None:
    print(ceasar(u'aąbcćdeęfghijklłmnńoóprsśtuwyzźż', 5))


if __name__ == '__main__':
    main()