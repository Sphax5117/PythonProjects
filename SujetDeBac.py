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

impl()

## Question 2
# 1 Recopier et compléter

def hauteur_pile(P):
    Q = creerPileVide()
    n = 0
    while not(estVide(P))

