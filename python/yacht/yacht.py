# Score categories
# Change the values as you see fit
from collections import Counter

ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL HOUSE"
FOUR_OF_A_KIND = "FOUR OF A KIND"
LITTLE_STRAIGHT = "LITTLE STRAIGHT"
BIG_STRAIGHT = "BIG STRAIGHT"
CHOICE = "CHOICE"
YACHT = "YACHT"


def score(dice, category):
    if category == ONES:
        return sum_equals(dice, 1)
    elif category == TWOS:
        return sum_equals(dice, 2)
    elif category == THREES:
        return sum_equals(dice, 3)
    elif category == FOURS:
        return sum_equals(dice, 4)
    elif category == FIVES:
        return sum_equals(dice, 5)
    elif category == SIXES:
        return sum_equals(dice, 6)
    elif category == YACHT:
        return yacht(dice)
    elif category == FULL_HOUSE:
        return full_house(dice)
    elif category == CHOICE:
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        return four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return little_straight(dice)
    elif category == BIG_STRAIGHT:
        return big_straight(dice)


def yacht(dice):
    if len(set(dice)) == 1:
        return 50
    return 0


def sum_equals(dice, number):
    occurrences = dice.count(number)
    if 0 < occurrences:
        return number * occurrences
    return 0


def full_house(dice):
    counter = Counter(dice)
    values = list(counter.values())
    values.sort()
    if values == [2, 3]:
        return sum(dice)
    return 0


def four_of_a_kind(dice):
    counter = dict((x, dice.count(x)) for x in set(dice))
    for key in counter:
        if 4 <= counter[key]:
            return key * 4
    return 0


def little_straight(dice):
    if sum(dice) == sum([1, 2, 3, 4, 5]):
        return 30
    return 0


def big_straight(dice):
    if sum(dice) == sum([2, 3, 4, 5, 6]):
        return 30
    return 0
