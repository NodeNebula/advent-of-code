def decode_unicode_escape(line):
    decoded = line.encode('unicode-escape').decode('utf-8')

    return decoded


def getOutput():
    char_diff = 0

    with (open("input.txt") as file):
        for line in file:
            in_memory = decode_unicode_escape(line.strip())

            char_diff += len(in_memory) + 2 - len(line.strip())

            print(len(in_memory), in_memory, " - ", len(line), line.strip())

    return char_diff


print(getOutput())
