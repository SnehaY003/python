def add_note():
    file = open("notes.txt", "a")
    note = input("Enter Note: ")
    file.write(note + "\n")
    file.close()

def view_notes():
    file = open("notes.txt", "r")
    print(file.read())
    file.close()

def search_note():
    word = input("Enter word to search: ")
    file = open("notes.txt", "r")
    found = False
    for line in file:
        if word in line:
            print(line)
            found = True

    if found == False:
        print("Note not found")
    file.close()

def delete_note():
    word = input("Enter note to delete: ")
    file = open("notes.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("notes.txt", "w")
    for line in lines:
        if word not in line:
            file.write(line)
    file.close()
    print("Note Deleted")

while True:

    print("\n1.Add Note")
    print("2.View Notes")
    print("3.Search Note")
    print("4.Delete Note")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_note()
    elif ch == 2:
        view_notes()
    elif ch == 3:
        search_note()
    elif ch == 4:
        delete_note()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")