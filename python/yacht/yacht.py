# Score categories
# Change the values as you see fit
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice, category):
    if category == YACHT:
        return yacht(dice)
    elif category == ONES:
        return category_number(dice, 1)
    elif category == TWOS:
        return category_number(dice, 2)
    elif category == THREES:
        return category_number(dice, 3)
    elif category == FOURS:
        return category_number(dice, 4)
    elif category == FIVES:
        return category_number(dice, 5)
    elif category == SIXES:
        return category_number(dice, 6)
    elif category == FULL_HOUSE:
        if four_of_a_kind(dice) == 0 and \
                little_straight(dice) == 0 and \
                big_straight(dice) == 0 and \
                yacht(dice) == 0 and \
                not check_double_pair(dice):
            return full_house(dice)
        else:
            return 0
    elif category == CHOICE:
        return choice(dice)
    elif category == FOUR_OF_A_KIND:
        return four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return little_straight(dice)
    elif category == BIG_STRAIGHT:
        return big_straight(dice)


def check_double_pair(dice):
    counter = dict((x, dice.count(x)) for x in set(dice))
    pair_count = 0
    for key in counter:
        if counter[key] == 2:
            pair_count += 1

    return pair_count == 2


def yacht(dice):
    if dice.count(dice[0]) == len(dice):
        return 50
    else:
        return 0


def category_number(dice, number):
    occurrences = dice.count(number)
    if occurrences == 0:
        return 0
    else:
        return number * occurrences


def choice(dice):
    return sum(dice)


def full_house(dice):
    return sum(dice)


def four_of_a_kind(dice):
    counter = dict((x, dice.count(x)) for x in set(dice))
    for key in counter:
        if counter[key] == 4 or counter[key] == 5:
            return key * 4
    return 0


def little_straight(dice):
    if sum(dice) == sum([1, 2, 3, 4, 5]):
        return 30
    else:
        return 0


def big_straight(dice):
    if sum(dice) == sum([2, 3, 4, 5, 6]):
        return 30
    else:
        return 0
