student = {
    "name":"Sneha",
    "age":20
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key not found.")