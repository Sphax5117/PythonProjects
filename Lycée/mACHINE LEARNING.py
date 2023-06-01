# Créé par t.hausmann, le 16/05/2023 en Python 3.7
import pandas
import csv
import matplotlib.pyplot as plt
import math


iris = pandas.read_csv("iris.csv")
x=iris.loc[:, "longueur_petale"]
y=iris.loc[:,"largeur_petale"]
lab=iris.loc[:, "espece"]
liste = list(zip(x,y,lab))
echan = [float(input("x : ")), float(input("y")), str(input("nom"))]


def dist_euclid(echan, liste):
    dist = []
    for i in range(len(liste)):
        distance = math.sqrt((echan[0] - liste[i][0])**2 + (echan[1] - liste[i][1])**2)
        dist.append([distance, liste[i][2]])
    dist = sorted(dist)
    return dist

dist_triee = dist_euclid(echan, liste)

def knn(dist_triee, k):
    voisins = [[0,0], [1,0], [2,0]]
    max = 0
    ##script fait par TOm Hausmann
    for i in range(k):
        if dist_triee[i][1] == 0:
            voisins[0][1] += 1
        elif dist_triee[i][1] == 1:
            voisins[1][1] += 1
        elif dist_triee[i][1] == 2:
            voisins[2][1] += 1
    for i in range(len(voisins)):
        if voisins[i][1] > max:
            max = voisins[i][1]
            echan = voisins[i][0]
    print(voisins)
    if echan == 0:
        esp = "Setosa"
        color = "g"
    elif echan == 1:
        esp = "Virginica"
        color = "r"
    elif echan == 2:
        esp = "Versicolor"
        color = "b"
    print("L'espèce est sûrement", esp)
    return color




colori = knn(dist_triee, 5)

plt.scatter(x[lab==0],y[lab==0], s=10, marker="^", color="g", label="setosa")
plt.scatter(x[lab==1],y[lab==1], s=10, marker="*", color="r", label="virginica")
plt.scatter(x[lab==2],y[lab==2], s=10, marker="x", color="b", label="versicolor")
plt.scatter(echan[0], echan[1], s=100, marker="+", color=colori, label=echan[2])
plt.legend()
plt.show()
