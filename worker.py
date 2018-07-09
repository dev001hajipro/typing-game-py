import threading
import time
import datetime


class Worker(threading.Thread):
    def __init__(self, fn, count=0):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = count
        self.fn = fn

    def run(self):
        while self.count > 0 and not self.event.is_set():
            # print(f"timerスレッド:{threading.current_thread().ident},count={self.count}")
            self.fn()
            self.count -= 1
            self.event.wait(1)

    def stop(self):
        self.event.set()


if __name__ == '__main__':

    def task_hello():
        print(f"\t hello task: {datetime.datetime.now()}")

    print(f"mainスレッド:{threading.current_thread().ident}, 開始")

    workerThread = Worker(task_hello, count=10)
    workerThread.start()

    # メインスレッドが先に終わらないようにする場合は、joinを使えばよい
    workerThread.join()

    # workerThread.stop()

    print(f"mainスレッド:{threading.current_thread().ident}, 終了")
