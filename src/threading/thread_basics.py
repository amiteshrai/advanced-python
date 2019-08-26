"""
Python has at least two different ways of solving this issue,
one is the threading module and the other is the multiprocessing module.
They look the same but are fundamentally different, and
therefore you need to understand their differences in order
to decide when to use one or the other.
"""

import threading
from time import sleep

import numpy as np

# 1: A Simple Measurement Class


class OhmLaw:
    def make_measurement(self, start, stop, num_points, delay):
        x_axis = np.linspace(start, stop, num_points)
        data = []
        for _ in x_axis:
            # Acquire fake data
            data.append(np.random.random())
            sleep(delay)
        return data


ohm = OhmLaw()
args = (0, 1, 11, 1)
result = ohm.make_measurement(*args)
print(result)

# 2: Running the measurement in a non-blocking way
t = threading.Thread(target=ohm.make_measurement, args=args)
t.start()
print("Triggered measurement")
# You will also notice that the program, even if it reached the
# end, is waiting for the thread t to be complete before exiting
# We can add a bit more of action in order to realize what is happening:

t = threading.Thread(target=ohm.make_measurement, args=args)
t.start()
print("Triggered measurement")
i = 0
while t.is_alive():
    i += 1
    print("Acquiring {}\r".format("." * i), end=" ")
    sleep(0.5)

# TODO: What are Threads

# 3: Plotting Results During Acquisition


class OhmLawAgain:
    def __init__(self):
        self.data = np.zeros(0)  # To store the data of the measurement
        self.step = 0  # To keep track of the step

    def make_measurement(self, start, stop, num_points, delay):
        x_axis = np.linspace(start, stop, num_points)
        self.data = np.zeros(num_points)
        self.step = 0
        for _ in x_axis:
            # Acquire fake data
            self.data[self.step] = np.random.random()
            self.step += 1
            sleep(delay)

        return self.data


ohm = OhmLawAgain()

t = threading.Thread(target=ohm.make_measurement, args=args)
t.start()
print("Triggered measurement")
i = ohm.step
while t.is_alive():
    if i != ohm.step:
        print("Latest data value: {}".format(ohm.data[ohm.step - 1]))
        i = ohm.step

args2 = (0, 1, 20, 1)
