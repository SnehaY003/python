def display():
    file = open("student_marks.txt", "r")
    print(file.read())
    file.close()

display()