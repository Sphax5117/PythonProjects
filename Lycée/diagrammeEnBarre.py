# Créé par t.hausmann, le 10/11/2022 en Python 3.7

def ajoute_espace(mot, longueur):
    return mot.ljust(longueur)

assert ajoute_espace('Anne', 7) == 'Anne   '
assert ajoute_espace('Luc', 7) == 'Luc    '
assert ajoute_espace('nsi',3) == 'nsi'
assert ajoute_espace('', 2) == '  '

def taille_max(categories):
    maxLen = 0
    for i in range(len(categories)):
        if len(categories[i]) > maxLen:
            maxLen = len(categories[i])
    return maxLen

assert taille_max(['Anne','Luc', 'Patrick', 'Sam']) == 7
assert taille_max(['tri', 'boucle', 'fonction', 'test']) == 8
assert taille_max(['isotopes', 'mercure', 'ballerines', 'covalence']) == 10



