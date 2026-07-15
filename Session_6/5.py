def count_words():
    file = open("Example.txt", "r")
    text = file.read()
    words = text.split()
    print("Total words =", len(words))
    file.close()

count_words()