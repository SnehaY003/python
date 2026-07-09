import random
ran = random.randint(1, 100)
while True:
    N=int(input("guess number: "))
    if ran > N:
        print("Too High")
    elif ran < N:
        print("Too Low")
    else:
        print("Correct! You guessed it.")
        break