"""
# Access Modifiers

    * In Python, we can impose access restrictions on different data members and
      member functions. The restrictions are specified through access modifiers.

    * Access modifiers are tags we can associate with each member to define which
      parts of the program can access it directly.

    # There are two types of access modifiers in Python.
        1. Public Attributes:
            Public attributes are those that be can be accessed inside the class and
            outside the class.

            Technically in Python, all methods and properties in a class are
            publicly available by default.

            If we want to suggest that a method should not be used publicly,
            we have to declare it as private explicitly.

        2. Private attributes:
            Private attributes cannot be accessed directly from outside the class
            but can be accessed from inside the.

            We can make members private using the double underscore __ prefix

        * Note: Methods are usually public since they provide an interface for the
                class properties and the main code to interact with each other.

        3. Not So Protected
            Protected properties and methods in other languages can be accessed by
            classes and their subclasses which will be discussed later.

            As we have seen, Python does not have a hard rule for accessing
            properties and methods, so it does not have the protected access modifier.


    # Types Of Members In Python:
        1. Private
        2. Protected
        3. Public
"""

## 1: An Example
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.__salary = float(salary)
        self.__tax_rate = 0.2

    def display_id(self):
        print("ID:", self.ID)

    def display_salary(self):  # display_salary is a public method
        print("Salary:", self.__salary)

    def __calc_take_home_salary(self):
        return self.__salary - self.__salary * self.__tax_rate

    def __str__(self):
        return f"""
            ID: {self.ID}
            Salary: {self.__salary}
            Take Home Salary : {self.__calc_take_home_salary()}
        """


steve = Employee(3789, 2500)
steve.display_id()
print("Steve's ID : ", steve.ID)
# print("Steve's ID : ", steve.__salary)
# print("Steve's Take Home Salary : ", steve.__calc_take_home_salary())
# To ensure that no one from the outside knows about this
# private property, the error does not reveal the identity of it.
print(steve)


## 2: Accessing Private Attributes in the Main Code
print(steve._Employee__salary)
print(steve._Employee__calc_take_home_salary())


class Point:
    def __init__(self, x, y, z) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def sum_of_squares(self):
        sq_x, sq_y, sq_z = self.x ** 2, self.y ** 2, self.z ** 2
        return sq_x + sq_y + sq_z
