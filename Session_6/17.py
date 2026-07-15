def add_student():
    file = open("student_marks.txt", "a")

    roll = input("Roll Number: ")
    name = input("Name: ")
    marks = input("Marks: ")

    file.write(roll + "," + name + "," + marks + "\n")
    file.close()
add_student()