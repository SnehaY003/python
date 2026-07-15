def append_file():
    file =open("Example.txt", "a")

    file.write("City: Gurgaon\n")
    file.write("Mobile: XXXXXXXXXX\n")
    file.close()

append_file()