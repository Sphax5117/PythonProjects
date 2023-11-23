# Créé par t.hausmann, le 20/11/2023 en Python 3.7
class File:

    def __init__(self):

        self.corps = []

    def enfile(self,v):
        self.corps.insert(0, v)
        return self.corps

    def defile(self):
        return self.corps.pop()

    def est_vide(self):
        return self.corps == []

    def taille(self):
        return len(self.corps)

    def tete(self):
        if self.corps:
            return self.corps[0]


    def queue(self):
        if self.corps:
            return self.corps[-1]


    def __str__(self):
        a = ''
        for i in self.corps:
            a = a + str(i) + " | "
        a = "| "+a+" |"
        return a

    def __del__(self):
        """Détruit la file
        """