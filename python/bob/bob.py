import re


def hey(phrase):
    phrase = re.sub('[\s+]', '', phrase)
    if phrase.isupper() and phrase.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase.endswith('?'):
        return "Sure."
    elif not phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."
