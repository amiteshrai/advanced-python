""" Understanding Thread Subclassing and Locks """

from threading import Lock, Thread, current_thread
from time import sleep

import numpy as np

args = (0, 1, 11, 1)


class OhmLaw:
    def make_measurement(self, start, stop, num_points, delay):
        thread = current_thread()
        x_axis = np.linspace(start, stop, num_points)
        data = []
        for _ in x_axis:
            # Acquire fake data
            print("Data Acuisition By Thread : {}".format(thread.getName()))
            data.append(np.random.random())
            sleep(delay)  # Try umcommenting this line
        return data


ohm = OhmLaw()

## 1: Subclassing a Thread
class Worker(Thread):
    def __init__(self, group, target, params):
        super().__init__()
        self.target = target
        self.group = group
        self.params = params

    def run(self):
        self.target(*self.params)


# worker = Worker("omh", ohm.make_measurement, args)
# worker.start()
## And it will behave in the same way as running a normal Thread.

## 2: Improved Subclassing of a Thread
class ImprovedWorker(Thread):
    def __init__(self, group):
        super().__init__()
        self.group = group
        self.queue = list()
        self._is_stopped = False

    def add_task(self, target, params) -> None:
        print("Adding task to queue")
        self.queue.append((target, params))

    def stop(self) -> None:
        self._is_stopped = True

    def run(self) -> None:
        while not self._is_stopped:
            if self.queue:
                func, params = self.queue.pop(0)
                func(*params)


# worker = ImprovedWorker("ohm-measurement")
# worker.start()
# worker.add_task(ohm.make_measurement, (0, 1, 11, 0.1))
# worker.add_task(ohm.make_measurement, (0, 1, 21, 0.1))
# worker.add_task(ohm.make_measurement, (0, 1, 31, 0.1))
# worker.add_task(ohm.make_measurement, (0, 1, 11, 0.1))
# worker.add_task(ohm.make_measurement, (0, 1, 21, 0.1))
# while worker.queue:
#     print("Queue length: {}".format(len(worker.queue)))
#     sleep(1)
# worker.stop()


## 3: Using Locks
## A lock allows you to prevent the execution of code if another
## thread is doing something

lock = Lock()
## Here, We define a lock outside of the Worker, because it needs
## to be shared between different instances


class WorkerWithLock(Thread):
    def __init__(self, group, target, params=None):
        super().__init__()
        self.group = group
        self.target = target
        self.params = params

    def run(self) -> None:
        lock.acquire()
        try:
            self.target(*self.params)
        except Exception as e:
            print("Execption: {}".format(e.message))
        finally:
            lock.release()


worker = Worker(group="ohm-measurement", target=ohm.make_measurement, params=args)
worker.start()
worker2 = Worker(group="ohm-measurement", target=ohm.make_measurement, params=args)
worker2.start()

## 4: Joining Threads
# worker.join()
# worker2.join()
print("Process Completed!")
