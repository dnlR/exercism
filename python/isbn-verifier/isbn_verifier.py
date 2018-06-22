import re


def verify(isbn):
    r = re.compile("\d-\d{3}-\d{5}-[\d|Xx]|\d{9}[\d|Xx]")
    match = r.match(isbn)
    if match is None:
        return False

    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    isbn_digits = list(isbn)
    if isbn_digits[-1] == "X" or isbn_digits[-1] == "x":
        isbn_digits[-1] = 10

    results = [int(isbn_digits[i]) * x for i, x in zip(range(0, 10),
                                                       range(10, 0, -1))]

    return sum(results) % 11 == 0
