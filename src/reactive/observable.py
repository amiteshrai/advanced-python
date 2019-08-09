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


# """
# Grouped Observable : ['__abstractmethods__', '__add__', '__await__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_methods', '_subscribe_core', 'aggregate', 'all', 'amb', 'and_', 'as_observable', 'average', 'buffer', 'buffer_with_count', 'buffer_with_time', 'buffer_with_time_or_count', 'case', 'catch_exception', 'combine_latest', 'concat', 'concat_all', 'concat_map', 'contains', 'controlled', 'count', 'create', 'create_with_disposable', 'debounce', 'default_if_empty', 'defer', 'delay', 'delay_subscription', 'delay_with_selector', 'dematerialize', 'distinct', 'distinct_until_changed', 'do_action', 'do_after_next', 'do_after_terminate', 'do_finally', 'do_on_dispose', 'do_on_subscribe', 'do_on_terminate', 'do_while', 'element_at', 'element_at_or_default', 'empty', 'every', 'exclusive', 'expand', 'filter', 'finally_action', 'find', 'find_index', 'first', 'first_or_default', 'flat_map', 'flat_map_latest', 'for_in', 'from_', 'from_callable', 'from_callback', 'from_future', 'from_iterable', 'from_list', 'from_marbles', 'from_string', 'generate', 'generate_with_relative_time', 'group_by', 'group_by_until', 'group_join', 'if_then', 'ignore_elements', 'interval', 'is_empty', 'join', 'just', 'key', 'last', 'last_or_default', 'let', 'let_bind', 'lock', 'many_select', 'map', 'materialize', 'max', 'max_by', 'median', 'merge', 'merge_all', 'merge_observable', 'min', 'min_by', 'mode', 'multicast', 'never', 'observe_on', 'of', 'on_error_resume_next', 'pairwise', 'partition', 'pausable', 'pausable_buffered', 'pluck', 'pluck_attr', 'publish', 'publish_value', 'range', 'reduce', 'repeat', 'replay', 'retry', 'return_value', 'sample', 'scan', 'select', 'select_many', 'select_switch', 'sequence_equal', 'share', 'single', 'single_or_default', 'skip', 'skip_last', 'skip_last_with_time', 'skip_until', 'skip_until_with_time', 'skip_while', 'skip_with_time', 'slice', 'some', 'standard_deviation', 'start', 'start_async', 'start_with', 'subscribe', 'subscribe_on', 'sum', 'switch_case', 'switch_latest', 'switch_map', 'take', 'take_last', 'take_last_buffer', 'take_last_with_time', 'take_until', 'take_until_with_time', 'take_while', 'take_with_time', 'tap', 'then', 'then_do', 'throttle_first', 'throttle_last', 'throttle_with_selector', 'throttle_with_timeout', 'throw', 'throw_exception', 'time_interval', 'timeout', 'timeout_with_selector', 'timer', 'timestamp', 'to_async', 'to_blocking', 'to_dict', 'to_future', 'to_iterable', 'to_list', 'to_marbles', 'to_set', 'to_sorted_list', 'to_string', 'transduce', 'underlying_observable', 'using', 'variance', 'when', 'where', 'while_do', 'window', 'window_with_count', 'window_with_time', 'window_with_time_or_count', 'with_latest_from', 'zip', 'zip_array', 'zip_list']
# """


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
