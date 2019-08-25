import array

# The List
vowels = ["a", "e", "i", "o", "u"]
vowels.append(2)
print(type(vowels))

# The Array
numbers = array.array("b", [1, 2, 3])

# OverflowError: signed char is greater than maximum
# numbers.append(255)
print(type(numbers))

# Deleting elements
del vowels[len(vowels) - 1]
del numbers[2]
print(vowels, numbers)

vowels.remove("a")
numbers.remove(1)
print(vowels, numbers)

# ValueError: array.remove(x) / list.remove(x): x not in list
# vowels.remove("a")
# numbers.remove(1)

# Extending List/Array
vowels.extend(["c", "d", "f", None])
# TypeError: an integer is required (got type NoneType)
numbers.extend([2, 3, 5, 6, None])

print(vowels, numbers)
