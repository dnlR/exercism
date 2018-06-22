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

    isbn_digits = [int(digit) for digit in isbn_digits]

    result = (isbn_digits[0] * 10 + \
            isbn_digits[1] * 9 + \
            isbn_digits[2] * 8 + \
            isbn_digits[3] * 7 + \
            isbn_digits[4] * 6 + \
            isbn_digits[5] * 5 + \
            isbn_digits[6] * 4 + \
            isbn_digits[7] * 3 + \
            isbn_digits[8] * 2 + \
            isbn_digits[9] * 1) % 11

    return result == 0


if __name__ == '__main__':
    print(verify('3-598-21508-8'))
    print(verify('3-598-21507-X'))
    print(verify('3598215088'))
    print(verify('359821507X'))
