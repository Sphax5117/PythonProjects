# Créé par t.hausmann, le 03/01/2023 en Python 3.7
# coding _utf-8_

## Question 1 => une liste

def fabric_grille():
    grille = [[0, 0, 0] for i in range(3)]
    return grille

grille = fabric_grille()
couples = ('00','01','02','10','11','12','20','21','22')

def afficher_grille(grille):
    for i in range(3):
        print(grille[i])


def saisie(nom, grille, couples):
    choice = input(f"{nom} choix (format lignecolonne) : ")
    while choice not in couples:
        print("Erroné")
        choice = input(f"{nom} choix (format lignecolonne) : ")
    if choice in couples and grille[int(choice[0])][int(choice[1])] == 0:
        afficher_grille(grille)









afficher_grille(grille)
saisie("Tom", grille, couples)