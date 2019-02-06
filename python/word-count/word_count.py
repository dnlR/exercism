import re


def word_count(phrase):
    counter = {}
    phrase = phrase.replace("_", " ")

    words = re.findall(r"\w+'\w+|\w+", phrase)
    for word in words:
        word = word.lower()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter
