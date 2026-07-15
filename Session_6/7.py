def copy_file():
    file1 = open("Example.txt", "r")
    data = file1.read()

    file2 = open("copy.txt", "w")
    file2.write(data)

    file1.close()
    file2.close()

copy_file()