# Créé par t.hausmann, le 20/11/2023 en Python 3.7

class File_Cir:


    def __init__(self, _taille):
        self._taille = _taille
        self._corps = [None] * (self._taille - 1)
        self.tete = 0
        self._queue = 0
        self._attente = 0


    def enfile(self,v):
        self._corps[self._queue] = v
        self._queue = (self._queue+1)% self._taille
        return self._corps

    def defile(self):
            c = self._corps.pop(self.tete)
            self.tete = (self.tete)% self._taille
            return c

    def est_vide(self):
        return self._corps == []

    def taille(self):
        return len(self._corps)


    def file_attente(self):
        return self._attente

    def __str__(self):
        a = ''
        for i in self._corps:
            a = a + str(i) + " | "
        a = "| "+a+" "
        return a

    def purger(self):
        pass
