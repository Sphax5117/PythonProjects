from random import randint
from time import perf_counter

lst = [2,35,38,15,50,27,100,33]
def tri_insert(lst):
    """
    """
    for i in range(1,len(lst)): ## Parcours de la liste
        while i > 0 and lst[i] < lst[i-1]: ## si lst a la position i est plus petit qu'a celui d'avant
            lst[i-1], lst[i] = lst[i], lst[i-1] ## on échange les positions
            i = i - 1 #on décrémente i pour chercher la position "2,3,4,5.. fois avant"

    return lst

# tri_insert(lst)
tps_insert = []
for i in (10,100,1000,10000):
    lst = [randint(1,i) for j in range(i)]
    d = perf_counter()
    tri_insert(lst)
    tps_insert.append((i, round((perf_counter() - d) * 10 **6,0)))
for i in range(len(tps_insert)):
    print(f"pour {tps_insert[i][0]} éléments n : on met {tps_insert[i][1]} secondes")