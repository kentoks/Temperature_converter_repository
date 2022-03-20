from tkinter import *
import random


class Converter:
    def __init__(self):
        print("hello world")

        # formatting variables...
        background_color = "light blue"

        # converter main screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color) # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        self.converter_frame.grid()

        # temperature conversion heading
        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Calibri",14,"bold"),
                                          bg=background_color,
                                          padx=10, pady=10) # remember about padx and pady

        self.temp_converter_label.grid(row=0) # what does row do again?


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
