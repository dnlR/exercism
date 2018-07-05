import string


def rotate(text, key):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    shifted_alphabet_lower = alphabet_lower[key:] + alphabet_lower[:key]
    shifted_alphabet_upper = alphabet_upper[key:] + alphabet_upper[:key]
    alphabet = alphabet_lower + alphabet_upper
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)
