to_sort = [1,5,8,6,8,4,7,6,3,45,6,9]

def min(liste):
    min = liste[0]
    for value in liste:
        if value < min:
            min = value
    return min

def max(liste):
    max = liste[0]
    for value in liste:
        if value > max:
            max = value
    return max

def tri_selection(liste):
    for i in range(len(liste)):
        mini = i
        for j in range(len(liste)):
            if liste[i] < liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    print(liste)

    return liste

def tri_insertion(liste):
    for i in range(len(liste)):
        while i > 0 and liste[i] < liste[i - 1]:
            liste[i], liste[i - 1] = liste[i - 1], liste[i]
            i = i -1 
    print(liste)


tri_selection(to_sort)
tri_insertion(to_sort)
min(to_sort)
max(to_sort)