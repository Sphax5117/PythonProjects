leave = True


def leaving():
    qds = input("Type 1 if you want to leave, else type any char : ")
    if qds == "1":
        quit()
    else:
        leave = True;


print("Welcome to the version 2.0 of my calculator !")
print("---------------------------------------------")
while leave is True:
    choice = input("Type 1 for addition, 2 for subtractions, 3 for multiplication and 4 for division : ")
    if not (choice.isdigit()):
        print("Please enter a NUMBER")
    else:
        if choice == "1":
            a = b = ""
            print("Welcome to the addition program")
            while not (a.isdigit() and b.isdigit()):
                a = input("Give me a first number : ")
                b = input("Give me a second number : ")
                if not (a.isdigit() and b.isdigit()):
                    print("Please enter two NUMBERS")
                else:
                    c = int(a) + int(b)

            print("The sum of " + a + " and " + b + " is " + str(c))
            leaving()
        if choice == "2":
            a = b = ""
            print("Welcome to the subtraction program")
            while not (a.isdigit() and b.isdigit()):
                a = input("Give me a first number : ")
                b = input("Give me a second number : ")
                if not (a.isdigit() and b.isdigit()):
                    print("Please enter two NUMBERS")
                else:
                    c = int(a) - int(b)

            print("The difference between " + a + " and " + b + " is " + str(c))
            leaving()
        if choice == "3":
            a = b = ""
            print("Welcome to the multiplication program")
            while not (a.isdigit() and b.isdigit()):
                a = input("Give me a first number : ")
                b = input("Give me a second number : ")
                if not (a.isdigit() and b.isdigit()):
                    print("Please enter two NUMBERS")
                else:
                    c = int(a) * int(b)

            print("The product of " + a + " and " + b + " is " + str(c))
            leaving()
        if choice == "4":
            a = b = ""
            print("Welcome to the division program")
            while not (a.isdigit() and b.isdigit()):
                a = input("Give me a first number : ")
                b = input("Give me a second number : ")
                if not (a.isdigit() and b.isdigit()):
                    print("Please enter two NUMBERS")
                else:
                    c = int(a) / int(b)

            print("The quotient of " + a + " and " + b + " is " + str(c))
            leaving()
