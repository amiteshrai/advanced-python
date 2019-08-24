""" Python Generators """

import cProfile
import re
import sys

import requests


# Function returning a generator
def countdown(number):
    """ Generator Function """
    print("Starting")

    while number > 0:
        yield number
        number -= 1


value = countdown(5)
print(value)
try:
    print(next(value))
    print(next(value))
    print(next(value))
    print(next(value))
    print(next(value))
    print(next(value))
    print(next(value))
except StopIteration as err:
    print("StopIteration Error")

# Generator Expressions
numbers_list = [1, 2, 3, 4, 5]
numbers_gen = (x for x in numbers_list)
print(numbers_gen)
print(next(numbers_gen))

large_list = [i ** 2 for i in range(1000000)]
print("Large List Size: ", sys.getsizeof(large_list))
large_gen = (i ** 2 for i in range(1000000))
print("Large Generator Size: ", sys.getsizeof(large_gen))

# Profiling
# Using Generators
cProfile.run("sum((i * 2 for i in range(10000000)))")
# Using List
cProfile.run("sum([i * 2 for i in range(10000000)])")


def get_pages(link):
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == "/":
                url = current_link + url[1:]
            pattern = re.compile("https?")
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link


webpage = get_pages("https://realpython.com/introduction-to-python-generators/")
for result in webpage:
    print(result)
