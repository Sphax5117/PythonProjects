# Créé par t.hausmann, le 14/11/2023 en Python 3.7

## a. Proposer les solutions pour :
## ✓ Consulter la position en x et en y d'un personnage par des accesseurs.
## ✓ Restreindre le gain ou la perte de PV par un mutateur en limitant à +50 le gain et à -10
## la perte.
##  ✓ Compléter la méthode del pour que compt renvoie bien le nombre d'objet toujours
## 'en vie

class Personnage:
    """On objet personnage définit par 3 atributs : sa position en x et en y, et
    ses PV
    """
    compte = 0
    def __init__(self):
        self.__X = 10  ## Variable en PRIVÉ, donc impossible à modifier depuis l'extérieur
        self.__Y = 30
        self.__PV = 20
        Personnage.compte += 1 ##La variable est définie à l'extérieur, donc dans
        ## la classe Personnage

    def get_PV(self):
        return self.__PV

    def set_x(self, X):
        self.__X == x
    def set_y(self, Y):
        self.__Y == y

    def deplacer(self, dx, dy):
        if dx + dy <= 6:
            self.__X += dx
            self.__Y += dy

    def __str__(self): ##est appellée quand on appelle print()
        return 'La position du personnage {} est ({}, {}) avec {} points de vie'.format(str(self.__X), str(self.__Y), str(self.__PV))

    ## Question A

    def get_Pos(self):
        return self.__X, self.__Y

    ## Question B

    def set_gain_Pv(self, gain):
        if gain <= 50 and gain > 0:
            self.__PV += gain
        else:
            return "/!\ Gain > 50 /!\ "

    def set_perte_Pv(self, perte):
        if perte >= -10 and perte < 0:
            self.__PV += perte
        else:
            return "/!\  Perte > 10 /!\ "



    def __del__(self): ## est appellée quand on appelle del()
        Personnage.compte -= 1
        print(Personnage.compte)



