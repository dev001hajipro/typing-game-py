# -*- coding: utf-8 -*-
"""
JavaScriptのsetIntervalのように一定間隔で処理をしたい場合に使う。
一定間隔で関数を呼ぶワーカースレッド。カウントダウンタイマーなどに使う
"""

import threading
import time
import datetime


class Worker(threading.Thread):
    """一定間隔で関数を呼ぶワーカースレッド。カウントダウンタイマーなどに使う"""

    def __init__(self, fn, count=0):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = count
        self.fn = fn

    def run(self):
        while self.count >= 0 and not self.event.is_set():
            # print(f"timerスレッド:{threading.current_thread().ident},count={self.count}")
            self.fn(self.count)
            self.count -= 1
            self.event.wait(1)

    def stop(self):
        self.event.set()


if __name__ == '__main__':
    None
