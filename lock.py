from threading import Lock
from threading import Thread
import time

DATA = 100


def list_data():
    for i in range(DATA + 1):
        yield i


lock = Lock()
generator_data = list_data()


def print_numbers(name_thred):
    for item in generator_data:
        time.sleep(0.1)
        lock.acquire()
        print("{}: {}".format(name_thred, item))
        lock.release()


# Create new threads
t1 = Thread(target=print_numbers, args=("Thread-1",))
t2 = Thread(target=print_numbers, args=("Thread-2",))

# Start all threads
t1.start()
t2.start()

# Start and wait for all threads to complete
t1.join()
t2.join()

print("Exiting Main Thread")
