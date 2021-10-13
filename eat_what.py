from functools import wraps
import random
import tkinter as tk
from tkinter import font
from tkinter.constants import NONE, WORD
import tkinter.messagebox as tkmsg
import time

# function


def decide(type):
    f = open(type, encoding="utf-8")
    text = f.read().splitlines()
    f.close()
    # 在字串中加入變數 使用format在後面補述中間的各變數為何
    msg = '吃\b{name}\b吧!'.format(name=random.choice(text))
    time.sleep(1)
    #tkmsg.askretrycancel(title="Answer!!!!!", message=msg)
    l1 = tk.Label(text=msg, font=('標楷體', 15, 'bold'),
                  bg='yellow', width=15, height=3)
    l1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


window = tk.Tk()  # 開視窗
window.title("EAT WHAT!!!!!")  # 視窗名稱
window.geometry("600x300+700+250")  # 視窗大小
btn1 = tk.Button(window, text='午餐',
                 command=lambda: decide('lunch.txt'), height=5, width=15, font=20)  # 作動按鈕
btn2 = tk.Button(window, text='晚餐', command=lambda: decide(
    'dinner.txt'), height=5, width=15, font=20)

btn1.place(relx=0.35, rely=0.5, anchor=tk.CENTER)  # 按鈕排版
btn2.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
window.mainloop()
