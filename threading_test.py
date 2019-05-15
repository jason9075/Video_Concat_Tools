import time
from threading import Thread


def my_function():
    print("thread start")
    time.sleep(1)
    raise RuntimeError
    # os._exit(1)


my_thread = Thread(target=my_function, name="myThread")
my_thread.setDaemon(True)
my_thread.start()

print("main running for 10 sec")
time.sleep(10)
print("main end")
