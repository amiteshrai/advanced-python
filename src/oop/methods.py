"""
* Python class method types:
    1. instance methods
    2. class methods
        Class methods are accessed using the class name and can be
        accessed without creating a class object.

        ** Note: Just like instance methods, all class methods have at
        least one argument, cls.
    3. static methods
        Static methods are methods that are usually limited to class only and not
        their objects. They have no direct relation to the class variables or
        instance variables.

        Static methods can be accessed using the class name or the object name.

        They are used as utility functions inside the class or when we do not
        want the inherited classes to modify a method definition.

* The Purpose of Methods
    Methods act as an interface between a program and the properties of a
    class in the program.

    These methods can either alter the content of the properties or use
    their values to perform a particular computation.

* Method Parameters
    Method parameters make it possible to pass values to the method.
    In Python, the first parameter of the method should ALWAYS be self
    (will be discussed below) and this is followed by the remaining parameters.

* Return Statement
    The return statement mClass methods are accessed using the class name
    and can be accessed without creating a class object.akes it possible
    to get the value from the method.

* The 'self' Argument
    One of the major differences between functions and methods in Python
    is the first argument in the method definition.

    This pseudo-variable provides a reference to the calling object, that
    is the object to which Method Overloadingthe method or property belongs to.

    If the user does not mention the self as the first argument, the
    first parameter will be treated for reference to the object.

    ** Note: The self argument only needs to be passed in the method
    definition and not when the method is called.

* Method Overloading (Polymorphism)
    Overloading refers to making a method perform different operations
    based on the nature ofClass methods are accessed using the class name
    and can be accessed without creating a class object. its arguments.

    Unlike in other programming languages, methods cannot be explicitly
    overloaded in Python but can be implicitly overloaded.
"""

## An Example
class Employee:
    org_name = "Ugam Solutions"

    # defining the initializer
    def __init__(self, ID, name, salary=None, department=None) -> None:
        self.ID = ID
        self.name = name
        self.salary = salary
        self.department = department

    # def tax(self):
    #     return self.salary * 0.2

    def tax(self, savings=None) -> float:
        if savings is not None and not isinstance(savings, float):
            raise TypeError("savings cannot be anything but number")
        # return self.salary * 0.2 if savings is None else self.salary - savings * 0.2
        return self.salary * 0.2 if savings is None else (self.salary - savings) * 0.2

    def salary_per_day(self) -> float:
        return self.salary / 30

    @classmethod
    def get_employer(cls) -> str:
        print(cls, id(cls), type(cls))
        return cls.org_name

    @staticmethod
    def print_employer() -> None:
        print(f"Employer Name : {Employee.org_name}")

    @staticmethod
    def get_salary(
        salary, monthly=True, daily=False, hourly=False, total_hours=None
    ) -> float:
        salary_calc = salary
        if monthly:
            salary_calc = salary / 12
        elif daily:
            salary_calc = salary / 365
        elif hourly:
            if total_hours is None:
                raise ValueError("Please input total working hours")
            salary_calc = salary / total_hours
        return salary_calc

    def __str__(self) -> str:
        print(id(self))
        return f"""
            ID : {self.ID}
            Salary : {self.salary}
            Department : {self.department}
            Tax paid by {self.name} : {self.tax()}
            Tax paid by {self.name} after savings : {self.tax(savings=4000.0)}
            Salary per day of {self.name} : {self.salary_per_day()}
            Organization Name: {self.org_name}
        """

    def get_department(self):
        return self.department


# initializing an object of the Employee class
pankaj = Employee(3789, "Pankaj Singh", 25000.0, "Technology")
print(pankaj)
print(pankaj.get_employer())
print(Employee.get_employer())
Employee.print_employer()
emp_salary = Employee.get_salary(
    120000, monthly=False, daily=False, hourly=True, total_hours=12
)
print(emp_salary)


print("\nClass Inheritence\n")


class HREmployee(Employee):
    def __init__(self, ID, name, salary=None, department=None):
        super().__init__(ID, name, salary=salary, department="Human Resource")

    # @property
    # def department(self):
    #     return self.department


smruti = HREmployee(3789, "Pankaj Singh", 250000.0, "Technology")
smruti_salary = smruti.get_salary(
    160000, monthly=False, daily=False, hourly=True, total_hours=12
)
print(f"Smruti's Salary / Hour : {smruti_salary}")
smruti.org_name = "ABC Coporation"
print(smruti.get_employer())
smruti.print_employer()
print(HREmployee.org_name)
print(smruti)
