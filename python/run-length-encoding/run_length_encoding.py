def decode(string):
    decoded_str = ""
    char_count = ""

    for char in string:
        if char.isdigit():
            char_count += char
            continue
        else:
            if char_count and 1 < int(char_count):
                decoded_str += char * int(char_count)
            else:
                decoded_str += char
            char_count = ""

    return decoded_str


def encode(string):
    char_count = 0
    encoded_str = ""

    for idx, char in enumerate(string):
        char_count += 1
        if idx + 1 == len(string) or char != string[idx + 1]:
            encoded_str += str(char_count) + char if 1 < char_count else char
            char_count = 0

    return encoded_str
