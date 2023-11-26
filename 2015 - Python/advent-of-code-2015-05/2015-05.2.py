import re

niceCount = 0

with open("input.txt") as file:
    for line in file.readlines():
        hasPairTwoLetters = False
        hasDoubleLetterIsh = False

        for i in range(len(line) - 1):
            doubleLetter = line[i] + line[i + 1]

            if len(re.findall(doubleLetter, line)) > 1:
                hasPairTwoLetters = True
                break

        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                hasDoubleLetterIsh = True
                break

        print(line, hasPairTwoLetters, hasDoubleLetterIsh)

        if hasPairTwoLetters and hasDoubleLetterIsh:
            niceCount += 1

print(niceCount)
