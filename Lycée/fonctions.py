# Créé par t.hausmann, le 22/09/2022 en Python 3.7
import math
import random

""" Ce script décrit les bases des fonctions. A noter que les constantes
s'écrivent en MAJUSCULE
"""

def fonctionfonction(x):
    """La fonction renvoie le résultat de 1/1+x^2"""
    assert -1 <= x <+ 1, "X n'est pas compris entre -1 et 1"
    R = 1/x + x**2
    return R

x = float(input("Entrez votre x (-1 <= x <+ 1) : "))
print(f"Le résultat est : {fonctionfonction(x)}")

def perim_surface(r):
    assert r > 0, "votre rayon est <= 0"
    PERIMETRE = 2*math.pi*r
    SRF = math.pi*r**2
    return PERIMETRE, SRF


rInput = float(input("Entrez votre rayon : "))
perim,srf = perim_surface(rInput)

print(f"le perim de votre cercle est {perim}")
print(f"la surface de votre cercle est {srf}")

def mean_notes():
    LISTE = [random.randint(5,20) for i in range(35)]
    SUM = 0
    for i in range(35):
        SUM += LISTE[i]
    FINALMEAN = SUM/35
    return round(FINALMEAN)

print(f"La moyenne est de : {mean_notes()}")
