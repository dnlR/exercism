import re
from functools import reduce


def abbreviate(words):
    words = re.sub('[-_]', ' ', words)

    acronym = reduce(lambda acc, word: acc + word[0].upper(), words.split(), '')
    # acronym = ''.join([word[0].upper() for word in words.split()])

    return acronym
