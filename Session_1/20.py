name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total_marks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total_marks = total_marks + marks

percentage = total_marks / 5

print("----- Student Report Card -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")