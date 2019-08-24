""" Python Decorators """

import functools
import time
from datetime import datetime

# Decorators provide a simple syntax for calling higher-order functions.
# By definition, a decorator is a function that takes another function and extends the
# behavior of the latter function without explicitly modifying it.
# In Python, functions are first-class objects. This means that functions can be passed
# around and used as arguments


# Basic Example
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"{name}, together we are awesome!"


def greet(greeter_func):
    return greeter_func("Amitesh")


greeting = greet(say_hello)
print(greeting)
greeting = greet(be_awesome)
print(greeting)

print("\n")

# Inner Functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()

print("\n")

# Returning Function From Within Function
def parent2(num):
    def first_child():
        return "Hi, I am the First Child"

    def second_child():
        return "And I am the Second Child"

    if num == 1:
        return first_child
    return second_child


first = parent2(1)
second = parent2(2)
print(first, second)

print("\n")
# Simple Decorators
# Simply put, decorators wrap a function and modify its behaviour
def first_decorator(func):
    def wrapper():
        print("Before Function Invocation")
        func()
        print("After Function Invocation")

    return wrapper


def say_cheese():
    print("Say Cheese :)")


cheese = first_decorator(say_cheese)
cheese()

print("\n")

# Another decorator
def run_only_during_day(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print("Executing Daytime Utility")
            func()

    return wrapper


cheese = run_only_during_day(say_cheese)
cheese()  # No effect if called 10 in the night, till 7 in the morning

print("\n")
# Adding Syntactic Sugar!


@first_decorator
def greetings():
    print("Hey, Good Morning!")


greetings()

print("\n")

# Decorating Functions With Arguments
def fetch_user(func):
    def wrapper(*args, **kwargs):
        print(f"Fetching Data For User: {args[0]}")
        func(*args, **kwargs)
        print(f"Cleaning Up Data For User: {args[0]}")

    return wrapper


@fetch_user
def greet_user(name):
    print(f"Hi {name}, Good Morning!")


greet_user("Amitesh")

print("\n")

# Returning Value From Wrapper Function
def fetch_user_details(func):
    def wrapper(*args, **kwargs):
        print(f"Fetching Data For User: {args[0]}")
        return func(*args, **kwargs)

    return wrapper


@fetch_user_details
def get_user_details(name):
    print(f"Get User Details For {name}")
    return {"name": "Amitesh", "id": 9284, "email": "amitesh.study@mymail.com"}


user_details = get_user_details("Amitesh")
print(user_details)

print("\n")

# Preserving Wrapped Function Identity
def wrapper_function(func):
    def wrapper():
        print(f"This is {func.__name__}")
        return func()

    return wrapper


@wrapper_function
def wrapped_function():
    print(f"This is {__name__}")


wrapped_function()

# Decorators should use the @functools.wraps decorator, which will preserve information
# about the original function.
# The @functools.wraps decorator uses the function functools.update_wrapper() to update
# special attributes like __name__ and __doc__ that are used in the introspection.

print("\n")

# More Examples
def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(100)
