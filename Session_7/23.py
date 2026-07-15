while True:

    print("\n----- Login System -----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    try:

        choice = int(input("Enter choice: "))

        if choice == 1:

            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")

            if "@" not in email or "." not in email:
                raise Exception("Invalid Email")

            file = open("users.txt", "a")

            file.write(username + "," + password + "," + email + "\n")

            file.close()

            print("Registration Successful")

        elif choice == 2:

            username = input("Username: ")
            password = input("Password: ")

            found = False

            file = open("users.txt", "r")

            for line in file:

                data = line.strip().split(",")

                if data[0] == username and data[1] == password:
                    found = True

            file.close()

            if found:
                print("Login Successful")

            else:
                print("Invalid Username or Password")

        elif choice == 3:
            break

        else:
            print("Invalid Choice")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print(e)