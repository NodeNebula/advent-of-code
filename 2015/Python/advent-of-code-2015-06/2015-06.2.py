class LightContest:
    def __init__(self):
        self.grid = [[0] * 1000 for _ in range(1000)]
        self.levels = 0
        self.lightsOn()

        print(self.countLevels())

    def lightsOn(self):
        with open("input.txt") as file:
            instructions = file.readlines()

        for instruction in instructions:
            self.useInstructions(instruction)

    def useInstructions(self, instruction):
        words = instruction.split()

        if words[0] == "toggle":
            start_x, start_y = map(int, words[1].split(","))
            end_x, end_y = map(int, words[3].split(","))
            self.notToggleButMore(start_x, start_y, end_x, end_y)
        else:
            start_x, start_y = map(int, words[2].split(","))
            end_x, end_y = map(int, words[4].split(","))

            if words[0] == "turn":
                switch = (words[1] == "on")
                self.lightDimming(start_x, start_y, end_x, end_y, switch)

    def notToggleButMore(self, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.grid[x][y] += 2

    def lightDimming(self, start_x, start_y, end_x, end_y, switch):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if switch:
                    self.grid[x][y] += 1
                else:
                    self.grid[x][y] -= 1
                    if self.grid[x][y] < 0:
                        self.grid[x][y] += 1

    def countLevels(self):
        for x in range(1000):
            for y in range(1000):
                self.levels += self.grid[x][y]

        return self.levels


LightContest()
