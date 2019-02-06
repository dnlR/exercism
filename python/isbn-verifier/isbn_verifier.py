import re


def clean_isbn(isbn: str) -> str:
    return isbn.replace("-", "")


def check_format_for_isbn(isbn: str) -> bool:
    r = re.compile("\d{9}[\d|Xx]")
    match = r.match(isbn)
    return match is not None and len(isbn) == 10


def convert_isbn_to_digits_list(isbn: str) -> [str]:
    return list(isbn)


def apply_control_digit_rule(isbn: [str]) -> [str]:
    if isbn[-1] == "X" or isbn[-1] == "x":
        isbn[-1] = 10
    return isbn


def apply_formula_to_isbn(isbn: [str]) -> bool:
    results = [int(isbn[i]) * x for i, x in zip(range(0, 10),
                                                range(10, 0, -1))]
    results = sum(results)
    return results % 11 == 0


def verify(isbn: str) -> bool:
    isbn = clean_isbn(isbn)

    if not check_format_for_isbn(isbn):
        return False

    isbn = convert_isbn_to_digits_list(isbn)
    isbn = apply_control_digit_rule(isbn)

    valid_isbn = apply_formula_to_isbn(isbn)

    return valid_isbn
