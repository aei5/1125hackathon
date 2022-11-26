import os
import sys
import tkinter as tk


if os.path.isdir("tes") == False:
    os.mkdir("tes")

root = tk.Tk()

# window title
root.title(u"window")

# 表示される写真
pic1 = tk.PhotoImage(file="./tes/IMG_6257.png", width=400, height=300)
pic2 = tk.PhotoImage(file="./tes/bird01.png", width=400, height=300)

# windows size
root.geometry('400x500')

def deleteEntry(event):
    entry.delete(0, tk.END)

def getText(event):
    with open('./tes/tes.txt','a') as saveFile:
        saveFile.write(entry.get()+"\n")

def putkaraage(event):
    canvas.create_image(0, 0, image=pic1, anchor=tk.NW, tag="oval")
def putbird(event):
    canvas.create_image(0, 0, image=pic2, anchor=tk.NW, tag="oval")

def erase(event):
    canvas.delete("oval")

# label
static1 = tk.Label(text="test", foreground='#ff0000', background='#90caf9')

# entry
entry = tk.Entry(width=50)
entry.insert(tk.END, '挿入する文字列')

# canvas
canvas = tk.Canvas(bg="black", width=400, height=300)

# button
button1 = tk.Button(text = 'input', width=30)
button1.bind('<1>', getText)
button1.bind('<3>', putkaraage)

button2 = tk.Button(text = 'pop', width=30)
button2.bind('<1>', erase)
button2.bind('<3>', putbird)

# 各ウィジェットの配置

static1.pack()
canvas.pack()
entry.pack()
button1.pack()
button2.pack()

root.mainloop()



