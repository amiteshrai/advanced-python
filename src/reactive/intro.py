""" Reactive Programming Intro With RxPy"""

import time

from rx import Observable, Observer


def print_number(number):
    """[summary]

    Arguments:
        x {[type]} -- [description]
    """

    print("The number is {}".format(number))


Observable.from_(range(10)).subscribe(print_number)


def push_five_strings(observer):
    """[summary]

    Arguments:
        observer {[type]} -- [description]
    """

    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()


# Implementing an Observer class for data streams and event handling
print("\n------------ Implementing an Observer --------------\n")


class PrintObserver(Observer):
    """ Data Streams Observer

    Arguments:
        Observer {[type]} -- [description]
    """

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


source = Observable.create(push_five_strings)

source.subscribe(PrintObserver())


# Arguments to subscribe()
print("\n----------Arguments to subscribe()------------\n")

# Most of the time you will not want to go through the verbosity of implementing your
# own Observer.
# You can instead pass 1 to 3 lambda arguments to subscribe() specifying the
# on_next, on_complete, and on_error actions.

source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

source.subscribe(
    on_next=lambda value: print("Received {0}".format(value)),
    on_completed=lambda: print("Done!"),
    on_error=lambda error: print("Error Occurred: {0}".format(error)),
)

# Operators and Chaining
print("\n----------Operators and Chaining------------\n")
source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

lengths = source.map(lambda s: len(s))
filtered = lengths.filter(lambda i: i >= 5)
filtered.subscribe(lambda value: print("Received {0}".format(value)))


# More Operators chaining
print("\n----------More Operators chaining------------\n")

Observable.from_([1, 2, 3, 4, 5, 6, 7, 8, 9]).subscribe(print_number)

print("\n----------More Operators chaining 2------------\n")
Observable.interval(1).take_until(Observable.timer(30)).sample(10).subscribe(
    print_number
)
print("Timer begins now")
time.sleep(0.005)


time.sleep(2)
# Emitting Events
print("\n---------- Emitting Events ------------\n")
Observable.interval(1000).map(lambda i: "{0} Mississippi".format(i)).subscribe(
    lambda s: print(s)
)

input("Press any key to quit\n")
