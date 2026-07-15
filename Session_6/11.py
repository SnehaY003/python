def add_employee():
    file = open("employee.txt", "a")

    emp_id = input("Employee ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    salary = input("Salary: ")
    file.write(emp_id + "," + name + "," + dept + "," + salary + "\n")
    file.close()

add_employee()