""" Python Class """

# A class with initializer, optional parameters
class Employee:
    def __init__(self, eid, name, department=None):
        super().__init__()
        self.id = eid
        self.name = name
        self.department = department


# Creating an object of the Employee
emp = Employee(9284, "Amitesh Kumar")
# Assigning employee department
emp.department = "Retail Tech"
# Creating a new attribute for emp
emp.position = "SSE"

print(emp.id, emp.name, emp.department, emp.position)

# Class VS Instance variables
class Player:
    team = "India"  # Class Variable

    def __init__(self, name, jersey_number):
        super().__init__()
        self.id = id(self)
        self.name = name  # Instance Variable(s)
        self.jersey_number = jersey_number

    def __str__(self):
        return "(ID => {}, Name =>{}, Jersey Number => {}, Team => {})".format(
            self.id, self.name, self.jersey_number, self.team
        )


p1 = Player("Rohit Sharms", 69)
p2 = Player("Jason Roy", 99)
p2.team = "England"
print(p1)
print(p2)
print(id(p1))
