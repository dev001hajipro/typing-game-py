# -*- coding: utf-8 -*-
import unittest
import worker

test_count = 0


def task_hello(count):
    global test_count
    test_count += 1


class TestWorker(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, 1)
        
    def test_run_worker(self):
        workerThread = worker.Worker(task_hello, count=1)
        workerThread.start()
        workerThread.join()
        self.assertEqual(2, test_count)


if __name__ == '__main__':
    unittest.main()
