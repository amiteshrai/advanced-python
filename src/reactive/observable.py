""" Observables Creation """

from rx import Observable
from rx.testing import TestScheduler, marbles

print("---- Creating Observable ----")
print("\n\t1. From List:")


def print_value(value):
    """ Print Value """

    print("The value is ==> {}".format(value))


observable = Observable.from_(["abc", "bcd", "cde", "def"])
observable.subscribe(print_value)

print("\n\t2. From Callbacks:")


def key_value_pairs(key, value, callback):
    """ Get Key/Value Pairs """

    callback("Key: {}, Value: {}".format(key, value))


# A factory to create observable from
hello = Observable.from_callback(key_value_pairs)

# Create observable from above factory
hello("First Name", "Amitesh").subscribe(print_value)
hello("Last Name", "Rai").subscribe(print_value)

print("\n\t2. From List:")
Observable.from_list([1, 2, 3]).subscribe(print_value)

print("\n\t2. From Items at different points of time (and not immediately):")
Observable.of(1, 2, 3, 4, "A", "B", [1, 2, 3]).subscribe(print_value)
