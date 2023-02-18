# Créé par l.bonnaud, le 01/02/2023 en Python 3.7
# -*- coding utf-8 -*-
# Jeu de plateforme

niveau1 = [0, 0, 1, 2, 0, 0, 1, 0, 1, 1, 2, 1, 0, 0]
niveau2 = [0, 0, 2, 3, 0, 0, 1, 0, 1, 1, 2, 1, 0, 0]

# question a
niveau2[1] = 1
niveau2[3] = 2


# question b
def conforme(niveau):
    """ vérifie la conformité d'un niveau : un index et son suivant doivent
        avoir un écart >= -1 et <= 2 pour que le niveau soit conforme
        param : niveau(list) liste des hauteurs successives du niveau
        return : (bool)
    """
    assert type(niveau) == list,"le type() de 'niveau' n'est pas conforme"
    result = True
    for i in range(len(niveau) - 1):
        if niveau[i] - niveau[i + 1] >= -1 and niveau[i] - niveau[i + 1] <= 2:
            result = True
        else:
            result = False
            return result
    return result


assert conforme([0, 0, 1, 0, 1, 2, 2, 3, 3, 4, 2, 1, -1, -2, -2]) == True,"/!\ defaut conforme()"
assert conforme([0, -2, -1, -1, -1, 0, 0, -2, -2, -1, -1, 0, -2, -3, -2]) == True,"/!\ defaut conforme()"
assert conforme([0, -1, -1, -1, 0, 1, 3, 1, 2, 2, 0, -1, 0, 1, 1]) == False,"/!\ defaut conforme()"
assert conforme([0, 0, 1, 0, 1, 2, 2, 3, 3, 4, 1, 1, -1, -2, -2]) == False,"/!\ defaut conforme()"

# question c

## Car on cherche à comparer avec l'index suivant, si on met len(niveau), on aura un index out of range

# question d
def difficulte(niveau) :
    """
    retourne la difficulté du niveau, qui se calcule en faisant la somme des écarts en valeur absolue
    param: niveau (list) des hauteurs sucessives
    return: (int)
    """
    S = 0
    for i in range(len(niveau) - 1):
        S += abs(niveau[i] - niveau[i + 1])
    return S

assert difficulte(niveau1) == 10, "/!\ defaut difficulte()"
assert difficulte([0, 1, 2, 0, 1, 2, 2, 3, 3, 4, 2, 1, -1, -2, -2]) == 14, "/!\ defaut difficulte()"
assert difficulte([0, -2, -3, -2, -1, 0, 0, -2, -3, -2, -1, 0, -2, -3, -2]) == 16, "/!\ defaut difficulte()"

# question e
niveau3 = [(0,0), (0,0), (1,1), (2,0), (0,2), (0,0), (1,1), (0,0), (1,3), (1,0)]
niveau3[8] = (1,1)



# question f et g
def score(niveau,n) :
    """
    Renvoie le score maxima (déjà acquis) par le joueur si il ne s'est pas fait éliminer entre temps en fonction de sa position (n)
    param: niveau (list) des hauteurs sucessives; position (int) du joueur
    return: score maximal (int) possible
    """
    assert n <= len(niveau), "/!\ n > longueur du niveau"
    S = 0
    for i in range(n + 1):
        if niveau[i][1] > 0:
            S += niveau[i][1]
    return S

assert score(niveau3,0) == 0, "/!\ defaut score()"
assert score(niveau3,9) == 5, "/!\ defaut score()"
assert score(niveau3,6) == 4, "/!\ defaut score()"

# question h
meilleurs_scores = {'Alice': 25, 'Bob': 18, 'John': 63, 'Alan': 21}

meilleurs_scores['Alice'] = 32

# question i
# La fonction compare les scores de tout les joueurs et retourne le nom du joueur au plus grand score, et celui au plus petit

# question j
def bon_niveau(records):
    X = []
    for nom in records:
        if records[nom] >= 20:
            X.append(nom)
    return X

assert bon_niveau({'Alice': 12, 'Bob': 18, 'Tima': 63, 'Alan': 20}) == ['Tima', 'Alan'], "/!\ defaut bon_niveau()"
assert bon_niveau({'Greg': 16, 'Bab': 26, 'Tino': 12, 'Gab': 17}) == ['Bab'], "/!\ defaut bon_niveau()"