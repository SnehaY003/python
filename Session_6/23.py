def add_contact():
    file = open("contacts.txt", "a")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    file.write(name + "," + phone + "," + email + "\n")
    file.close()

def view_contacts():
    file = open("contacts.txt", "r")
    print(file.read())
    file.close()

def search_contact():
    name = input("Enter Name: ")
    file = open("contacts.txt", "r")
    found = False
    for line in file:
        data = line.strip().split(",")

        if data[0] == name:
            print(line)
            found = True
    if found == False:
        print("Contact not found")

    file.close()

def delete_contact():
    name = input("Enter Name: ")
    file = open("contacts.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("contacts.txt", "w")
    for line in lines:
        if line.split(",")[0] != name:
            file.write(line)
    file.close()
    print("Contact Deleted")

while True:
    print("\n1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_contact()
    elif ch == 2:
        view_contacts()
    elif ch == 3:
        search_contact()
    elif ch == 4:
        delete_contact()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")