# Créé par t.hausmann, le 13/10/2022 en Python 3.7
# -*- coding UTF-8 -*-


################################## Exercice 19 ###############################
def permute(liste, i, j):
    """
    permute deux valeurs dans une liste d'index i et ji
    :param (list) la liste à permuter
    :return (list) la liste après permutation
    """
    liste.insert(i, liste.pop(j))
    liste.insert(j, liste.pop(i+1))

    return liste
assert permute([4,0,2,-1], 0, 3) == [-1, 0, 2, 4], "/!\ permute"

def renverse(liste):
    '''
    Renvoie une liste des éléments à l'envers
    :param (liste) la liste à renverser
    :return (liste) la liste renversée
    '''
    listeRetournee = []
    for i in range(len(liste)):
        listeRetournee.append(liste[-i - 1])
    return listeRetournee

assert renverse([4,0,2,-1]) == [-1,2,0,4], "/!\ renverse()"

################## Exercice 20 #############################

def somme_vecteur(vecteur1, vecteur2):
    '''
    Fais la somme des vecteurs, quel que soit leur nombre de dimensions
    :param (list,list) Les vecteurs à additioner
    :return (list) La somme de ces vecteurs
    '''
    vecteurAdditiones = []
    assert len(vecteur1) - len(vecteur2) == 0, "/!\ Les vecteurs n'ont pas la dim"
    for i in range(len(vecteur1)):
        vecteurAdditiones.append(vecteur1[i] + vecteur2[i])

    return vecteurAdditiones

assert somme_vecteur([1,2,3,4], [5,6,7,8]) == [6,8,10,12], "/!\ somme_vecteur()"

def produit_vecteur_reel(coordonees, reel):
    ''' Fais le produit d'un vecteur par un réel quel que soit la dimension
    de celui ci
    :param (list, int) Les coordonées du vecteur et le réel
    :return (list) Les coordonées du vecteur final
    '''
    vecteurMultiplies = []
    for i in range(len(coordonees)):
        vecteurMultiplies.append(coordonees[i] * reel)

    return vecteurMultiplies

assert produit_vecteur_reel([1,2,3,4], -2) == [-2,-4,-6,-8], "/!\ ERROR"

############################### Exercice 21 ################################

def est_croissant(liste):
    '''
    Indique si la liste entrée est croissante
    :param (liste) la liste à vérifier
    :return (bool) la vérification
    '''
    croissant = False
    for i in range(len(liste) - 1):
        if liste[i] < liste[i+1]:
            croissant = True
        else:
            croissant = False

    return croissant

assert est_croissant([1,2,3]) == True, "/!\ est_croissant()"
assert est_croissant([1,3,2]) == False, "/!\ est_croissant()"

def est_decroissant(liste):
    '''
    Indique si la liste entrée est décroissante
    :param (liste) la liste à vérifier
    :return (bool) la vérification
    '''

    decroissant = False
    for i in range(len(liste) - 1):
        if liste[i] > liste[i+1]:
            decroissant = True
        else:
            decroissant = False

    return decroissant

assert est_decroissant([3,2,1]) == True, "/!\ est_decroissant()"

######################## Exercice 22 ############################

def diff_succesives(valeurs):
    '''
    Donne la différence succesives entre les valeurs
    param: (list) La liste de valeur
    return: (list) La liste des différences succesives
    '''
    diff = []
    for i in range(len(valeurs) - 1):
        diff.append(valeurs[i+1] - valeurs[i])
    return diff


assert diff_succesives([15,20,22,18,18,20]) == [5,2,-4,0,2], "/!\ diff()"

###################### Exercice 23 #############################

def plus_longue_suite_croissante():


