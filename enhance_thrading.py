import sys
import threading
import queue
import time


class ExcThread(threading.Thread):

    def __init__(self, bucket):
        threading.Thread.__init__(self)
        self.bucket = bucket

    def run(self):
        try:
            time.sleep(5)
            raise Exception('5 sec later, An error occured here.')
        except Exception:
            self.bucket.put(sys.exc_info())


def main():
    bucket = queue.Queue()
    thread_obj = ExcThread(bucket)
    thread_obj.start()
    print("main start")

    while True:
        print("main keep going")

        try:
            exc = bucket.get(block=False)
        except queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print(exc_type, exc_obj)
            print(exc_trace)

        thread_obj.join(0.1)
        if thread_obj.isAlive():
            continue
        else:
            break


if __name__ == '__main__':
    main()
