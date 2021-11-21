import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))
    
root = tk.Tk()
root.geometry("480x480")
tk.Label(root, text="Your Expression:").pack()
entry = tk.Entry(root)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(root)
res.pack()
root.mainloop()