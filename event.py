from threading import Thread
from threading import Event
import time

DATA = 100


def list_data():
    for i in range(DATA + 1):
        yield i


def print_numbers(name_thred, event_even, event_odd):
    for item in generator_data:
        time.sleep(0.05)
        if item % 2 == 0:
            event_odd.wait()
            event_odd.clear()
            print("{}: {}".format(name_thred, item))
            event_even.set()
        else:
            event_even.wait()
            event_even.clear()
            print("{}: {}".format(name_thred, item))
            event_odd.set()


event_even = Event()
event_odd = Event()
generator_data = list_data()

t1 = Thread(target=print_numbers, args=("Thread-1", event_even, event_odd,))
t2 = Thread(target=print_numbers, args=("Thread-2", event_even, event_odd,))

t1.start()
time.sleep(1)
t2.start()
event_odd.set()

t1.join()
t2.join()

print("Exiting Main Thread")
