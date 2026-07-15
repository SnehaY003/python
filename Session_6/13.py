def search():
    emp_id = input("Enter Employee ID: ")
    file = open("employee.txt", "r")
    for line in file:
        if emp_id in line:
            print("Employee Found")
            print(line)
    file.close()

search()