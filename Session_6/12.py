def display():
    file=open("employee.txt", "r")
    print(file.read())
    file.close()

display()