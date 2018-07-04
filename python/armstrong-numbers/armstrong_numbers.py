def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    digit_count = len(digits)
    armstrong_digits = [n ** digit_count for n in digits]
    sum_digits = sum(armstrong_digits)

    return number == sum_digits

