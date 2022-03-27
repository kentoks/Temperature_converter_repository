from tkinter import *
from functools import partial # to prevent unadditional windows from popping up
import random

class Converter:
    def __init__(self):
        # formatting variables
        background_color = "deep sky blue"


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
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font=("Arial", 14, "bold"))
        self.to_convert_entry.grid(row=2)


        # conversion button frame (row 3) # using multi colors such as
        # Orchid3 | Khaki1
        self.conversion_button_frame = Frame(self.converter_frame)
        self.conversion_button_frame.grid(row=3, pady=10)

        # celsius
        self.to_celsius_button = Button(self.conversion_button_frame,
                                        text="To Celsius", font=("Arial", 10, "bold"),
                                        bg="Khaki1", padx=10, pady=10,
                                        command=lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=0, column=0) # what is column=0? it means nothing on vertical?

        # fahrenheit
        self.to_fahrenheit_button = Button(self.conversion_button_frame,
                                           text="To Fahrenheit", font=("Arial", 10, "bold"),
                                           bg="Orchid3", padx=10, pady=10,
                                    command=lambda: self.temp_convert(-273))
        self.to_fahrenheit_button.grid(row=0, column=1) # what is row=0 mean


        # answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font=("Arial", 14, "bold"), fg="purple",
                                     bg=background_color, pady=20,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)


        # history / help button frame (row 5)
        self.history_help_frame = Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=10)

        self.calculation_history_button = Button(self.history_help_frame,
                                                 font=("Arial", 12, "bold"),
                                                 text="HELP", width=5)
        self.calculation_history_button.grid(row=0, column=1)

    def temp_convert(self, to): # what is 'to' again?
        print(to)

        # adding bg color for entries that have errors
        error = "#ffafaf" # hex code for 'pale pink', when entry box is string or error, prints this color

        # retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get() # gets the user inputs from the entry box on the converter
        # Interface/GUI

        # check that amount is valid
        try:
            to_convert = float(to_convert)


        # convert to F

        # convert to C

        # round...

        # display answer

        # add answer to list for History

        except ValueError:
            self.converted_label.configure(text="Enter a number!!!", fg="red") # Configure?
            self.to_convert_entry.configure(bg=error) # bg error color remember, 'pale pink'


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
