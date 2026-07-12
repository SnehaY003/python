from ast import Return


def vowels_count(string):
    ans=0
    for ch in string.lower():
        if ch in "aeiou":
            ans+=1
    
    return ans

text=input("Enter text: ")
print ("Vowels =",vowels_count(text))