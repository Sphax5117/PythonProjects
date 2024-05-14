# Créé par t.hausmann, le 05/12/2023 en Python 3.7

## d => Montrer que la valeur optimale est 12

## Pour une liste : S = ( (9, 10, 1.11), (12, 7, 0.58), (2, 1, 0.5), (7, 3, 0.43), (5, 2, 0.4) ).
## Avec (p,v,d)

## La valeur optimale est 12, soit l'élément 1 et l'élément 5 car, leur poids est
## 9 + 5 = 14 < 15 et leur valeur est 12, ce qui est la plus grande possible

from random import randint
from time import perf_counter
import matplotlib.pyplot as plt

def sd(S,P,i):
    """
    Calcule la valeur optimale d'une solution au problème du sac à dos.

    Cette fonction est une implémentation récursive pour résoudre le problème du sac à dos.
    Elle calcule la valeur maximale que l'on peut obtenir avec une capacité de sac donnée.

    Args:
        S (list of tuples): Liste de triplets (poids, valeur, ratio) des éléments.
        P (int): Poids maximal que le sac à dos peut supporter.
        i (int): Index de l'élément actuel à considérer dans la liste.

    Returns:
        int: Valeur optimale que l'on peut obtenir avec la capacité donnée du sac à dos.
    """
    if i == 0:
        return 0
    if S[i-1][0] > P: # Si Pi > P :
        return sd(S,P,i-1)
    elif i > 0:
        return max(S[i-1][1] + sd(S, P-S[i-1][0], i-1), sd(S,P, i-1))


S = ((5,7),(3,1),(3,4),(3,2))
assert sd(S, 10, len(S)) == 11, "/!\ défaut sd()"
S = ((5,2),(7,3),(2,1),(12,7),(9,10))
assert sd(S, 15, len(S)) == 12, "/!\ défaut sd()"


def sdTd(S,P):
    """
    Implémente une solution top-down du problème du sac à dos en utilisant la programmation dynamique.

    Cette version utilise la récursivité avec une mémoire (Memoization) pour améliorer l'efficacité.

    Args:
        S (list of tuples): Liste de tuples (poids, valeur) des éléments.
        P (int): Poids maximal que le sac à dos peut supporter.

    Returns:
        int: Valeur optimale pour la capacité donnée du sac à dos.
    """
    n = len(S)
    Memo = []
    for i in range(n+1):
        Memo.append([None]*(P + 1))
    return sdTDRec(S, P, n, Memo)

def sdTDRec(S, P, i, Memo):
    """
    Fonction récursive pour la solution top-down du problème du sac à dos.

    Args:
        S (list of tuples): Liste de tuples (poids, valeur) des éléments.
        P (int): Poids maximal actuel du sac à dos.
        i (int): Index de l'élément actuel à considérer.
        Memo (list of lists): Tableau de mémoire pour stocker les résultats intermédiaires.

    Returns:
        int: Valeur optimale pour la capacité actuelle et l'ensemble d'éléments.
    """
    vi = S[i-1][1]
    pi = S[i-1][0]
    if Memo[i][P] == 0: #solution pas calculée
        if i == 0:
            return 0
        elif pi > P:
            Memo[i][P] = sdTDRec(S,P,i-1,Memo)
        else:
            Memo[i][P] = max(sdTDRec(S, P, i-1, Memo), vi + sdTDRec(S, P-pi, i-1, Memo))
    return Memo[i][P]

S = [(5, 7), (3, 1), (3, 4), (3, 2)]



def sdBU(S,P):
    """
    Implémente une solution bottom-up du problème du sac à dos en utilisant la programmation dynamique.

    Cette version construit la solution de manière itérative à partir de sous-problèmes plus petits.

    Args:
        S (list of tuples): Liste de tuples (poids, valeur) des éléments.
        P (int): Poids maximal que le sac à dos peut supporter.

    Returns:
        list: Liste des éléments à inclure pour obtenir la valeur optimale.
    """
    n = len(S)
    Memo = []
    Result = []
    for i in range(n+1):
        Memo.append([0]*(P + 1))
    for i in range(1,n+1):
        for c in range(P+1):
            if S[i-1][0] > c:
                Memo[i][c] = Memo[i-1][c]
            else:
                Memo[i][c] = max(Memo[i-1][c], S[i-1][1] + Memo[i-1][c - S[i-1][0]])
    for i in range(n, 0, -1):
        if Memo[i][c] != Memo[i-1][c]:
            Result.append(S[i-1])
            c = c - S[i-1][0]
    return Result



##assert sdBU(((5,7),(3,1),(3,4),(3,2)),10) == 11, "Defaut zebi"

def sdTDPrint(S, P):
    """
    Affiche les éléments sélectionnés pour obtenir la valeur optimale dans le problème du sac à dos.

    Utilise une approche top-down avec programmation dynamique pour déterminer les éléments à inclure.

    Args:
        S (list of tuples): Liste de tuples (poids, valeur) des éléments.
        P (int): Poids maximal que le sac à dos peut supporter.

    Returns:
        list: Liste des éléments à inclure pour obtenir la valeur optimale.
    """
    n = len(S)
    Memo = []
    Result = []
    c = P
    for i in range(n+1):
        Memo.append([0]*(P + 1))
    sdTDRec(S,P,n, Memo)
    for i in range(n, 0, -1):
        if Memo[i][c] != Memo[i-1][c]:
            Result.append(S[i-1])
            c = c - S[i-1][0]
    return Result



nb_objet = []
tps_TD = []
tps_BU = []
for i in range(4,100,10):
    S = [(randint(1,10), randint(5,10)) for j in range(i)]
    nb_objet.append(i)
    P = i*7
    d = perf_counter()
    sdTd(S,P)
    tps_TD.append(perf_counter() - d)
    m = perf_counter()
    sdBU(S,P)
    tps_BU.append(perf_counter() - m)



plt.clf()
plt.yscale("log")
plt.plot(nb_objet, tps_BU, '-',label = "Bottom Up", color='green')
plt.plot(nb_objet, tps_TD, '-',label = "Top Down", color='red')
plt.xlabel('valeur n')
plt.ylabel('Temps en ms')
plt.legend()
plt.show()


