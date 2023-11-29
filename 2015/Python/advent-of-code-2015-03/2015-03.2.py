xMain, yMain = 0, 0
xRobo, yRobo = 0, 0
visited = [[0, 0]]
robosTurn = False

with open("input.txt") as file:
    for char in file.readline():
        hasVisited = False

        if not robosTurn:
            if char == "^":
                yMain -= 1
            elif char == "v":
                yMain += 1
            elif char == ">":
                xMain += 1
            elif char == "<":
                xMain -= 1

            visited.append([xMain, yMain])

            robosTurn = True
        else:
            if char == "^":
                yRobo -= 1
            elif char == "v":
                yRobo += 1
            elif char == ">":
                xRobo += 1
            elif char == "<":
                xRobo -= 1

            visited.append([xRobo, yRobo])

            robosTurn = False

        # print(visited)
        # print(x, y)

fin = []
for i in visited:
    if i not in fin:
        fin.append(i)

print(len(fin))
