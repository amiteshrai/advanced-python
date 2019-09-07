"""
# Encapsulation => Information Hiding

In OOP, objects and classes are the fundamental entities. Objects are created using
classes. One can observe that classes contain properties and that objects are
created to manipulate and access these properties. To make this object-oriented
system more reliable and error free, it is a good practice to limit access to the
class members at times.

Information hiding refers to the concept of hiding the inner workings of a class and
simply providing an interface through which the outside world can interact with the
class without knowing what’s going on inside.

* Components of Data Hiding:
    1. Encapsulation
        Encapsulation is a fundamental programming technique used to achieve data
        hiding in OOP.

        Encapsulation in OOP refers to binding the data and the methods to
        manipulate that data together in a single unit, that is, class.

        * Advantages of Encapsulation
        1. Classes make the code easy to change and maintain.
        2. Properties to be hidden can be specified easily.
        3. We decide which outside classes or functions can access the class properties.
    2. Abstraction
"""

## 1: An Example
class User:
    def __init__(self, username=None):  # defining initializer
        print("Init")
        self.__username = username

    def set_username(self, x):
        self.__username = x

    def get_username(self):
        # print(dir(self))
        return self.__username


user = User("Amitesh Rai")
print("Before setting:", user.get_username())
user.set_username("Avinash Rai")
print("After setting:", user.get_username())
user.__username = "Pythonista"
print("After setting from outside class:", user.__username)
print("After setting from outside class:", user.get_username())
## What's going on here ?
## Answer lies in => dir(user)

## 2: Bad Example
class BadUser:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self, username, password):
        if (self.username.lower() == username.lower()) and (self.password == password):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


bad_user = BadUser("bad_user", "12345")
bad_user.login("steve", "12345")
bad_user.login("steve", "6789")
bad_user.password = "6789"
bad_user.login("steve", "6789")


## 3: A Good Example
class GoodUser:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if (self.__username.lower() == username.lower()) and (
            self.__password == password
        ):
            print(
                "Access Granted against username:",
                self.__username.lower(),
                "and password:",
                self.__password,
            )
        else:
            print("Invalid Credentials!")


steve = GoodUser("steve", "12345")
## created a new User object and stored the password and username
steve.login("steve", "12345")
## Grants access because credentials are valid
steve.login("steve", "6789")
## does not grant access since the credentails are invalid
steve.__password  # compilation error will occur due to this line
