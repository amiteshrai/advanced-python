""" Python Class """

## A class with initializer, optional parameters
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


## Wrong Use of Class Variables
class PlayerWithIssue:
    team = "India"  # class var
    former_teams = []  # wrong use of class var

    def __init__(self, name):
        super().__init__()
        self.name = name  # instance var

    def __str__(self):
        return f"""
            Player Info
        Name : {self.name},
        Team : {self.team},
        Former Teams : {self.former_teams}
        """


p1 = PlayerWithIssue("Shikhar Dhawan")
p1.former_teams.append("India U19 - 2004")
print(p1)
p2 = PlayerWithIssue("Yuvraj Singh")
p2.former_teams.append("India U19 - 2001")
print(p2)

# Change class var
p2.former_teams = None
print(p1, p2)
print(PlayerWithIssue.former_teams)


class PlayerWithoutIssue:
    team = "India"  # class var

    def __init__(self, name):
        super().__init__()
        # instance vars
        self.name = name
        self.former_teams = list()

    def __str__(self):
        return f"""
            Player Info
        Name : {self.name},
        Team : {self.team},
        Former Teams : {self.former_teams}
        """


p1 = PlayerWithoutIssue("Shikhar Dhawan")
p1.former_teams.append("India U19 - 2004")
p2 = PlayerWithoutIssue("Yuvraj Singh")
p2.former_teams.append("India U19 - 2001")
print(p1, p2)

# After change
p1.former_teams = None
print(p1, p2)


class PlayerWithMembers:
    # team = "India"
    team_members = set()

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.former_teams = list()
        self.team_members.add(self.name)

    def __str__(self):
        return f"""
            Player Info
        Name : {self.name},
        Team : {self.team},
        Team Members : {self.team_members}
        Former Teams : {self.former_teams}
        """

    @property
    def team(self):
        return "India"


p1 = PlayerWithMembers("Shikhar Dhawan")
p1.former_teams.append("India U19 - 2004")
p2 = PlayerWithMembers("Rohit Sharma")
p2.former_teams.append("India U19 - 2005")
p3 = PlayerWithMembers("MS Dhoni")
p3.former_teams.append("India Test")

print(p1, p2, p3)
# print(dir(PlayerWithMembers.team.fget()))
print(PlayerWithMembers.team.fget(p2))
print(type(p1.team))
