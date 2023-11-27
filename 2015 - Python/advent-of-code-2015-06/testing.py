import tkinter as tk
from PIL import Image, ImageTk, ImageColor


class ChristmasLightsGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [[False] * size for _ in range(size)]

    def toggle_lights(self, start_x, start_y, end_x, end_y):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.grid[x][y] = not self.grid[x][y]

    def turn_off_lights(self, start_x, start_y, end_x, end_y, turn_on):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.grid[x][y] = turn_on

    def count_lit_lights(self):
        return sum(row.count(True) for row in self.grid)

    def process_instruction(self, instruction):
        words = instruction.split()
        action = words[0]

        if action == 'toggle':
            start_x, start_y = map(int, words[1].split(','))
            end_x, end_y = map(int, words[3].split(','))
            self.toggle_lights(start_x, start_y, end_x, end_y)
        else:
            start_x, start_y = map(int, words[2].split(','))
            end_x, end_y = map(int, words[4].split(','))

            if action == 'turn':
                turn_on = (words[1] == 'on')
                self.turn_off_lights(start_x, start_y, end_x, end_y, turn_on)

    def process_instructions(self, instructions):
        for instruction in instructions:
            self.process_instruction(instruction)

    def main(self):
        # Read instructions from Santa
        with open("input.txt", "r") as file:
            instructions = file.readlines()

        # Process instructions
        self.process_instructions(instructions)

        # Create and display the image
        self.display_image()

    def display_image(self):
        root = tk.Tk()
        root.title("Christmas Lights Grid")

        canvas = tk.Canvas(root, width=self.size, height=self.size)
        canvas.pack()

        image = Image.new("RGB", (self.size, self.size), "black")
        pixels = image.load()

        for x in range(self.size):
            for y in range(self.size):
                color = "yellow" if self.grid[x][y] else "black"
                pixels[x, y] = ImageColor.getrgb(color)

        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        root.mainloop()


# Example usage:
lights_grid = ChristmasLightsGrid(1000)
lights_grid.main()
