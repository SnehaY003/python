def add_expense():
    file = open("expense.txt", "a")
    date = input("Enter Date: ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    description = input("Enter Description: ")
    file.write(date + "," + category + "," + amount + "," + description + "\n")
    file.close()

def view_expense():
    file = open("expense.txt", "r")
    print(file.read())
    file.close()

def total_expense():
    file = open("expense.txt", "r")
    total = 0
    for line in file:
        data = line.strip().split(",")
        total = total + float(data[2])
    print("Total Expense =", total)
    file.close()

while True:
    print("\n1.Add Expense")
    print("2.View Expenses")
    print("3.Calculate Total Expense")
    print("4.Exit")

    ch = int(input("Enter choice: "))
    if ch == 1:
        add_expense()
    elif ch == 2:
        view_expense()
    elif ch == 3:
        total_expense()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")