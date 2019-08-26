""" Problems On Lists """

# Challenge 4: List of Products of all Elements
# Given a list, return a list where each index stores the
# product of all numbers in the list except the number at
# the index itself.

inputs = [9, 2, 3, 4, 5]
outputs = [120, 60, 40, 30, 24]

# 1: Using a nested loop
def findProduct(elements):
    results = []
    n = len(elements)
    for i in range(n):  # O(n)
        result = 1
        for j in range(n):  # O(n)
            if i != j:
                result = result * elements[j]
        results.append(result)
    return results


print("Using a nested loop : ", findProduct(inputs))

# 1: Using a nested loop (Improved)
