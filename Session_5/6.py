def count(sentence):
    words=sentence.split()
    return len(words)

s=input("Enter a sentence: ")
print("Number of words:",count(s))