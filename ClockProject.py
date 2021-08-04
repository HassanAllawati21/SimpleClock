from tkinter import *
from tkinter.ttk import *

from time import strftime

root1 = Tk()
root1.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root1, font=("Old London", 150), background = "black", foreground = "gold")
label.pack(anchor='center')
time()

mainloop()