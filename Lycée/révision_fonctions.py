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

def tri_insertion(liste):
    for i in range(len(liste)):
        while i > 0 and liste[i] < liste[i - 1]:
            liste[i], liste[i - 1] = liste[i - 1], liste[i]
            i = i -1
    print(liste)
    return liste

def tri_selection(liste):
    for i in range(len(liste)):
        mini = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[mini]:
                liste[j], liste[mini] = liste[mini], liste[j]

    return liste



tri_insertion(to_sort)
tri_selection(to_sort)
min(to_sort)
max(to_sort)