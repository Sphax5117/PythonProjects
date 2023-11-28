# Créé par t.hausmann, le 28/11/2023 en Python 3.7
import pyxel as px
from copy import deepcopy

class JdlV :
    def __init__(self, grille):
            px.init(100, 100, fps = 10, title = "Jeu de la vie")
            self.grille = [[0 for x in range (px.width)] for y in range (px.height)]
            self.grille_future = deepcopy(self.grille)
            self.grille = self.pattern()
            # lancement de la fenetre
            px.run(self.draw, self.update)
##        self.grille = grille                               # récupération de la grille
##        self.grille_future = deepcopy(self.grille)         # fabrication de la grille de mise à jour
##        px.init(len(self.grille[0]), len(self.grille), fps = 10, title = "Jeu de la vie", quit_key = px.KEY_ESCAPE)    # creation de la fenetre pyxel
##        px.run(self.draw, self.update)

    def draw(self):
        col = 15
        col2 = 12
        col3 = 11
        px.cls(col)
        for y in range(len(self.grille)):
            for x in range(len(self.grille[y])):
                if self.grille[y][x] == 0:
                    px.pset(x,y,col2)
                elif self.grille[y][x] == 1:
                    px.pset(x,y, col3)

    def nombre_voisines(self, y, x):
        nbr_voisine = 0
        voisine = [(y-1, x-1), (y-1,x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1)]
        for i in range(len(voisine)):
            if voisine[i][0] >= 0 and voisine[i][0] < len(self.grille) and voisine[i][1] >= 0 and voisine[i][1] < len(self.grille) and self.grille[voisine[i][0]][voisine[i][1]] == 1:
                    nbr_voisine += 1
        return nbr_voisine

    def update(self):
        self.grille_future = deepcopy(self.grille)
        for y in range(len(self.grille)):
            for x in range(len(self.grille[y])):
                nbr_voisine = self.nombre_voisines(y, x)
                if self.grille[y][x] == 0 and nbr_voisine == 3:
                    self.grille_future[y][x] = 1
                elif self.grille[y][x] == 1 and (nbr_voisine == 2 or nbr_voisine == 3):
                    self.grille_future[y][x] = 1
                else:
                    self.grille_future[y][x] = 0
        self.grille = deepcopy(self.grille_future)

    def pattern(self):
        """ insère le pattern 'pat' au milieu de la grille
            disponible à https://conwaylife.com/wiki/Category:Patterns
        """
        fichier = open("truc.cells", "r")
        liste = fichier.readlines()
        # conversion du *.cells en [[] [] ... ]
        pat =[]
        for i in liste :
            if i[0] != '!' :
                ligne = []
                for j in i :
                    if j == '.' :
                        ligne.append(0)
                    elif j == 'O':
                        ligne.append(1)
                pat.append(ligne)
        # taille de pat
        h_pat = len(pat)
        w_pat = max([len(pat[i]) for i in range(len(pat))])
        # point d'insertion du pattern 'pat' dans la grille
        pt_insert = ((px.height-h_pat)//2, (px.width-w_pat)//2)   # au format [y][x]
        y_insert = 0        # parcourt les lignes
        while y_insert < h_pat :
            x_insert = 0    # parcourt les colonnes d'une ligne
            while x_insert < len(pat[y_insert]) :
                self.grille[pt_insert[0]+y_insert][pt_insert[1]+x_insert] = pat[y_insert][x_insert]
                x_insert += 1
            y_insert += 1
        return self.grille

grille_blinker = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,1,1,1,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]

JdlV(grille_blinker)

