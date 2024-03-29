# Créé par t.hausmann, le 12/09/2023 en Python 3.7

## Question 1

# 1 Implementation de la Pile

def creerPileVide():
    pile = []
    return pile

def estVide(pile):
    if len(pile) == 0:
        return True
    else:
        return False

def empiler(pile, element):

    return pile.append(element)

def depiler(pile):
    return pile.pop()


# 2 Donner le contenu de la pile Q

#Le contenu devrait être [4,2,5,8]

# 3 Implémentation

def impl():
    pile = creerPileVide()
    P = [8,5,2,4]
    while not estVide(P):
        empiler(pile, depiler(P))
    print(pile)

    return pile

## Question 2
# 1 Recopier et compléter

def hauteur_pile(P):
    Q = creerPileVide()
    n = 0
    while not(estVide(P)):
        n += 1
        x = depiler(P)
        empiler(Q, x)
    while not(estVide(Q)):
        x = depiler(Q)
        empiler(P, x)

    return n

hauteur_pile([8,5,2,4])

# 2 fonction max_pile()

def max_pile(P, i):
    maxPos = 0
    max = 0
    for e in range(1, i + 1):
        if P[-e] > max:
            maxPos = e
            max = P[-e]
    print(maxPos)
    return maxPos

max_pile([8,5,2,4], 3)

# 3 fonction retourner()

def retourner(P, j):
    pileAux = []
    for e in range((len(P) - j)):
        pileAux.append(P[e])
    for i in range(1,j+1):
        pileAux.append(P[-i])

    print(pileAux)

retourner([8,5,2,4], 3)





