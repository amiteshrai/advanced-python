""" Immutability In Python """

import copy

var1 = [1, 2, 3]
var2 = (1, 2, 3)
print(id(var1), id(var2))

# Extending list/tuples
var1 += [4, 5]
var2 += (4, 5)
print(id(var1), id(var2))

# Accessing elements from list/tuples
print(var1[2], var2[2])

# Mutating list/tuples
var1[2] = 2
# TypeError: 'tuple' object does not support item assignment
# var2[2] = 2


# Other immutable types
var3 = 1
var4 = "Amitesh"
print(id(var3), id(var4))

var3 += 1
var4 = var4 + " Kumar"
print(id(var3), id(var4))


var5 = var1
print(var1 is var5)  # object ref
print(var1 == var5)  # object value

var6 = "abc"
var7 = var6
print(var6 is var7)
print(var6 == var7)

var6 += "def"
print(var6 is var7)

# Performance comparison

# 1. python -m timeit "1 == 1"
# 100000000 loops, best of 3: 0.0181 usec per loop

# 2> python -m timeit "1 is 1"
# 100000000 loops, best of 3: 0.0134 usec per loop

# The other is that when working with custom classes,
# you can specify what happens when you compare them to other objects.
# This is a very silly example but would prove the point:


class MyClass:
    def __eq__(self, other):
        return True


my_obj = MyClass()

if my_obj == None:
    print("My object == None")

if my_obj is None:
    print("My Object is None")


# Mutable Objects in Functions
def divide_and_average(var):
    for i, v in enumerate(var):
        var[i] = v / 2

    avg = sum(var) / len(var)
    return avg


my_list = [1, 2, 3]
print(divide_and_average(my_list))
print(my_list)


def divide_and_average2(var):
    var = copy.copy(var)
    for i, v in enumerate(var):
        var[i] = v / 2

    avg = sum(var) / len(var)
    return avg


my_list = [1, 2, 3]
print(divide_and_average2(my_list))
print(my_list)


# Default Arguments in Functions
def increase_values(var1=[1, 1], value=0):
    value += 1
    var1[0] += value
    var1[1] += value
    return var1


print(increase_values())  # [2, 2]
print(increase_values())  # [3, 3]


# Your Own Immutable Objects
class Employee:
    def __init__(self, eid, ename):
        super().__init__()
        self.id = eid
        self.name = ename

    def __setattr__(self, name, value):
        if name != "id":
            return super().__setattr__(name, value)
        else:
            raise TypeError("ID attribute cannot be changed")


# TypeError: ID attribute cannot be changed
# emp = Employee(101, "Python")


class Employee2:
    def __init__(self, eid, ename):
        super().__init__()
        super().__setattr__("id", eid)
        super().__setattr__("name", ename)

    def __setattr__(self, name, value):
        if name != "id":
            return super().__setattr__(name, value)
        else:
            raise TypeError("ID attribute cannot be changed")

    def __str__(self):
        return "Employee => (ID (Immutable): {}, NAME (Mutable): {})".format(
            self.id, super().__getattribute__("name")
        )


emp2 = Employee2(101, "Python")
emp2.name = "Python 101"

# TypeError: ID attribute cannot be changed
# emp2.id = 102
print(emp2)
