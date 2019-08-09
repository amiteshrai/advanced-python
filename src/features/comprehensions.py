""" Python List Comprehensions """

numbers = [1, 2, 3, 4, 5, 6, 7]

# Calc squares
# 1. using list comprehension
squares = [number ** 2 for number in numbers]
# 2. using map function
squares = map(lambda number: number ** 2, numbers)

# Calc squares for only even numbers
# 1. using list comprehension
squares = [number ** 2 for number in numbers if number % 2 == 0]
# 2. using map function
squares = map(
    lambda number: number ** 2, filter(lambda number: number % 2 == 0, numbers)
)
print(list(squares))


# Dict comprehension
marks = {"physics": 54, "maths": 85, "chemistry": 80}
subjects = {name for name in marks.keys()}
print(subjects)

subjects = {name.upper() for name in subjects}
print(subjects)

# Flatten a matrix
matrix = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
flattened = [x for sublist1 in matrix for sublist2 in sublist1 for x in sublist2]
print(flattened)
