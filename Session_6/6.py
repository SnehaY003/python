def count_characters():
    file = open("Example.txt", "r")
    print("Total characters =", len(file.read()))
    file.close()

count_characters()