try:
    file=open("a.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")