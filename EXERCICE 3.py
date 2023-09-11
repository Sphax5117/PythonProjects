# Créé par t.hausmann, le 11/09/2023 en Python 3.7

opération = "5+2*3+4"

def separe(op):
    nombre= []
    opEleme = []
    op = list(op)
    for i in range(len(op)):
        if op[i].isdigit():
            nombre.append(int(op[i]))
        else:
            opEleme.append(str(op[i]))

    print(opEleme)
    print(nombre)

separe(opération)


