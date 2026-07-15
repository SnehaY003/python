def search_word():
    word = input("Enter word: ")
    file = open("Example.txt", "r")
    data = file.read()

    if word in data:
        print("Word Found")
    else:
        print("Word Not Found")

    file.close()

search_word()