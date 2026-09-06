import random
a = random.randint(1,100)
b = int(input("guess a number between 1 and 100: "))
if b<1 or b>100:
    print("please select a number between 1 to 100 only")
elif b==a:
    print("yayyy! you got it right!")
elif b>a:
    print("my number is lower than your guess.")
elif b<a:
    print("my number is higher than your guess.")


while b != a:
    b = int(input("please try again: "))

    if b < 1 or b > 100:
        print("please select a number between 1 to 100 only")

    elif b==a:
        print("yayyy! you got it right!")

    elif b>a:
        print("my number is lower than your guess.")

    elif b<a:
        print("my number is higher than your guess.")










