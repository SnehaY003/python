def create_file():
    file = open("Example.txt", "w")

    file.write("Name: Sneha Yadav\n")
    file.write("Age: 20\n")
    file.write("Course: B.Tech\n")
    file.write("College: XYZ\n")
    file.close()

create_file()