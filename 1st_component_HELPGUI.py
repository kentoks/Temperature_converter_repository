from tkinter import *
import random


class Converter:
    def __init__(self, parent): # what is parent?
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()