import tkinter as tk
from tkinter import filedialog, ttk
import os
import csv

##pythonXXX myprogram.py

window = tk.Tk()
window.title('Reporting Condenser')
window.geometry("300x200")

my_Filetypes = [('CSV Files', '.CSV')]

def locateFile():
    file = filedialog.askopenfilename(parent=window,
                                initialdir=os.getcwd(),
                                title="Only Select a CSV file:",
                                filetypes=my_Filetypes)
    if file:
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',') 
            dict = {}
            for row in reader:
                date = row[0]
                data = row[1]
                if date not in dict:
                    dict[date] = {data: 1}
                elif data not in dict[date]:
                    dict[date][data] = 1
                else: 
                    dict[date][data] += 1
            
        print(dict)  
        
browseButton = ttk.Button(window, text="Select CSV Location", command=locateFile)
browseButton.place(x=95, y=100)

instructions = tk.Label(text="1. Select CSV file to compress." + "\n" + "2. It will print to a new CSV on the desktop" + "\n" + "3. Make sure to delete the new CSV after you're finished")
instructions.pack()

window.mainloop()