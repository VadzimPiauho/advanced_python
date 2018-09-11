from threading import Semaphore
from threading import Thread
import time

DATA = 100


def list_data():
    for i in range(DATA + 1):
        yield i


def print_numbers(name_thred, semaphore_even, semaphore_odd):
    for item in generator_data:
        time.sleep(0.05)
        if item % 2 == 0:
            semaphore_even.acquire()
            print("{}: {}".format(name_thred, item))
            semaphore_odd.release()
        else:
            semaphore_odd.acquire()
            print("{}: {}".format(name_thred, item))
            semaphore_even.release()


semaphore_even = Semaphore(1)
semaphore_odd = Semaphore(0)
generator_data = list_data()

t1 = Thread(target=print_numbers, args=("Thread-1", semaphore_even, semaphore_odd))    # noqa
t2 = Thread(target=print_numbers, args=("Thread-2", semaphore_even, semaphore_odd))    # noqa

t1.start()
t2.start()

t1.join()
t2.join()

print("Exiting Main Thread")
