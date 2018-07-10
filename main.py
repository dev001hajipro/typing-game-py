# -*- coding: utf-8 -*-
import random
import tkinter as tk
import threading

import worker


def choise_word(words: list) -> str:
    max = len(words) - 1
    rnd = random.randint(0, max)
    return words[rnd]


score = 0
remaining_sec = 60
words = [
    'apple',
    'banana',
    'cherry',
    'grape',
    'kiwi',
    'lime',
    'lemon',
    'mandarin',
    'melon',
    'orange',
    'pear',
    'persimmon',
    'plum',
    'strawberry',
    'vine',
    'watermelon'
]


root = tk.Tk()
root.title("タイピングゲーム")
root.geometry("720x360")

canvas = tk.Canvas(root, width=720, height=360, background="#fff")
textScore = canvas.create_text(
    5, 5, text=f"score:{score}", anchor="nw", font=('Courier', 12), fill="#333")
textRemainingSec = canvas.create_text(
    5, 25, text=f"time :{remaining_sec}", anchor="nw", font=('Courier', 12), fill="#333")


def resetButton_onclick():
    initData()


resetButton = tk.Button(root, text="reset", width=10,
                        command=resetButton_onclick)
resetButton.place(x=5, y=45)


def countdown(count: int):
    global remaining_sec
    remaining_sec = count


word = None
workerThread = None


def initData():
    print("init data")
    global score, remaining_sec, word, workerThread

    score = 0
    remaining_sec = 60

    word = choise_word(words)
    if workerThread != None:
        workerThread.stop()
    workerThread = worker.Worker(countdown, count=10)
    workerThread.start()


initData()

textTypingTarget = canvas.create_text(
    720/2, 360/2, text=f"{word}", font=('Consolas', 72), justify='center')

canvas.bind("<1>", lambda event: canvas.focus_set())


def hanadleKeyInput(event):
    global word, score

    if word[0] == event.char:
        word = word[1:]
        score += 1
        if len(word) == 0:
            word = choise_word(words)
    
    render()


canvas.bind("<Key>", hanadleKeyInput)
canvas.pack()
canvas.focus_set()

def render():
    canvas.itemconfigure(textTypingTarget, text=f"{word}")
    canvas.itemconfigure(textScore, text=f"score:{score}")
    canvas.itemconfigure(textRemainingSec, text=f"time :{remaining_sec}")




# refresh UI by the main thread. the remaining_sec is updated by the worker thread.
def refresher():
    render()
    root.after(1000, refresher)


refresher()
root.mainloop()
