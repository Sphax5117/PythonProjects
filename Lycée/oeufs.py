# Créé par t.hausmann, le 15/09/2022 en Python 3.7

"""
Auteur : Tom Hausmann
Date : 15/09/2022
But : calculer le nombre de boites pour un nombre d'oeuf
Input : nombre d'oeuf
Outputs : nombre de boites
"""
oeufs = int(input("Combien d'oeufs avez vous : "))
nbBoites = oeufs // 6
if (oeufs % 6 > 0):
    nbBoites = nbBoites + 1
print(nbBoites)