try:
    marks = int(input("Enter marks: "))
    if marks >= 0 and marks <= 100:
        print("Marks accepted")
    else:
        print("Marks must be between 0 and 100")

except ValueError:
    print("Invalid input")