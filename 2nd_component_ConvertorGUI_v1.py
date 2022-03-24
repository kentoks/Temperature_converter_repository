from tkinter import *
from functools import partial # to prevent unadditional windows from popping up
import random

class Converter:
    def __init__(self):
        # formatting variables
        background_color = "light blue"


        # converter frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()


        # temperature converter heading (row 0)
        self.temperature_heading_label = Label(self.converter_frame,
                                               text="Temperature Converter",
                                               font=("Arial", 16, "bold"),
                                               bg=background_color,
                                               padx=5, pady=25)
        self.temperature_heading_label.grid(row=0)


        # user instructions (row 1)
        self.temperature_instruction_label = Label(self.converter_frame,
                                               text="Type in the amount to convert your preferred "
                                                    "temperature, and then push the one of the "
                                                    "buttons below...",
                                               font=("Arial", 10, "italic"), wrap=250,
                                               justify=LEFT, bg=background_color, padx=10,
                                               pady=10)
        self.temperature_instruction_label.grid(row=1)

        # temperature entry box (row 2)

        # conversion button frame (row 3)

        # answer label (row 4)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
