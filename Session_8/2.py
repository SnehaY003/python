class Student:
    def __init__(self, emp_id, name, dept,sal):
        self.id = emp_id
        self.name = name
        self.dept = dept
        self.sal= sal

    def display(self):
        print("Employee Id:", self.id)
        print("Employee Name:", self.name)
        print("Employee Department:", self.dept)
        print("Employee Salary:", self.sal)

s1 = Student(101, "Sneha", "Head", 20000)
s2 = Student(102, "Mehak", "Co-Head", 30000)
s1.display()
print()
s2.display()