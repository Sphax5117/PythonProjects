# a. Dictionnaire
from copy import deepcopy
valeur =  {"joueur_1":[0,0], "joueur_2":[0,0], "joueur_3":[0,0]}

def inpt():
    while True:
        inpt = int(input(f"input : "))
        if inpt >= 0 or inpt <= 12:
            return inpt
        print("retry")

def MlK(valeur):
    win = False
    j = None   
    while win == False:
        for i in valeur:
            inpt()                    # commence le comptage de pts si score inferieur a 12
            valeur[i][0] += inpt()
            valeur[i][1] = 0
            if valeur[i][0] == 50:                         # verifie si le score = à 50 et fait gagner la personne qui a win
                print(i, "a gagné")
                return valeur
            elif valeur[i][0] > 50:                        # vérifie si le score est supérieur à 50 puis le remet a 25
                print("Score dépasse 50 : passe a 25")
                valeur[i][0] = 25
            elif inpt == 0:                             # si le score d'un joueur est 0 ça ajoute un au compteur de zero
                valeur[i][1] += 1
                if valeur[i][1] == 3:
                    j = i                        # si le joueur a 3 zeros il est éliminé
                    print(i, "a perdu")                        
                    break

        print(valeur)  
        if j != None and len(valeur) <= 3:
            del(valeur[j])
            print(valeur)                   
        if len(valeur) == 1:
            print(''.join([keys for keys in valeur]), " a gagné")
            return valeur
MlK(valeur)