import string


def is_isogram(input):
    letter_count = {c: 0 for c in string.ascii_lowercase}

    for letter in input.lower():
        if letter in string.ascii_lowercase:
            letter_count[letter] += 1

    return max(letter_count.values()) in [0, 1]


def is_isogram(string):
    sanitized_string = string.lower().replace(' ', '').replace('-', '')
    return len(sanitized_string) == len(set(sanitized_string))
