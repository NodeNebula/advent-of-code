floor = 0

with open("input.txt") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

print(floor)
