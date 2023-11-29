x, y = 0, 0
visited = [[0, 0]]

with open("input.txt") as file:
    for char in file.readline():
        hasVisited = False

        if char == "^":
            y -= 1
        elif char == "v":
            y += 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1

        visited.append([x, y])

        # print(visited)
        # print(x, y)

fin = []
for i in visited:
    if i not in fin:
        fin.append(i)

print(len(visited), len(fin))
