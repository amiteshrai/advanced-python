""" Understanding Thread Subclassing and Locks """

from threading import Thread
from time import sleep

from thread_basics import OhmLaw, args


# 1: Subclassing a Thread
class Worker(Thread):
    def __init__(self, group, target, params):
        super().__init__()
        self.target = target
        self.group = group
        self.params = params

    def run(self):
        self.target(*self.params)


ohm = OhmLaw()
worker = Worker("omh", ohm.make_measurement, args)
worker.start()
# And it will behave in the same way as running a normal Thread.

# 2: Improved Subclassing of a Thread
class Worker2(Thread):
    def __init__(self, group):
        super().__init__()
        self.group = group
        self.queue = list()
        self._is_stopped = False

    def add_task(self, target, params):
        print("Adding task to queue")
        self.queue.append((target, params))

    def stop(self):
        self._is_stopped = True

    def run(self):
        while not self._is_stopped:
            if self.queue:
                func, params = self.queue.pop(0)
                func(*params)


worker = Worker2("ohm-measurement")
worker.start()
worker.add_task(ohm.make_measurement, (0, 1, 11, 0.1))
worker.add_task(ohm.make_measurement, (0, 1, 21, 0.1))
worker.add_task(ohm.make_measurement, (0, 1, 31, 0.1))
worker.add_task(ohm.make_measurement, (0, 1, 11, 0.1))
worker.add_task(ohm.make_measurement, (0, 1, 21, 0.1))
while worker.queue:
    print("Queue length: {}".format(len(worker.queue)))
    sleep(1)
worker.stop()
