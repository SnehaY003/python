def result(marks):
    total=sum(marks)
    percentage=total/5
    if percentage>=90:
        grade="A"
    elif percentage>=75:
        grade = "B"
    elif percentage>=60:
        grade ="C"
    elif percentage>=40:
        grade = "D"
    else:
        grade = "Fail"
    return total, percentage, grade

marks= []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks of subject {i}: ")))

total,percentage,grade = result(marks)
print("Total =", total)
print("Percentage =", percentage)
print("Grade =", grade)