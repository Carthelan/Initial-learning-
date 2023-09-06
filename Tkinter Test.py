from tkinter.filedialog import askopenfile
import tkinter as tk

r = tk.Tk
r.title = ('Collected range reporting')

canvas1 = tk.Canvas(r(), width=500, height=300)
canvas1.pack()

entry1 = tk.Entry()
canvas1.create_window(200, 140, window=entry1)

def fileLocationInput():
    askopenfile(mode='r', filetypes=[('any name you want to display', 'extension of file type')])

button1 = tk.Button(text='Input File Location', command=fileLocationInput)
canvas1.create_window(200, 180, window=button1)





r().mainloop()  