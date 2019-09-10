"""
# Python Inheritance

Inheritance provides a way to create a new class from an existing class.
The new class is a specialized version of the existing class such that it inherits
all the non-private fields (variables) and methods of the existing class.
The existing class is used as a starting point or as a base to create the new class.

    * The IS A Relationship
    1. Square IS A shape
    2. Python IS A programming language
    3. Car IS A vehicle

    * The Python Object class
        In Python, whenever we create a class, it is, by default, a subclass of
        built-in Python object class. This makes it an excellent example of
        inheritance in Python. This class has very few properties and methods but
        does provide a strong basis for Object-Oriented Programming in Python.

    * The Terminologies
        In inheritance, in order to create a new class based on an existing class we
        use the following terminology:

        Parent Class (Super Class or Base Class): This class allows the re-use of its
        public properties in another class.
        Child Class (Sub Class or Derived Class): This class is the one that inherits
        or extends the superclass.

    Note : A child class has all public attributes of the parent class.

    * What is the super() Function?
        The use of super() comes into play when we implement inheritance. It is used
        in a child class to refer to the parent class without explicitly naming it.

        It makes the code more manageable, and there is no need to know the name of
        the parent class to access its attributes.

    * Types of Inheritance
        1. Single
        2. Multi-level
        3. Hierarchical
        4. Multiple
        5. Hybrid

    * Advantages of Inheritance
        1. Re-usability
        2. Code Modification
        3. Extensibility
        4. Data Hiding
"""
import random
from uuid import uuid4


## 1: An Example
class Vehicle:

    # def __init__(self, make=None, color=None, model=None):
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
        self.__classid = uuid4()
        self._creation_id = random.randint(1, 10000000)

    def print_details(self):
        print("Manufacturer : ", self.make)
        print("Color : ", self.color)
        print("Model : ", self.model)

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        # if name == "_Vehicle__classid":
        #     raise AttributeError(f"{type(self)} has no attrubute {name}")
        # else:
        #     super().__setattr__(name, value)
        return super().__setattr__(name, value)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def print_car_details(self):
        self.print_details()
        print("Doors : ", self.doors)


class Bus(Vehicle):
    def __init__(self, make, color, model, wheels):
        super().__init__(make, color, model)
        # super().__init__()
        self.wheels = wheels

    def print_details(self):
        super().print_details()
        print("Number Of Wheels : ", self.wheels)


car = Car("Suzuki", "Grey", "2015", 4)
car.print_car_details()
print("\n")
bus = Bus("Tata", "Steel Grey", "2018", 18)
bus.print_details()

## Accessing private members from the Base class (Vehicle)
print("Before : ", bus._Vehicle__classid)
bus._Vehicle__classid = uuid4()
print("After : ", bus._Vehicle__classid)
print(car._Vehicle__classid)
# print(bus._Car__classid) # No such attribute
print(dir(bus))


## Accessing protected members from the Base class (Vehicle)
# print(car._creation_id)
# print(bus._creation_id)
# print(dir(car))


## Multi-level Inheritance
class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


# creating an object of the Prius class
priusPrime = Hybrid("Suzuki", "Grey", "2015", 4)
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the parent class

## Multiple Inheritance Example
class CombustionEngine:  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine:  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybirdEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybirdEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()


## Hybrid Inheritance Example
class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybirdEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybirdEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
