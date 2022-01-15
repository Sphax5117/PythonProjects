a = b = ""

while not(a.isdigit() and b.isdigit()):
    a = input("Give me a first number : ")
    b = input("Give me a second number : ")
    if not(a.isdigit() and b.isdigit()):
        print("Please enter two NUMBERS")
    else:
        c = int(a) + int(b)

print("The sum of " + a + " and " + b + " is " + str(c))