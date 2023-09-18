# Créé par t.hausmann, le 18/09/2023 en Python 3.7

def creer_file_vide():
    file = []
    return file

def est_vide(file):
    if len(file) == 0:
        return True
    else:
        return False

def enfile(file, element):
    file.insert(0, element)
    return file

def defile(file):
    last = file.pop()
    return last

## 2

# En vrai on fait len(file) et ça fait pareil

## 3

def variation(F):
    if len(F) == 1:
        return []
    else:
        tab = [0 for k in range (len(F) -1)]
        element1 = defile(F)
        for i in range(len(F)):
            element2= defile(F)

            tab[i] = int(element2) - int(element1)
            element1 = element2
            print(element1, element2)
    print(tab)
    return tab


def nombre_baisse(f):
    maxDown = 1000
    dayCount = 0
    for i in range(len(f) -1):
        if f[i] > f[i+1]:
            dayCount += 1
    for i in range(len(f)):
        if f[i] < maxDown:
            maxDown = f[i]

    print(dayCount, maxDown)
    return dayCount

nombre_baisse([1, -4, 2, -1, -2])