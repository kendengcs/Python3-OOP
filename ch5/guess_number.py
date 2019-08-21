import random

b = random.randint(1,99)
while True:
    a = int(input("Please input a number from 1 to 99"))
    if (a == b):
        print("Great, you made it!")
        break
    elif a > b :
        print("It's too large, try again~")
    else:
        print("It's too small, try again~")