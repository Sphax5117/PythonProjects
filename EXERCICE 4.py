# Créé par t.hausmann, le 11/09/2023 en Python 3.7
op = '(1*4) + 1)'

def controle(op):
    count = 0
    for i in range(len(op)):
        if op[i] == "(" or op[i] == ")":
            count += 1
    if (count % 2) == 0:
        print("True")
    else:
        print("False")

controle(op)