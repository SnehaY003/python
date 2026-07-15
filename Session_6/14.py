def update():
    emp_id = input("Enter Employee ID: ")
    salary = input("Enter New Salary: ")

    file = open("employee.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("employee.txt", "w")

    for line in lines:
        data = line.split(",")

        if data[0] == emp_id:
            line = data[0] + "," + data[1] + "," + data[2] + "," + salary + "\n"
        file.write(line)
    file.close()
    print("Salary Updated")
update()