
# Créé par t.hausmann, le 11/05/2023 en Python 3.7
import random
from math import sqrt
S = [[1,0,3,0], [3,0,2,0], [0,0,4,0], [0,0,0,0]]
# Sudoku 4x4 - MP_Spé_NSI
# coding -*- utf-8 -*-

# Création de la grille ________________________________________
##S = [
##     [1,0,3,0] ,


# La fonction ligne ____________________________________________
def ligne(S, i) :
    """ renvoie la liste des chiffres d'une ligne i de S
        param S(list) la grille de sudoku
        param i(int) une ligne de la grille
        return l(list) ensemble des chiffres présents sur la ligne i
        de la grille S
    """
# ASSERTION sur i
    assert i > 0, "I doit être positif"
    l = []
    for n in range(len(S[i])):
        if S[i][n]>0:
            l.append(S[i][n])
    print(l)
    return l


ligne(S, 1)

# La fonction colonne ___________________________________________
def colonne(S, j) :
    """ renvoie la liste des chiffres d'une colonne j de S
        param S(list) la grille de sudoku
        param j(int) une colonne de la grille
        return l(list) ensemble des chiffres présents sur la colonne j
        de la grille S
    """
    assert j>0, "J doit être positif"
    l = []
    for n in range(len(S[j])):
        if S[n][j]>0:
            l.append(S[n][j])
    print(l)
    return l

colonne(S, 2)



# La fonction bloc ______________________________________________
def bloc(S, i, j) :
    """ renvoie la liste des chiffres d'un bloc identifier par l'une
        de ses cases (i, j)
        param S(list) la grille de sudoku
        param i(int) une ligne de la grille
        param j(int) une colonne de la grille
        return l(list) ensemble des chiffres présent dans le bloc
    """
    l = ...
    # calcul de h et g
    h = ...
    g
    # taille du côté du bloc carré
    t = int(sqrt(len(S)))
##    for ligne in (...) :
##        for colonne ...


# La fonction possibles ________________________________________________
def possibles (S, i, j) :
    """ Doc string à écrire
    """
##    l = ...
##    for x in ...
##        if not x in ligne(S,i) and ...
##            l. ...
##    return l

# La fonction suivante __________________________________________________
def suivante (i, j) :
    """ calcule les coordonnées de la case suivante
        param i(int) la ligne de la case actuelle
        param j(int) la colonne de la case actuelle
        return k(int) ligne de la case suivante
        return l(int) colonne de la case suivante
    """
    if j < 3 :
        k = ...
        l = ...
    elif j == ... :
        k = ...
        l = ...
    return (..., ...)


#La fonction résolution _____________________________________________
def resolution (S, i, j) :
    affiche()
##    if i == ... :
##        return True
##    elif ... :
##        k, l = ...
##        return resolution(S, k, l)
##    elif ...
##        for x in ...:
##            S[i][j] = ...
##            k, l = ...
##            if resolution(S, k, l) == True :
##                return True
##    S[i][j] = 0
##    return False

# Affichage console __________________________________________________
def affiche() :
    a='\n'
    for i in range (len(S[0])) :
        for j in range (len(S)) :
            a = a + str(S[i][j]) + "\t"
        a = a + "\n"
    print(a)

##resolution (S,0,0)

