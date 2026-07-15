def search():
    roll = input("Roll Number: ")
    file = open("student_marks.txt", "r")
    for line in file:
        data = line.split(",")

        if data[0] == roll:
            print(line)
            
    file.close()

search()