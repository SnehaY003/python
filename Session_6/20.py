def average():
    file = open("student_marks.txt", "r")
    sum = 0
    n = 0
    for line in file:
        record = line.split(",")

        marks = int(record[2])

        sum = sum + marks
        n = n + 1

    avg = sum / n
    print("Average Marks =", avg)
    file.close()

average()