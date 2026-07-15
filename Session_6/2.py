def read_file():
    file = open("Example.txt","r")

    print(file.read())
    file.close()

read_file()