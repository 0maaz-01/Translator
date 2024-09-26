# pip install googletrans==3.1.0a0, Install this version for running the code
# This Translator will only run if your system is connected to the internet.

# Importing everything from the tkinter module
from tkinter import *
# Importing Translator and LANGUAGES from googletrans module
from googletrans import Translator, LANGUAGES

# Coverting the input text into the selected language
def conversion(text, froml, to):
    # We are making an object of the Translator class that is present in the googletrans module
    trans = Translator()
    # Translate is a function present in the Translator Class that receives source text (src) and convert it into destination text (dest)
    trans1 = trans.translate(text,src= froml,dest = to)
    # Returning the converted text to the position where the function was called from.
    return trans1.text

# Getting the input text and the selected languages
def get_details():
    # Getting the language of input text and storing it into lan1 (a variable)
    lan1 = variable.get()
    # Getting the language of output text and storing it into lan1 (a variable)
    lan2 = variable2.get()
    # Getting the input text present on the first entry box and storing it into lan1 (a variable)
    msg = entry.get(1.0, END)
    # Calling the conversion function so that we can pass the arguements -- message, input language, output language
    textget = conversion(msg, lan1, lan2)
    # Deleting all the text present in the output window, if in case user has typed something on the result window
    result.delete(1.0, END)
    # Inserting the converted text to the output window
    result.insert(END, textget)


# Creating a window
window = Tk()
# Setting the title of the window
window.title("Translator")
# Setting the size of the window
window.geometry("600x700")
# Setting the background of the window
window.config(bg = "black")
# Window size can't be adjusted
window.resizable(False, False)

# Creating the Title present inside the window
title = Label(window, text = "Translator", font = ("Aerial",30, "bold"), background="orange", foreground="black", width = 25)
title.place(x=0,y=35)

# Creating a frame inside the window that will hold all buttons, entry window, result window
frame = Frame(window).pack(side = BOTTOM)

# Creating the entry window inside the frame that will take the input text
entry = Text(frame, font = ("Aerial", 20, "bold"), wrap = WORD, background="#6330ff", foreground="white")  # words ko wrap karne ke liye ya fir words ko alag alag karne ke liye
entry.place(x = 20, y = 120, width = 560 ,height = 200)

# Importing the languages from the google module, LANGUAGES.keys() contains code for language and for this reason it is not important
list_text = list(LANGUAGES.values())

# Creating variables that will hold colors.
colour_bg1 = "orange"
colour_fg1 = "black"

colour_bg2 = "#ffc87c"
colour_fg2 = "BLACK"


# To get the selected languages
variable = StringVar()
variable.set("english")

# Creating the first dropdown menu inside the frame
select_option = OptionMenu(frame, variable, *list_text)

#  Customizing the appearance of the dropdown menu and placing it on the window
select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                     font=("Aerial", 20, "bold"), pady=20, indicatoron=0)

select_option.place(x = 20, y = 340, height = 55, width = 180)

# Customizing the appearance of the options present in the dropdown menu
select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                             activeforeground=colour_fg2, font=("Aerial", 20, "bold"), border=0)

# 2nd dropdown menu
variable2 = StringVar()
variable2.set("hindi")

select_option1 = OptionMenu(frame, variable2, *list_text)


select_option1.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                     font=("Aerial", 20, "bold"), pady=20, indicatoron=0)

select_option1.place(x = 400, y = 340, height = 55, width = 180)

select_option1["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                             activeforeground=colour_fg2, font=("Aerial", 20, "bold"), border=0)

# Translate Button
button = Button(frame, text = "Translate",font=("Aerial", 20, "bold"), compound = "center", relief = RAISED, command = get_details, background = "orange", borderwidth = 10, foreground="black", activebackground = "#ffc87c", activeforeground = "black")
button.place(x = 225,y = 340, height = 55, width = 150)

# Output Window
result = Text(frame, font = ("Aerial", 20, "bold"), wrap = WORD, foreground="white", background="#6330ff")  # words ko wrap karne ke liye ya fir words ko alag alag karne ke liye
result.place(x = 20, y = 415, width = 560 ,height = 200)

window.mainloop()