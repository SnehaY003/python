try:
    file = open("data.txt", "w")
    text = input("Enter text: ")
    file.write(text)
    file.close()
    print("Data written successfully.")

except Exception as e:
    print("Error:", e)