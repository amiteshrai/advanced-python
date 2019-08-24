""" Observables Creation """

from rx import Observable
from rx.testing import TestScheduler

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

print("\n\t3. From Items at different points of time (and not immediately):")
Observable.of(1, 2, 3, 4, "A", "B", [1, 2, 3]).subscribe(print_value)

print("\n\t4. Using Marbles Simulator:")

test_scheduler = TestScheduler()

Observable.from_marbles("--(a1)---(b1)-(c1)|", test_scheduler).subscribe(print_value)
Observable.from_marbles("-(a2)--(b2)---(c2)|", test_scheduler).subscribe(print_value)

print("\n\t5. Using Interval:")
Observable.interval(10, test_scheduler).take_until(Observable.timer(30)).subscribe(
    print_value
)
test_scheduler.start()
test_scheduler.stop()

print("\n\t6. From Buffer:")
Observable.from_(range(2000)).buffer(Observable.interval(10)).subscribe(
    lambda buffer: print("# of items in buffer: {}".format(len(buffer)))
)


print("\n\t7. From Buffer with count:")
Observable.from_(range(40)).buffer_with_count(10).subscribe(print_value)

print("\n\t8. From Buffer with time:")
test_scheduler2 = TestScheduler()
Observable.interval(10, test_scheduler2).take_until(
    Observable.timer(30)
).buffer_with_time(20).subscribe(
    lambda buffer: print("# of items in buffer: {}".format(len(buffer)))
)

test_scheduler2.start()
test_scheduler2.stop()

print("\n\t9. Grouping Observables:")


def key_selector(x):
    """ Even/Odd """

    if x % 2 == 0:
        return "even"
    return "odd"


def subscribe_group_observable(grp_observable):
    """ subscribe_group_observable """

    def print_count(count):
        """ print_count """

        print(
            "Group Observable key '{}' contains '{}' items".format(
                grp_observable.key, count
            )
        )

    grp_observable.count().subscribe(print_count)


groups = Observable.from_(range(10)).group_by(key_selector)
groups.subscribe(subscribe_group_observable)

print("\n\t10. Sampling Observables:")
test_scheduler3 = TestScheduler()
Observable.interval(1, test_scheduler3).take_until(Observable.timer(30)).sample(
    3
).subscribe(print_value)
test_scheduler3.start()
test_scheduler3.stop()

print("\n\t11. Max Value in Observables:")
Observable.from_(range(100000)).max(lambda x, y: (x - y)).subscribe(
    lambda val: print("Max Value is {}".format(val))
)

print("\n\t11. Map Observables:")
Observable.from_([1, 2, 3, 4]).map(lambda x, y: (x ** y)).subscribe(print_value)
