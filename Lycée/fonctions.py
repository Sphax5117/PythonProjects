# Créé par t.hausmann, le 22/09/2022 en Python 3.7
def calcul_carré(nb):
    '''Calcule le carré du nombre donné
    Si le carré est plus grand que 10 impossible (test assert)'''
    assert nb>=10, "Le nombre est plus grand que 10"
    nbcarré = nb * nb
    return nbcarré

a = calcul_carré(5)
b = calcul_carré(11)
print(a)
print(b)
print(calcul_carré(11))