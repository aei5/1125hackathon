import tkinter as tk
import sys

root = tk.Tk()

root.geometry("300x200")

m = input()

static = tk.Label(text=m)
static.pack()

root.mainloop()
