def convert(number):
    raindrop_sounds = ""

    if number % 3 == 0:
        raindrop_sounds += "Pling"
    if number % 5 == 0:
        raindrop_sounds += "Plang"
    if number % 7 == 0:
        raindrop_sounds += "Plong"
    if not raindrop_sounds:
        raindrop_sounds = str(number)

    return raindrop_sounds
