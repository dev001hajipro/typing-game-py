# -*- coding: utf-8 -*-
import random
import tkinter
import threading

import worker

def choise_word(words: list) -> str:
    max = len(words) - 1
    rnd = random.randint(0, max)
    return words[rnd]

score = 0
remaining_sec = 10
words = [
    'apple',
    'banana',
    'grape',
    'melon',
    'orange',
]


root = tkinter.Tk()
root.title("タイピングゲーム")
root.geometry("720x360")

canvas = tkinter.Canvas(root, width=720, height=360, background="#fff")
textScore = canvas.create_text(
    5, 5, text=f"score:{score}", anchor="nw", font=('Courier', 12), fill="#333")
textRemainingSec = canvas.create_text(
    5, 25, text=f"time :{remaining_sec}", anchor="nw", font=('Courier', 12), fill="#333")


def countdown(count :int):
    global remaining_sec
    remaining_sec = count


word = None
workerThread = None


def initData():
    global word, workerThread

    word = choise_word(words)
    workerThread = worker.Worker(countdown, count=10)
    workerThread.start()


initData()

textTypingTarget = canvas.create_text(
    720/2, 360/2, text=f"{word}", font=('Consolas', 72), justify='center')

canvas.bind("<1>", lambda event: canvas.focus_set())


def hanadleKeyInput(event):
    global word, score
    word = word[1:]
    if len(word) == 0:
        word = choise_word(words)
    score += 1
    # update ui
    canvas.itemconfigure(textTypingTarget, text=f"{word}")
    canvas.itemconfigure(textScore, text=f"score:{score}")


canvas.bind("<Key>", hanadleKeyInput)
canvas.pack()
canvas.focus_set()


# refresh UI by the main thread. the remaining_sec is updated by the worker thread.
def refresher():
    print("called refresher")
    canvas.itemconfigure(textRemainingSec, text=f"score:{remaining_sec}")
    root.after(1000, refresher)


refresher()
root.mainloop()
