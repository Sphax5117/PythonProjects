# Créé par t.hausmann, le 03/10/2023 en Python 3.7
from random import randint

def mini(L,d,f):
    """
    Renvoie le minimum d'une liste
    : param L (list), d indice 0 de la liste (int), f dernier indice(int)
    : return (int) le minimum
    >>> mini([23,12,4,56,35], 0, 4)
    4
    """

    if d == f:
        return L[d]
    else:
        m = (d+f)//2
        x = mini(L,d,m)
        y = mini(L, m+1, f)
        if x < y:
            return x
        else:
            return y


def rech_dicho_recur(L,v,d,f):
    """
    Algorithme de recherche dichotomique récursif
    : param L (list), v (int), d (int), f(int)
    : return m (int) indice de v
    >>> l =[5,8,12,25,54]
    >>> rech_dicho_recur(l, 8, 0, len(l) - 1)
    1
    >>> l =[5,8,12,25,54]
    >>> rech_dicho_recur(l, 32, 0, len(l) - 1)
    'Pas présent'

    """
    if d > f:
        return "Pas présent"
    else:
        m = (d+f)//2
        if L[m] > v:
            return rech_dicho_recur(L,v,d,m-1)
        elif L[m] < v:
            return rech_dicho_recur(L,v,m+1,f)
        elif L[m] == v:
            return m


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)

