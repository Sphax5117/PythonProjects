# Créé par t.hausmann, le 23/11/2023 en Python 3.7
# CELLULE A
# Implémentation du jeu de la vie en POO
# -*- coding utf-8 -*-
import pyxel as px
from copy import deepcopy

class JdlV :
    def __init__(self, grille) :                           # constructeur de la class
        self.grille = grille                               # récupération de la grille
        self.grille_future = deepcopy(self.grille)         # fabrication de la grille de mise à jour
        px.init(len(self.grille[0]), len(self.grille), fps = 10, title = "Jeu de la vie")    # creation de la fenetre pyxel
        px.run(self.draw, self.update)                     # lancement de la fenetre pyxel

    def draw(self):
    #effacer l'ecran → voir cls() ds la doc de l'API
    #parcourir les y lignes de la grille :
    #parcourir les x colonnes de la grille :
    #attribuer une couleur pour les "0" et les "1" → voir pset() ds la doc de l'API
        col = 15
        col2 = 12
        col3 = 11
        px.cls(col)
        for y in range(len(grille_blinker)):
            for x in range(len(grille_blinker[y])):
                if grille_blinker[y][x] == 0:
                    px.pset(x,y,col2)
                elif grille_blinker[y][x] == 1:
                    px.pset(x,y, col3)


    def update(self):
        pass

    def nombre_voisines(self):
    ##initialiser le "nbr_voisines" à zéro
    ##déclarer la liste des voisines "voisines"
    ##parcourir les 8 voisines :
    ##tester si (y,x) est ds la grille et que grille[y][x] vaut 1 :
    #incrémenter "nbr_voisines"
    #renvoyer "nbr_voisines
        nbr_voisine = 0
        voisines = []



grille_blinker = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,1,1,1,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]

JdlV(grille_blinker)
