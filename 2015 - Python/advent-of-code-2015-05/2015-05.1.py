niceCount = 0
vowels = ["a", "e", "i", "o", "u"]
blacklist = ["ab", "cd", "pq", "xy"]

with open("input.txt") as file:
    for line in file.readlines():
        hasMinimumVowel = False
        hasDoubleLetter = False
        hasBlackListed = False

        vowelCount = 0

        for i in range(len(vowels)):
            vowelCount += line.count(vowels[i])

        if vowelCount >= 3:
            hasMinimumVowel = True

        doubleLetterCheck = [*line]
        for i in range(len(doubleLetterCheck) - 1):
            if doubleLetterCheck[i] == doubleLetterCheck[i + 1]:
                hasDoubleLetter = True

        # Blacklisted character combo check
        for i in range(len(blacklist)):
            if blacklist[i] in line:
                hasBlackListed = True

        if hasMinimumVowel and hasDoubleLetter and not hasBlackListed:
            niceCount += 1

        if not hasMinimumVowel:
            print("doesn't reach minimal vowel count")
        if not hasDoubleLetter:
            print("doesn't have double letter")
        if hasBlackListed:
            print("has blacklisted letters")

print(niceCount)

