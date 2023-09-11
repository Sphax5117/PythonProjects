# Créé par t.hausmann, le 11/09/2023 en Python 3.7

from collections import deque

liste = []
liste = deque()

def enfile(liste, tuple):
    for i in tuple:
        liste.appendleft(i)
    return list(liste)


