from tkinter import *
from functools import partial # to prevent unwanted windows
# functools prevent multiple instances from occuring, such as having multiple 'help' tabs


class Converter:
    def __init__(self):

        # formatting variables...
        background_color = "light blue"

        # converter main screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10) # allows help button sizes at bottom to change
        # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        # remember what Frame is...
        self.converter_frame.grid()

        # temperature conversion heading
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Calibri",18,"bold"),
                                          bg=background_color,
                                          padx=10, pady=10)

        self.temp_converter_label.grid(row=0)

        # help button (row 1)
        self.help_button = Button(self.converter_frame, text="HELP",
                                  font=("Calibri", 14,),
                                  padx=10, pady=5, command=self.help)
        self.help_button.grid(row=1)


    def help(self):
        print("You have asked for help?")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here") # what does it do?


class Help:
    def __init__(self, partner): # what is partner?
        background = "orange"

        # disable 'help' button
        partner.help_button.config(state=DISABLED) # what does state mean?

        # sets up child window (ie: help box)
        self.help_box = Toplevel() # what is toplevel()

        # sets up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # sets up help heading (row 0) (1st row)
        self.how_heading = Label(self.help_frame, text="Help/instructions",
                                 font=("Calibri", 12, "bold"), bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1) (2nd row)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        # what is wrap and what is justify, think...
        self.help_text.grid(row=1)

        # dismiss button (row 2) (3rd row)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10,
                                     bg="orange", font=("Calibri", 12, "bold"),
                                     command=self.close_help)
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy() # remember about destroy() which is just closing the box

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
