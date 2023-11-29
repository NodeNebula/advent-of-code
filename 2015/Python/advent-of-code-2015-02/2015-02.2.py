total = 0

with open("input.txt") as file:
    for line in file.readlines():
        dim = line.strip().split("x")

        l, w, h = int(dim[0]), int(dim[1]), int(dim[2])

        total += l * w * h + min(2 * (l + w), 2 * (l + h), 2 * (w + h))

print(total)