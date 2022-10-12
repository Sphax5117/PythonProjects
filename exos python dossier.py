# Créé par t.hausmann, le 06/10/2022 en Python 3.7
import numpy as np
import math

##########################Exercice 3#############################
#1)

from tkinter import N


def minimum(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min

assert minimum([-3,5,-9,-9,4]) == -9, "/!\ minimum"

#2)

def position_minimum(a):
    min = a[0]
    min_pos = 0
    for i in range(len(a)):
        if a[i] < min and a[i] != min:
            min = a[i]
            min_pos = i
    return min_pos

assert position_minimum([-3,5,-9,-9,4]) == 2, "/!\ position_minimum()"

#3)

def position_minimum_multiple(a):
    min_values = minimum(a)
    min_index = []
    # for i in range(len(a)):
    #     if a[i] <= min:
    #         min = a[i]
    #         min_pos.append(i)
    #     elif a[i-1] < a[i]:
    #         print(min_pos[i-1])
    #         print(i-1)
    #         min_pos.pop(i-1)
    for i in range(0, len(a)):
        if min_values == a[i]:
            min_index.append(i)

    return min_index
assert position_minimum_multiple([-3,5,-9,-9,4,4]) == [2, 3], "/!\ position_minimum_multiple()"

########################################Exercice 4 #########################

#1)

def maximum(a):
    maxi = a[0]
    for i in range(len(a)):
        if a[i] > maxi:
            maxi = a[i]
    return maxi

assert maximum([-3,5,-9,-9,4]) == 5, "/!\ maximum"

#2)

def position_maximum(a):
    maxi = a[0]
    max_pos = 0
    for i in range(len(a)):
        if a[i] > maxi:
            maxi = a[i]
            max_pos = i
    return max_pos

assert position_maximum([-3,5,-9,-9,4]) == 1, "/!\ position_maximum()"

#3)

def position_maximum_multiples(a):
    max_values = maximum(a)
    max_index = []
    for i in range(0, len(a)):
        if max_values == a[i]:
            max_index.append(i)

    return max_index

assert position_maximum_multiples([-3,5,-9,-9,4,5]) == [1, 5], "/!\ position_maximum_multiple()"

###################################Exercice 5############################

def moyenne(a):
    moyenne = sum(a)/len(a)

    return moyenne

assert moyenne([3,5,-9,2,4]) == 1, "/!\ moyenne()"

##################################Exercice 6############################

def moy_pond(valeurs, coefficients):
    productSum = 0
    efTotal = 0
    for i in range(len(valeurs)):
        productSum += valeurs[i] * coefficients[i]
    for i in range(len(coefficients)):
        efTotal += coefficients[i]
    moy_ponde = productSum/efTotal

    return moy_ponde

assert moy_pond([10,16,5], [1,0.5,2]) == 8, "/!\ moy_pond()"

###############################Exercice 7###############################

def moy_geom(nombres):
    xTimesx = 1
    for i in nombres:
        xTimesx = xTimesx*i
    n = len(nombres)
    moy = xTimesx ** (1/n)

    return round(moy)

assert moy_geom([2, 4, 8]) == 4, "/!\ moy_geom"



##############################Exercice 8 ###############################

#1)
def contient_valeur(a,b):
    isInList = False
    for i in range(len(a)):
        if a[i] == b:

            isInList = True

    return isInList

assert contient_valeur([3,5,2], 5) == True, "/!\ contient_valeur()"
assert contient_valeur([3,5,2], 0) == False, "/!\ contient_valeur()"

#2)

def position_valeur(a,b):
    index = None
    isInList = False
    for i in range(len(a)):
        if a[i] == b:
            index = a.index(a[i])
            isInList = True

    return index

assert position_valeur([5,3,5], 5) == 0, "position_valeur()"
assert position_valeur([5,3,5], 0) == None, "position_valeur()"

#3)

def position_valeur_mult(a,b):
    index = []
    isInList = False
    for i in range(0, len(a)):
        if b == a[i]:
            index.append(i)
            isInList = True

    return index

assert position_valeur_mult([3,5,5], 5) == [1,2], "position_valeur_mult"
assert position_valeur_mult([3,5,5], 0) == [], "position_valeur_mult"

###################### Exercice 9 ############################

def occurence(a,b):
    occur = 0
    for i in range(len(a)):
        if a[i] == b:
            occur += 1

    return occur

assert occurence([3,5,-9,5,4], 5) == 2; "occurence()"
assert occurence([3,5,-9,5,4], 1) == 0; "occurence()"

###################### Exercice 10###########################

#1)

def entremele(liste1, liste2):
    finaList = []
    for i in range(len(liste1)):
        finaList.append(liste1[i])
        finaList.append(liste2[i])
    return finaList

assert entremele([1,2,3], [5,6,7]) == [1,5,2,6,3,7]; "entremele()"

def entremele2(liste1, liste2):
    finaList = []
    listDif = 0
    for i in range(len(liste1)):
        finaList.append(liste1[i])
        finaList.append(liste2[i])
    if len(liste1) < len(liste2):
        listDif = len(liste2) - len(liste1)
        for i in range(listDif):
            finaList.append(liste2[i + 2])
    if len(liste1) > len(liste2):
        listDif = len(liste1) - len(liste2)
        for i in range(listDif):
            finaList.append(liste1[i + 2])
    return finaList


assert entremele2([1,2], [5,6,7,8]) == [1,5,2,6,7,8], "entremele2()"


########################### Exercice 11 ###########################

def decale_gauche(a):
    a.append(a.pop(0))
    """append a la fin de a la valeur que l'on fait 'sauter' a l'index
    0 (au début) """
    return a

assert decale_gauche([1,2,3]) == [2,3,1], "decale_gauche()"

def decale_droite(a):
    a.insert(0, a.pop(-1))
    """insere a l'index 0(au début) la valeur que l'on fait 'sauter' a l'index
    -1 (a la fin) """
    return a

assert decale_droite([1,2,3]) == [3,1,2], "decale_droite()"

########################## Exercice 12 ###############################

def decale_gauche_cran(a,n):
    for i in range(n):
        a.append(a.pop(0))
    """append a la fin de a la valeur que l'on fait 'sauter' a l'index
    0 (au début) """
    return a

assert decale_gauche_cran([1,2,3], 2) == [3,1,2], "decale_gauche_cran"
assert decale_gauche_cran([4,5,6], 2) == [6,4,5], "decale_gauche_cran"


def decale_droite_cran(a,n):
    for i in range(n):
        a.insert(0, a.pop(-1))
    """append a la fin de a la valeur que l'on fait 'sauter' a l'index
    0 (au début) """
    return a

assert decale_droite_cran([4,5,6], 2) == [5,6,4], "decale_gauche_cran"
assert decale_droite_cran([1,2,3], 3) == [1,2,3], "decale_gauche_cran"

########################## Exercice 13 #################################

########################## Exercice 14 ##################################

def mediane(valeurs):
    croissant = sorted(valeurs)
    mediane = 0
    middleNumber = int(len(croissant)/2)
    if len(croissant) % 2 == 0:
        mediane = (croissant[middleNumber -1] + croissant[middleNumber])/2
    elif len(croissant) % 2 != 0:
        mediane = croissant[math.ceil(len(croissant)//2)]

    return mediane



assert mediane([3,5,-9,4,4]) == 4, "/!\ mediane()"
assert mediane([1,2,3,4]) == 2.5, "/!\ fzfzef"

############################ Exercice 15 ###########################

def variance(x):
    '''
    Input/Output : liste de valeurs numériques(série statistique)/Variance
    But : Calculer la variance d'une liste statistique
    '''
    n = len(x)
    secondPart = 0
    for i in range(n): #sigma n=1 et i=1
         secondPart += (x[i] - moyenne(x))**2
    V = 1/n * secondPart
    return V

assert variance([1,2,3,4,5]) == 2.0, "/!\ variance()"

########################### Exercice 16 ##############################

def ecart_type(a):
    ecartT = math.sqrt(variance(a))
    return ecartT

assert ecart_type([1,2,3,4,5]) == 2**.5, "/!\ ecart_type()"


########################### Exercice 17 ###############################

def valeurs_sup(liste, valeur):
    valeurSup = []
    for i in range(len(liste)):
        if liste[i] >= valeur:
            valeurSup.append(liste[i])

    return valeurSup

assert valeurs_sup([1,2,3],1.5) == [2,3], "/!\ valeur_sup()"
assert valeurs_sup([1,2,3],4) == [], "/!\ valeur_sup()"

