#!usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import schedule
import time
import datetime
import tkinter as tk
import random


def massage_pop():
    root = tk.Tk()
    root.title("まごころ")
    root.geometry("300x200")
    with open("./tes/tes.txt","r") as saveFile:
        lines = saveFile.readlines()
        s_lines = [line.strip() for line in lines]
        num = random.randrange(len(s_lines))
        print(num)
        #for line in s_lines:
            #static = tk.Label(text=line)
        static = tk.Label(text=s_lines[num])
        static.pack()
    root.mainloop()

schedule.every(5).seconds.do(massage_pop)  # 関数job1を、2秒毎に実行する
#schedule.every(1).minutes.do(job2)  # 関数job2を、1分毎に実行する

schedule.every().minutes.at(":23").do(massage_pop)  # 関数job3を、毎23秒に実行する

print("start",datetime.datetime.now())


while True:
    schedule.run_pending()
    time.sleep(1)
