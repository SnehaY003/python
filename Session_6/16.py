def count():
    file = open("employee.txt", "r")
    lines = file.readlines()
    print("Employees =", len(lines))
    file.close()

count()