def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
