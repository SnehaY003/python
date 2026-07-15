students = {}

while True:
    print("\n----- Student Record Management -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll = input("Enter Roll Number: ")

            if roll in students:
                raise Exception("Roll Number already exists!")

            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            students[roll] = {"Name": name, "Marks": marks}

            print("Student Added Successfully.")

        elif choice == 2:
            roll = input("Enter Roll Number: ")

            if roll not in students:
                raise Exception("Student not found.")

            print(students[roll])

        elif choice == 3:
            roll = input("Enter Roll Number: ")

            if roll not in students:
                raise Exception("Student not found.")

            name = input("Enter New Name: ")
            marks = int(input("Enter New Marks: "))

            students[roll] = {"Name": name, "Marks": marks}

            print("Record Updated.")

        elif choice == 4:
            roll = input("Enter Roll Number: ")

            if roll not in students:
                raise Exception("Student not found.")

            del students[roll]

            print("Record Deleted.")

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Enter valid numbers.")

    except Exception as e:
        print(e)