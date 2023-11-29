import tkinter as tk
from PIL import Image, ImageTk, ImageColor


class LightContest:
    def __init__(self):
        self.grid = [[False] * 1000 for _ in range(1000)]
        self.lightsOn()

    def lightsOn(self):
        with open("input.txt") as file:
            instructions = file.readlines()

        for instruction in instructions:
            self.useInstructions(instruction)

        print("Number of lights on:", self.countLights())
        self.showLights()

    def useInstructions(self, instruction):
        words = instruction.split()
        action = words[0]

        if action == "toggle":
            start_x, start_y = map(int, words[1].split(","))
            end_x, end_y = map(int, words[3].split(","))
            self.toggleLights(start_x, start_y, end_x, end_y)
        else:
            start_x, start_y = map(int, words[2].split(","))
            end_x, end_y = map(int, words[4].split(","))

            if action == "turn":
                switch = (words[1] == "on")
                self.switchLights(start_x, start_y, end_x, end_y, switch)

    def toggleLights(self, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.grid[x][y] = not self.grid[x][y]

    def switchLights(self, start_x, start_y, end_x, end_y, switch):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.grid[x][y] = switch

    def countLights(self):
        return sum(row.count(True) for row in self.grid)

    def showLights(self):
        root = tk.Tk()
        root.title("Xmas light contest")

        canvas = tk.Canvas(root, width=1000, height=1000)
        canvas.pack()

        image = Image.new("RGB", (1000, 1000), "black")
        pixels = image.load()

        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                color = "yellow" if self.grid[x][y] else "black"
                pixels[x, y] = ImageColor.getrgb(color)

        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        root.mainloop()


LightContest()
