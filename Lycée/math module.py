# Créé par t.hausmann, le 15/09/2022 en Python 3.7
"""
Auteur : Tom Hausmann
Date : 15/09/2022
But = calculer surface et périmètre d'un cercle
Input : rayon
Outputs : surface et perimetre
"""
import math
from math import cos, pi

pi = math.pi
rayon = int(input("Rayon du cercle : "))
perimetre = 2 * pi * rayon
surface = pi * rayon * rayon
print(perimetre)
print(surface)