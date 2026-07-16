class Student:
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def display(self):
        print("Roll Number:", self.roll)
        print("Name:", self.name)
        print("Age:", self.age)


s = Student(1, "Sneha", 20)
s.display()