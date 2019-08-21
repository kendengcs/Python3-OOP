import random

#b = random.randint(1,5)
b = 20
while True:
    a = int(input("Please input a number from 1-100: "))

    if (a==b):
        print("You made it!")
        break
    elif a > b:
        print("Too large, try again")
    else:
        print("Too small, try again")