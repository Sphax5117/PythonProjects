# Créé par t.hausmann, le 16/11/2023 en Python 3.7
from POO_Pile import *

def verif(E):
    global pile #Variable Globale (consultable)
    pile = Pile()
    valid = True
    for i in E:
        if i == "(":
            pile.empile("(")
        elif i == ")":
            if pile.get_taille() == 0:
                valid = False
            else:
                top = pile.get_sommet()
                pile.depile()
    if valid == True:
        print("L'expression est bien parenthésée")
    else:
        print("L'expression est mal parenthésée")


E = '36+(25*96)/(89-34))'
verif(E)