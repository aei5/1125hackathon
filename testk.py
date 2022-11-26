import os
import sys
import tkinter as tk


if os.path.isdir("tes") == False:
    os.mkdir("tes")

root = tk.Tk()

# window title
root.title(u"window")

# 表示される写真
pic = tk.PhotoImage(file="./tes/IMG_6257.png", width=400, height=300)

# windows size
root.geometry('400x300')

def deleteEntry(event):
    entry.delete(0, tk.END)

def getText(event):
    with open('./tes/tes.txt','a') as saveFile:
        saveFile.write(entry.get()+"\n")

def putPicture(event):
    canvas.pack()
    canvas.create_image(0, 0, image=pic, anchor=tk.NW, tag="oval")

def erase(event):
    canvas.delete("oval")

# frontend
# label
static1 = tk.Label(text="test", foreground='#ff0000', background='#90caf9')
# これで本当にいいのか？
static1.pack()

canvas = tk.Canvas(bg="black", width=400, height=300)

# entry
entry = tk.Entry(width=50)
entry.insert(tk.END, '挿入する文字列')
entry.pack()

# button
button1 = tk.Button(text = 'input', width=30)
button1.bind('<1>', getText)
button1.bind('<3>', putPicture)
button1.pack()

button2 = tk.Button(text = 'pop', width=30)
button2.bind('<1>', erase)
button2.bind('<3>', putPicture)
button2.pack()

root.mainloop()



