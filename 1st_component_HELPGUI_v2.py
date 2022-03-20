from tkinter import *



class Converter:
    def __init__(self):
        print("hello world")

        # formatting variables...
        background_color = "light blue"

        # converter main screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10) # allows help button sizes at bottom to change
        # can use height=300, width=30,
        # but can be deleted, so the text can fit in the box
        # remember what Frame is
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
        # get_help = Help()
        # get_help.help_text.configure(text="Help text goes here") # what does it do?



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
