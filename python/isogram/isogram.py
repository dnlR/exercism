from string import ascii_lowercase


def is_isogram(string: str):
    string = string.lower()
    for c in ascii_lowercase:
        if 1 < string.count(c):
            return False
    return True
