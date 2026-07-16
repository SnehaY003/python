class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("Sneha")
s2 = Student("Mehak")
s3 = Student("Nakul")
print("Total Students =", Student.count)