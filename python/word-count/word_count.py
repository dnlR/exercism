import re
from string import punctuation
from collections import Counter


def count_words(sentence):
    sentence = re.sub("[,_]", " ", sentence)
    words = [word.strip(punctuation).lower() for word in sentence.split()]

    return Counter(words)
