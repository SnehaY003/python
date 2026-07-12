def palindrome(text):
    return text==ans[::-1]

ans=input("enter string: ")
if palindrome(ans):
    print("Palindrome")
else:
    print("Not palindrome")