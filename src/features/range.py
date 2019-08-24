""" Python Range Feature """

from random import randint

print("--- Generating Random Bits ---")
random_bits = 0

for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))
print(randint(0, 1))

names = ["Amitesh", "Avinash", "Alok", "Deepak Nahar"]
name_length = [len(n) for n in names]

# Finding longest string in a list
longest_name = None
max_letters = 0

# Not an optimized way
for i in range(len(names)):
    count = name_length[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count


# Optimized Way
longest_name = None
max_letters = 0
# zip returns a lazy generator in python 3
print(zip(name_length, names))
for count, name in zip(name_length, names):
    if count > max_letters:
        max_letters = count
        longest_name = name

print("Longest Name: {} With Max Letters: {}".format(longest_name, max_letters))

print("\n--- Finding coprime ---")


def coprime(number1, number2):
    """ Finding coprime """
    is_coprime = True
    for val in range(2, min(number1, number2) + 1):
        if number1 % val == 0 and number2 % val == 0:
            is_coprime = False
    return is_coprime


print(coprime(2, 9))
print(coprime(3, 6))
