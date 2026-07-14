student = {
    "Name": "sneha",
    "Age": 18,
    "Course": "Btech"
}

key = input("Enter key to search: ")

if key in student:
    print("Key Found!")
    print("Value =", student[key])
else:
    print("Key Not Found!")