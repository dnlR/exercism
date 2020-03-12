def score(word):
    points = 0
    for letter in word.upper():
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            points += 1
        elif letter in ['D', 'G']:
            points += 2
        elif letter in ['B', 'C', 'M', 'P']:
            points += 3
        elif letter in ['F', 'H', 'V', 'W', 'Y']:
            points += 4
        elif letter in ['K']:
            points += 5
        elif letter in ['J', 'X']:
            points += 8
        elif letter in ['Q', 'Z']:
            points += 10

    return points
