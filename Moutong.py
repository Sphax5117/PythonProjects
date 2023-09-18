    # Créé par t.hausmann, le 14/09/2023 en Python 3.7

def saute(case):
    """ Fait sauter le mouton présent dans la case en modifiant
    le jeu et l'historique, enregistrés en variables globales
    """
    global jeu, historique
    if jeu[case]=="B" and case<6 and jeu[case+1]=="O":
        jeu[case], jeu[case+1] = "O", "B"
    elif jeu[case]=="B" and case<5 and jeu[case+1]=="N" and jeu[case+2]=="O":
        jeu[case], jeu[case+2] = "O", "B"
    elif jeu[case]=="N" and case>0 and jeu[case-1]=="O":
        jeu[case], jeu[case-1] = "O", "N"
    elif jeu[case]=="N" and case>1 and jeu[case-1]=="B" and jeu[case-2]=="O":
        jeu[case], jeu[case-2] = "O", "N"

    historique.append(jeu.copy())

def undo():
    """ Remet la variable globale jeu à la dernière position enregistrée
    en utilisant la variable globale historique
    """
    global jeu, historique
    if len(historique) == 1:
        jeu = ["B", "B", "B", "O", "N", "N", "N"]
    else:
        jeu = historique[-2]
        historique.pop()