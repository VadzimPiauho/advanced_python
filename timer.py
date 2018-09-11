from threading import Timer
import time

DATA = 100
TIME = 0.1


def list_data():
    for i in range(DATA+1):
        yield i


def print_even_numbers():
    for item in generator_data:
        print("{}: {}".format("Thread-1", item))
        time.sleep(TIME)


def print_odd_numbers():
    for item in generator_data:
        print("{}: {}".format("Thread-2", item))
        time.sleep(TIME)


generator_data = list_data()

Timer(TIME / 2, print_even_numbers).start()
Timer(TIME, print_odd_numbers).start()
