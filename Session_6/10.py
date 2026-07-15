def upper_case():
    file = open("Example.txt", "r")
    data = file.read()
    print(data.upper())
    file.close()

upper_case()