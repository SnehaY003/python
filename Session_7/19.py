class LoginError(Exception):
    pass

username = "admin"
password = "1234"

attempt = 0

while attempt < 3:
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Login Successful")
        break

    else:
        print("Wrong credentials.")
        attempt += 1

if attempt == 3:
    raise LoginError("Maximum login attempts reached.")