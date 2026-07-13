def display_tuple(t):
    for item in t:
        print(item)

t = tuple(input("Enter tuple elements: ").split())

display_tuple(t)