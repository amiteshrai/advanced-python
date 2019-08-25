""" Find Two Numbers that Add up to N """
# Inputs
lst = [1, 21, 3, 14, 5, 60, 7, 6]
N = 81

# 1: Brute Force
print("Brute Force")


def findSumElements1(elements, val):
    """ O(n ** 2) """

    n = len(elements)
    for i in range(n):
        for j in range(n):
            if elements[i] + elements[j] == val and i != j:
                return [elements[i], elements[j]]


print(findSumElements1(lst, N))

# 2: Sorting the List
print("\n Sorting the List")


def binarySearch(elements, item):
    first, last = 0, len(elements) - 1
    found = None

    while first <= last and not found:
        mid = first + last // 2
        if elements[mid] == item:
            found = mid
        else:
            if item < elements[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def findSumElements2(elements, val):
    elements.sort()  # O(nlogn)

    for element in elements:  # O(nlogn)
        other_el = val - element
        index = binarySearch(elements, other_el)  # O(logn)
        if index:
            return [element, other_el]


print(findSumElements2(lst, N))

# 3: Moving indices
print("\n Moving indices")


def findSumElements3(elements, val):
    elements.sort()  # O(nlogn)
    start, end = 0, len(elements) - 1
    result = []
    sum_els = 0

    # move start and end indices accordingly
    while start != end:
        sum_els = elements[start] + elements[end]
        if sum_els < val:
            start += 1
        elif sum_els > val:
            end -= 1
        else:
            result.extend([elements[start], elements[end]])
            return result
    return result


print(findSumElements3(lst, 8))

# 4: Using a Dictionary


def findSumElements(elements, val):
    foundValues = set()

    for el in elements:  # O(n)
        other_el = val - el
        if other_el in foundValues:  # O(1)
            return [val - el, el]
        foundValues.add(el)
    return False
