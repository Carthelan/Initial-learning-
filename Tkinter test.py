import tkinter as tk
from tkinter import Button, filedialog
import os

##figure out how to designate a python distro to make the program use

window = tk.Tk()
window.title('Reporting Condenser')
window.geometry("300x300")

my_Filetypes = [('CSV Files', '.CSV')]

def locateFile():
    file = filedialog.askopenfilename(parent=window,
                                initialdir=os.getcwd(),
                                title="Please select a file:",
                                filetypes=my_Filetypes)
    if file:
        filepath = os.path.abspath(file.name)
        tk.Label(str(filepath)).pack()
browseButton = Button (window, text="Browse", command=locateFile)
browseButton.pack()

instructions = tk.Label(text="Select CSV file to compress")
instructions.pack()


window.mainloop()