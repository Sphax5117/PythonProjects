# Créé par t.hausmann, le 14/11/2023 en Python 3.7

class Pile:
    """Implémentation basique d'une pile"""

    def __init__(self):
        self.__corps = []

    def est_vide(self):
        return self.__corps == []

    def get_taille(self):
        taille = len(self.__corps)
        return taille

    def get_sommet(self):
        sommet = self.__corps[-1]
        return sommet

    ## Question b
    def empile(self, V):
        self.__corps.append(V)
        print(self.__corps)

    def depile(self):
        self.__corps.pop()
        print(self.__corps)

    def __str__(self):
        return 'La Pile est : {}'.format(str(self.__corps))

