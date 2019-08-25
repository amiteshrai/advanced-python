""" Merge Two Sorted Lists"""

# Python built-in functions
print(" Using python built-in functions")
arr1 = [1, 3, 4, 5]
arr2 = [2, 5, 7, 8]
arr = arr1 + arr2
arr.sort()
print(arr)


# 1. Creating a new list
print("\n Merging by creating a new list")


def mergeLists(list1, list2):
    """
    Merge two lists in sorted manner.
    Time Complexity: O(n + m)
    Arguments:
        list1 {list} -- [description]
        list2 {list} -- [description]
    """

    n1 = len(list1)
    n2 = len(list2)
    merged_list = [None] * (n1 + n2)

    # Traverse both arrays
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        # Traverse Both lists and insert smaller value from list1 or list2
        # into result list and then increment that lists index.
        # If a list is completely traversed, while other one is left then just
        # copy all the remaining elements into result list
        if list1[i] < list2[j]:
            merged_list[k] = list1[i]
            k += 1
            i += 1
        else:
            merged_list[k] = list2[j]
            k += 1
            j += 1

    # Store remaining elements of first array
    while i < n1:
        merged_list[k] = list1[i]
        k += 1
        i += 1

    # Store remaining elements of first array
    while j < n2:
        merged_list[k] = list2[j]
        k += 1
        j += 1

    return merged_list


print(mergeLists(arr1, arr2))

# 2. Merging in Place

print("\n Merging in place")


def mergeListsInplace(list1, list2):
    """
    Merge two lists in sorted manner.
    Time Complexity: O(m(n+m))
    This is because the insert function takes O(n)O(n) time and it happens
    m times in the worst case scenario (when all the elements of the
    second list are less than all elements of the first list.

    Arguments:
        list1 {list} -- [description]
        list2 {list} -- [description]
    """

    n1, n2 = len(list1), len(list2)
    # Creating 2 new variable to track the 'current index'
    i, j = 0, 0
    # While both indeces are less than the length of their lists
    while i < n1 and j < n2:
        # If the current element of list1 is greater than the current element of list2
        if list1[i] > list2[j]:
            list1.insert(i, list2[j])
            i += 1
            j += 1
        else:
            i += 1

    # Append whatever is left of list2 to list1
    if j < n2:
        list1.extend(list2[j:])

    return list1


print(mergeListsInplace(arr1, arr2))
