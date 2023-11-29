def decode_unicode_escape(line):
    decoded = bytes(line, 'utf-8').decode('unicode-escape')
    return decoded


def getOutput():
    char_diff = 0

    with open("input.txt") as file:
        for line in file:
            in_memory = decode_unicode_escape(line)

            char_diff += len(line) - len(in_memory) + 2

    return char_diff


print(getOutput())
