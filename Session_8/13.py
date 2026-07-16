class College:
    def __init__(self, name, location, students):
        self.name = name
        self.location = location
        self.students = students

    def display(self):
        print("College:", self.name)
        print("Location:", self.location)
        print("Students:", self.students)


c = College("ABC College", "Delhi", 1200)
c.display()