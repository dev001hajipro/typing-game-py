# -*- coding: utf-8 -*-


import random
import sys
import tkinter
import threading
import datetime

import worker


def choise_word(words: list) -> str:
    max = len(words) - 1
    rnd = random.randint(0, max)
    return words[rnd]


def main(words: list) -> None:
    for _ in range(50):
        word = choise_word(words)
        print(f"{word} ", end='')
    print('')


def button1_onclick(event):
    print(event.x, event.y)
    label1.configure(text="ogggg")
    workerThread.stop()


root = tkinter.Tk()
label1 = tkinter.Label(text="hello")


def task_hello():
    print(f"\t hello task: {datetime.datetime.now()}")
    label1.configure(text=f"\t hello task: {datetime.datetime.now()}")


workerThread = worker.Worker(task_hello, count=10)

if __name__ == '__main__':

    workerThread.start()

    words = [
        'apple',
        'banana',
        'grape',
        'melon',
        'orange',
    ]
    # main(words)
    # print("abcde"[1:])
    # UI
    root.title("タイピングゲーム")
    root.geometry("720x360")

    label1.pack()

    label2 = tkinter.Label(text="hello2")
    label2.pack()

    button1 = tkinter.Button(text="button1")
    button1.bind("<Button-1>", button1_onclick)
    button1.pack()

    root.mainloop()
