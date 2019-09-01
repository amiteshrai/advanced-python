"""
Python has at least two different ways of running task in parallel,
one is the threading module and the other is the multiprocessing module.
They look the same but are fundamentally different, and
therefore you need to understand their differences in order
to decide when to use one or the other.
"""

import threading
from time import sleep

import numpy as np

args = (0, 1, 11, 1)
args2 = (0, 1, 21, 1)


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
result = ohm.make_measurement(*args)
print(result)

# 2: Running the measurement in a non-blocking way
thread = threading.Thread(target=ohm.make_measurement, args=args)
thread.start()
print("Triggered measurement")
# You will also notice that the program, even if it reached the
# end, is waiting for the thread t to be complete before exiting
# We can add a bit more of action in order to realize what is happening:

# thread = threading.Thread(target=ohm.make_measurement, args=args)
# thread.start()
# print("\nTriggered measurement\n")
# i = 0
# while thread.is_alive():
#     i += 1
#     print("Acquiring {}\r".format("." * i), end=" ")
#     sleep(0.25)

# TODO: What are Threads

# 3: Plotting Results During Acquisition


# class OhmLawAgain:
#     def __init__(self):
#         self.data = np.zeros(0)  # To store the data of the measurement
#         self.step = 0  # To keep track of the step

#     def make_measurement(self, start, stop, num_points, delay):
#         x_axis = np.linspace(start, stop, num_points)
#         self.data = np.zeros(num_points)
#         self.step = 0
#         delay = 0.25
#         for _ in x_axis:
#             # Acquire fake data
#             self.data[self.step] = np.random.random()
#             self.step += 1
#             sleep(delay)

#         return self.data


# ohm = OhmLawAgain()

# thread = threading.Thread(target=ohm.make_measurement, args=args)
# thread.start()
# print("\nTriggered measurement\n")
# i = ohm.step
# while thread.is_alive():
#     if i != ohm.step:
#         print("Latest data value : {}".format(ohm.data[ohm.step - 1]))
#         i = ohm.step


# # 4: Multiple Threads

# ohm = OhmLawAgain()

# print("\nTriggered multiple measurement\n")
# try:
#     thread1 = threading.Thread(target=ohm.make_measurement, args=args)
#     thread2 = threading.Thread(target=ohm.make_measurement, args=args2)
#     thread1.start()
#     thread2.start()

#     i = ohm.step
#     while thread1.is_alive() or thread2.is_alive():
#         if i != ohm.step:
#             print("Latest data value : {}".format(ohm.data[ohm.step - 1]))
#             i = ohm.step
# except Exception:
#     print("Error while running multiple measurements")


# class OhmLawDobara:
#     def __init__(self):
#         self.data = np.zeros(0)
#         self.step = 0
#         self.running = False

#     def make_measurement(self, start, stop, num_points, delay):
#         if self.running:
#             raise Exception("Can't trigger multiple measurements at the same time")

#         x_axis = np.linspace(start, stop, num_points)
#         self.data = np.zeros(num_points)
#         self.step = 0
#         self.running = True
#         for _ in x_axis:
#             # Acquire fake data
#             self.data[self.step] = np.random.random()
#             self.step += 1
#             sleep(delay)
#         self.running = False

#         return self.data


# ohm = OhmLawDobara()
# try:
#     thread1 = threading.Thread(target=ohm.make_measurement, args=args)
#     thread2 = threading.Thread(target=ohm.make_measurement, args=args2)
#     print("\nTriggered multiple measurement\n")
#     thread1.start()
#     thread2.start()
# except Exception:
#     print("Error while running multiple measurements")


# 5: Stopping a Thread
# When you are running a long task, it may happen that you need to stop it.
# Python doesn't allow you to kill threads, which means that we have to find a
# way around it.


# class OhmLawWithStop:
#     def __init__(self):
#         self.data = np.zeros(0)  # To store the data of the measurement
#         self.step = 0  # To keep track of the step
#         self.running = False
#         self.is_stopped = False

#     def stop(self):
#         self.is_stopped = True

#     def make_measurement(self, start, stop, num_points, delay):
#         if self.running:
#             raise Exception("Can't trigger two measurements at the same time")

#         x_axis = np.linspace(start, stop, num_points)
#         self.data = np.zeros(num_points)
#         self.step = 0
#         self.is_stopped = False
#         self.running = True
#         for _ in x_axis:
#             if self.is_stopped:
#                 print("Stopping")
#                 break
#             # Acquire fake data
#             self.data[self.step] = np.random.random()
#             self.step += 1
#             sleep(delay)
#         self.running = False
#         return self.data


# ohm = OhmLawWithStop()
# thread = threading.Thread(target=ohm.make_measurement, args=(0, 20, 20, 1))
# thread.start()
# current_thread = threading.current_thread()

# sleep(2)
# print("\nStopping Thread\n")
# ohm.stop()
