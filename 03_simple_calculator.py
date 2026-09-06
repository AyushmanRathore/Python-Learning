a = float(input("what is the first number to opperate: "))
b = float(input("what is the second number to opperate: "))
c = (input("what is the operation (+, -, *, /) you want to perform: ")).lower()

if c == "+" or c == "add" or c == "addition":
    print (a+b)

elif c == "-" or c == "subtract" or c == "subtraction":
    print(a-b)

elif c == "/" or c == "divide" or c == "division":
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(a/b)

elif c == "*" or c == "multiply" or c == "multiplication":
    print(a*b)   

else:
    print("Invalid operation")

# for the reecxecution of the code:

d =  input("do you want to calculate anything else with me? (yes or no): ").lower()
while d == "yes":
        print("ok, let's do it again")

        a = float(input("what is the first number to opperate: "))
        b = float(input("what is the second number to opperate: "))
        c = (input("what is the operation (+, -, *, /) you want to perform: "))

        if c == "+" or c == "add" or c == "addition":
            print (a+b)

        elif c == "-" or c == "subtract" or c == "subtraction":
            print(a-b)

        elif c == "/" or c == "divide" or c == "division":
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(a/b)

        elif c == "*" or c == "multiply" or c == "multiplication":
            print(a*b)   

        else:
            print("Invalid operation")

        d =  input("do you want to calculate anything else with me? (yes or no): ").lower()

while d == "no":
        print("sure,  tell me if there is anything you want to calculate with me in the future")
        break
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
