def replace_word():
    old =input("Enter old word: ")
    new =input("Enter new word: ")

    file =open("Example.txt", "r")
    data =file.read()
    file.close()

    data =data.replace(old, new)
    file=open("Example.txt", "w")
    file.write(data)
    file.close()

replace_word()