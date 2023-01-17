# Créé par t.hausmann, le 03/01/2023 en Python 3.7
# coding _utf-8_

## Question 1 => une liste

def fabric_grille():
    grille = [['-', '-', '-'] for i in range(3)]
    return grille

grille = fabric_grille()

def afficher_grille(grille):
    for i in range(3):

        print( '|' + str('|'.join(grille[i])) + '|')
    return grille[i]

def saisie(nom, grille, sign):
    couples = ('00','01','02','10','11','12','20','21','22')
    choice = input(f"{nom} ({sign}) => (format lignecolonne) : ")
    while choice not in couples:
        print("Erroné")
        choice = input(f"{nom} => (format lignecolonne) : ")
    if choice in couples and grille[int(choice[0])][int(choice[1])] == '-':
        grille[int(choice[0])][int(choice[1])] = sign
        afficher_grille(grille)


def test_grille(grille, sign):

    if grille[0] == [sign, sign, sign]:
        print(f"{sign} gagnant (1ere ligne)")
        return False
    elif grille[1] == [sign, sign, sign]:
        print(f"{sign} gagnant (2eme ligne)")
        return False
    elif grille[2] == [sign, sign, sign]:
        print(f"{sign} gagnant (2eme ligne)")
        return False
    elif grille[0][0] == sign and grille[1][0] == sign and grille[2][0] == sign:
        print(f"{sign} gagnant (1ere colonne)")
        return False
    elif grille[0][1] == sign and grille[1][1] == sign and grille[2][1] == sign:
        print(f"{sign} gagnant (2eme colonne)")
        return False
    elif grille[0][2] == sign and grille[1][2] == sign and grille[2][2] == sign:
        print(f"{sign} gagnant (3eme colonne)")
        return False
    elif grille[0][0] == sign and grille[1][1] == sign and grille[2][2] == sign:
        print(f"{sign} gagnant (premiere diago)")
        return False
    elif grille[0][2] == sign and grille[1][1] == sign and grille[2][0] == sign:
        print(f"{sign} gagnant (deuxième diago)")
        return False

def jeu():
    gr = afficher_grille(grille)
    joueur1 = input("Joueur 1 nom :")
    joueur2 = input("Joueur 2 nom :")
    a = test_grille(grille, "x")
    b = test_grille(grille, "o")
    while a != False or b != False:
        a = test_grille(grille, "x")
        b = test_grille(grille, "o")
        if a == False or b == False:
            break
        print("list avec -")
        saisie(joueur1, grille, "x")
        saisie(joueur2, grille, "o")


jeu()


