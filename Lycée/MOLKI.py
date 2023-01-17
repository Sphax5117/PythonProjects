# a. Dictionnaire
from copy import deepcopy
valeur =  {"joueur_1":0, "joueur_2":0, "joueur_3":0}

def MlK(valeur):
    win = False
    j = None
    nbr0 = {"joueur_1":0, "joueur_2":0, "joueur_3":0}       # dictionnaire comptant les 0 de chaque joueur
    while win == False:
        for i in valeur:
            inpt = int(input(f"{i} :"))
            if inpt <= 12:                                  # commence le comptage de pts si score inferieur a 12
                valeur[i] += inpt
                if valeur[i] == 50:                         # verifie si le score = à 50 et fait gagner la personne qui a win
                    print(i, "a gagné")
                    return valeur
                elif valeur[i] > 50:                        # vérifie si le score est supérieur à 50 puis le remet a 25
                    print("Score dépasse 50 : passe a 25")
                    valeur[i] = 25
                    print(valeur)
                elif inpt == 0:                             # si le score d'un joueur est 0 ça ajoute un au compteur de zero
                    nbr0[i] += 1
                    print(nbr0[i])
                    if nbr0[i] == 3:
                        j = i                        # si le joueur a 3 zeros il est éliminé
                        print(i, "a perdu")                        
                        break
            else:
                print("valeur doit petre inférieure à 12")  
                print(f"{valeur}")
        if j != None and len(valeur) == 3:
            del(valeur[j])
            print(valeur)                   
        if len(valeur) == 1:
            
            print(''.join([keys for keys in valeur]), " a gagné")
            return valeur


MlK(valeur)