#Created by Hausmann Tom on 06/12/2022
# coding _utf8_
from time import perf_counter
from random import randint
lst =[randint(10,100000) for i in range(10000)]


nbr = [2,35,38,15,50,27,100,33]
def tri_select(nbr):
    """
    But : Trier une liste de donnée par sélection
    param : la liste
    Sortie : la liste triée
    """
    for i in range(len(nbr)):
        mini = i    
        for j in range(i+1, len(nbr)):
            if nbr[mini] > nbr[j]:
                index = j
                nbr[mini], nbr[index] = nbr[index], nbr[mini]
    return nbr



def tri_select2(lst):
    """
    But : Trier une liste de donnée par sélection
    param : (list)
    Sortie : (list) La liste triée
    """
    n = len(lst)
    lst_triee = []
    for i in range(n-1):
        variant = n - i 
        mini = min(lst)
        lst.remove(mini)
        lst_triee.append(mini)
        if lst_triee[i] == mini:
            invariant = True
    

# tri_select2(nbr)



d = perf_counter()
x = tri_select(lst)
z1 = round((perf_counter()- d),2)
print("temps tri_select : ", z1 ," s")

d = perf_counter()
x = tri_select2(lst)
z2 = round((perf_counter()- d),2)
print("temps tri_select2 : ", z2," s")

if z1 < z2:
    print("tri_select est plus performant")
elif z2 < z1:
    print("tri_select2 est plus performant")