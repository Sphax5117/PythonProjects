valeur =  {"joueur_1":[0,0], "joueur_2":[0,0], "joueur_3":[0,0]}

def acqui_entree():
    while True:
        entree = input("t")
        if entree in ("0", "1","2", "3", "4", "5", "6", "7","8", "9", "10", "11", "12"):
            return int(entree)
        print("mauvaise valeur")

def Mlk(valeur):
        while True:
            for i in valeur:
                a = acqui_entree()                    # commence le comptage de pts si score inferieur a 12
                valeur[i][0] += a
                valeur[i][1] = 0
                if valeur[i][0] == 50:                         # verifie si le score = à 50 et fait gagner la personne qui a win
                    print(i, "a gagné")
                    return valeur
                elif valeur[i][0] > 50:                        # vérifie si le score est supérieur à 50 puis le remet a 25
                    print("Score dépasse 50 : passe a 25")
                    valeur[i][0] = 25
                elif a == 0:                             # si le score d'un joueur est 0 ça ajoute un au compteur de zero
                    valeur[i][1] += 1
                    if valeur[i][1] == 3:                 # si le joueur a 3 zeros il est éliminé
                        print(i, "a perdu")                        
                        break
    


Mlk(valeur)