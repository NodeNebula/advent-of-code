import tkinter as tk
from tkinter import Canvas, Button
from PIL import Image, ImageDraw, ImageTk  # Import ImageTk


class PixelArtApp:
    def __init__(this, master, width, height):
        this.master = master
        this.master.title("Pixel Art Editor")

        # Create a blank image with a white background
        this.image = Image.new("RGB", (width, height), "blue")
        this.draw = ImageDraw.Draw(this.image)

        # Create a canvas to display the image
        this.canvas = Canvas(this.master, width=width, height=height, bg="white")
        this.canvas.pack()

        # Create a button to set a pixel to black
        this.black_button = Button(this.master, text="Set to Black", command=this.set_pixel_black)
        this.black_button.pack()

        # Create a button to set a pixel to white
        this.white_button = Button(this.master, text="Set to White", command=this.set_pixel_white)
        this.white_button.pack()

    def set_pixel_black(self):
        x, y = 2, 2  # Set coordinates based on your requirements
        self.draw.point((x, y), fill="black")
        self.update_canvas()

    def set_pixel_white(self):
        x, y = 2, 2  # Set coordinates based on your requirements
        self.draw.point((x, y), fill="white")
        self.update_canvas()

    def update_canvas(self):
        # Convert the Pillow image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(self.image)

        # Update the canvas with the new image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # To prevent garbage collection


root = tk.Tk()
app = PixelArtApp(root, width=300, height=300)
root.mainloop()
