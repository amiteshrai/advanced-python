"""
# What is Polymorphism ?

The word Polymorphism is a combination of two Greek words, Poly meaning many and
Morph meaning forms.

In programming, polymorphism refers to the same object exhibiting different forms
and behaviors.

For example, take the Shape Class. The exact shape you choose can be anything.
It can be a rectangle, a circle, a polygon or a diamond. So, these are all shapes,
but their properties are different. This is called Polymorphism.

** What does Polymorphism Achieve?
1. Makes code manageable
2. Promotes Open Close Principle (SOLID)
      " Software entities (classes, modules, functions, etc.) should be open for
      extension, but closed for modification."

** Ways to implement polymorphism:
1. Polymorphism Using Methods.
2. Polymorphism Using Inheritance.
    1. Method Overriding
    Method overriding is the process of redefining a parent class’s method in a
    subclass.

    In other words, if a subclass provides a specific implementation of a method
    that had already been defined in one of its parent classes, it is known as
    method overriding.

    ** Advantages and Key Features of Method Overriding:
    1. The derived classes can give their own specific implementations to inherited
    methods without modifying the parent class methods.
    2. For any method, a child class can use the implementation in the parent class
    or make its own implementation.
    3. Method Overriding needs inheritance and there should be at least one derived
    class to implement it.
    4. The method in the derived classes usually have a different implementation from
    one another.

    2. Operator/Method Overloading
        Show examples to explain.
    3. Abstract Base Classes
        Discussed at the very end.

3. Polymorphism Using Duck Typing.
    Duck typing is one of the most useful concepts in Object-Oriented Programming in
    Python.
    Using duck typing, we can implement polymorphism without using inheritance.

    ** What is Duck Typing ?
        If an object quacks like a duck, swims like a duck, eats like a duck or in
        short, acts like a duck, that object is a duck.
        Duck typing extends the concept of dynamic typing in Python.
        Dynamic typing means we can change the type of an object later in the code.
        Using duck typing, we can achieve polymorphism without inheritance.

** Abstract Base Classes
    Duck typing is useful as it simplifies the code and the user can implement the
    functions without worrying about the data type. But this may not be the case
    all the time. The user might not follow the instructions to implement the
    necessary steps for duck typing. To cater to this issue, Python introduced the
    concept of Abstract Base Classes, or ABC.

    Abstract base classes define a set of methods and properties that a class must
    implement in order to be considered a duck-type instance of that class.
"""
from abc import ABC, abstractmethod

## An Example with polymorphism using methods
# class Rectangle:
#     def __init__(self, width=0, height=0):
#         super().__init__()
#         self.width = width
#         self.height = height

#     @property
#     def sides(self):
#         return 4

#     def area(self):
#         return self.width * self.height


# class Circle:
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius

#     @property
#     def PI(self):
#         return 3.14

#     @property
#     def sides(self):
#         return 0

#     def area(self):
#         return self.PI * (self.radius ** 2)


# shapes = [Rectangle(6, 10), Circle(7)]
# print("Sides of a rectangle are", str(shapes[0].sides))
# print("Area of rectangle is:", str(shapes[0].area()))

# print("Sides of a circle are", str(shapes[1].sides))
# print("Area of circle is:", str(shapes[1].area()))

## Method calls on lines 59 and 62 look identical, but different methods are called.
## Thus, we have achieved polymorphism.


## An Example with polymorphism using inheritance
class Shape:
    def __init__(self, sides=0):
        self.sides = sides
        self.__constants = {"PI": 3.14}

    def area(self):  # Abstract method
        pass


## Rectangle IS A Shape with a specific width and height
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def area(self):  # Overrides abstract methods from parent class
        return self.width * self.height


## Circle IS A Shape with a specific radius
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(sides=0)
        self.radius = radius

    def area(self):  # Overrides abstract methods from parent class
        return self._Shape__constants.get("PI") * (self.radius ** 2)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].area()))
print("Area of circle is:", str(shapes[1].area()))
## This is Polymorphism; having specialized implementations of the same methods for
## each class.


## Example 3: Operator Overloading
class PlusMinusOperator:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = PlusMinusOperator(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = PlusMinusOperator(self.real - other.real, self.imag - other.imag)
        return temp


obj1 = PlusMinusOperator(3, 7)
obj2 = PlusMinusOperator(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj3:", obj4.imag)

## However, below is not possible
# print(shapes[0] + shapes[1])
## TypeError: unsupported operand type(s) for +: 'Rectangle' and 'Circle'


## Provide few more examples on operator overloading

## An Example : Dynamic Typing
value = 29
print(f"type of 'value' is {type(value)}")
value = "Amitesh Rai"
print(f"type of 'value' is {type(value)}")


## An Example : Implementing Duck Typing
class Dog:
    def make_some_noise(self):
        print("Woof Woof ...")


class Cat:
    def make_some_noise(self):
        print("Meow Meow ...")


class UgamEmployees:
    def make_some_noise(self):
        print(f"We are learning Python ...")


class Sound:
    def produce_sound(self, animal):
        print(f"Producing sound for {type(animal).__name__}")
        animal.make_some_noise()


sound = Sound()
dog = Dog()
cat = Cat()
sound.produce_sound(dog)
sound.produce_sound(cat)
ugamites = UgamEmployees()
sound.produce_sound(ugamites)


class AbstractShape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# abstract = AbstractShape()
## Above code will not compile since AbstractShape has abstract methods without
## method definitions in it


class Square(AbstractShape):
    def __init__(self, length):
        self.length = length


# square = Square(4)
## Above code will not compile since abstarct methods have not been defined in
## the child class, Square


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # calculate the semi-perimeter
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2

        return (
            semi_perimeter
            * (semi_perimeter - self.side1)
            * (semi_perimeter - self.side2)
            * (semi_perimeter - self.side3)
        ) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


triangle = Triangle(4, 5, 6)
print(f"area of triangle is : {triangle.area()}")
print(f"perimeter of triangle is : {triangle.perimeter()}")
