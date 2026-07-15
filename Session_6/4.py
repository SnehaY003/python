def count_lines():
    file = open("Example.txt", "r")
    print("Total lines =", len(file.readlines()))
    file.close()

count_lines()