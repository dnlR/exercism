import string


def rotate(text, key):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet + alphabet.upper(),
                          shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)
