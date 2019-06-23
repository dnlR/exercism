from string import ascii_lowercase


def is_pangram(sentence):
    sentence = sentence.lower()
    checks = [(letter in sentence) for letter in ascii_lowercase]
    return all(checks)
