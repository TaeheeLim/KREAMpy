import tkinter as tk
from tkinter import *

popTitle = 'KREAM 보관판매 매크로'

window = tk.Tk()
window.title(popTitle)
window.geometry('640x400+100+100')
window.resizable(True, True)

label = tk.Label(window, text="Hello, World!")
label.pack()

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)
e6 = tk.Entry(window)
e7 = tk.Entry(window)

window.mainloop()