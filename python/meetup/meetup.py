import datetime


class MeetupDayException(Exception):
    pass


day_week_to_digit = {"monday": 0,
                     "tuesday": 1,
                     "wednesday": 2,
                     "thursday": 3,
                     "friday": 4,
                     "saturday": 5,
                     "sunday": 6}

descriptors = {"1st": 1,
               "2nd": 2,
               "3rd": 3,
               "4th": 4,
               "5th": 5,
               "teenth": 13}

first_to_fifth = ["1st", "2nd", "3rd", "4th", "5th"]
one_day = 1


def meetup_day(year, month, day_of_the_week, which):
    day_of_the_week = day_of_the_week.lower()
    descriptor = which.lower()

    if descriptor in first_to_fifth:
        day_occurrences = 0
        d = datetime.date(year, month, 1)
        while day_occurrences < descriptors[descriptor]:
            if d.weekday() == day_week_to_digit[day_of_the_week]:
                day_occurrences += 1
            if day_occurrences < descriptors[descriptor]:
                tmp_d = d + datetime.timedelta(one_day)
                if d.month == tmp_d.month:
                    d = tmp_d
                else:
                    raise MeetupDayException(f"There is no "
                                             f"{descriptor}{day_of_the_week} "
                                             f"in {d.month}")
        return d
    elif descriptor == "teenth":
        d = datetime.date(year, month, descriptors[descriptor])
        while d.weekday() != day_week_to_digit[day_of_the_week]:
            d += datetime.timedelta(one_day)
        return d
    elif descriptor == "last":
        d = datetime.date(year, month, 1)
        d += datetime.timedelta(32)
        d = d.replace(day=1)
        d -= datetime.timedelta(one_day)
        while d.weekday() != day_week_to_digit[day_of_the_week]:
            d -= datetime.timedelta(one_day)
        return d
