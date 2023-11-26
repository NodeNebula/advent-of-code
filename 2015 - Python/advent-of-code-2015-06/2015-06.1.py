import tkinter as tk


class LightContest:
    def __init__(this, test):
        this.test = test

        this.getInput(open("input.txt"))

    def getInput(this, file):
        print(file.readline())


root = tk.Tk()
root.title("Advent of Code 2015 - Challenge 6 part 1")
root.geometry("1000x1000")
LightContest("test")

root.mainloop()
