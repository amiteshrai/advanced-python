"""
    Python Slicing
    Format:
        somelist[start:end:stride]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- List Slicing ---")
print(numbers[1:])
print(numbers[-3:])
print(numbers[4:-5])
print(numbers[-11:])

print("--- Copying List ---")
numbers_copy = numbers[:]
print(numbers_copy)
print(numbers == numbers_copy)


print("--- List Slicing With Intervals ---")
print(numbers[2:-1:2])

# Variable references
sliced_numbers = numbers[2:6]
sliced_numbers2 = numbers[2:6]
print("--- List Comparison ---")
print(sliced_numbers == sliced_numbers2)
print("--- Address Comparison ---")
print(id(sliced_numbers) == id(sliced_numbers2))
sliced_numbers.append(10)
print("--- List Comparison ---")
print(sliced_numbers == sliced_numbers2)

# Slicing and assignments
print("--- Slicing & Assignment In One Statement ---")
sliced_list = numbers[0::2]
print(sliced_list)  # [1, 3, 5, 7, 9]
sliced_list[1:3] = [11, 21, 31]
print(sliced_list)  # [1, 11, 21, 31, 7, 9]

print("--- Reversing List ---")
numbers_reversed = numbers[::-1]
print(numbers_reversed)
