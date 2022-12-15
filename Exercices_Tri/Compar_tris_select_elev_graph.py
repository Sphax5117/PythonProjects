#tri par sélection
from time import perf_counter
from random import randint
import matplotlib.pyplot as plt

##lst1=[randint(10,100) for i in range (10)]
lst1=[2, 35, 38, 15, 50, 27, 100, 33]

def tri_select(lst):
    n=len(lst)
    for i in range (n):
        min = lst[i]
        index = i
        for j in range (i+1,n):
            if lst[j]<min :
                min = lst[j]
                index=j
        if lst[i]>lst[index]:
            lst[i],lst[index]=lst[index],lst[i]
    return lst

def tri_select2(lst):
    lst_triee=[]
    while len(lst)>0 :
        lst_triee.append(lst.pop(lst.index(min(lst))))
    return lst_triee

##        mini = min(lst)
##        index=lst.index(mini)
##        x = lst.pop(index)
##        lst_triee.append(x)


# graphique d'évolution des temps de calculs
# listes des valeurs
         # axe y2                    # axe x
# boucle pour fabriquer les valeurs des axes :
#   x de 200 à 5 000 par pas de 200
#   y1 temps de calcul de 'tri_select'
#   y2 temps de calcul de 'tri_select2'
taille = []
for i in range(100,5000,100):
    taille.append(i)        # ajoute i pour l'axe x
    # une liste de i valeurs aléatoires entre 10 et 100 000
tps_select = []             # axe y1
tps_select2 = []
for i in taille:
    lst=[randint(10,100000) for j in range(i)]
    # AXE Y1
    t_actuel = perf_counter()        # mémorise le temps actuel en µs
    tri_select(lst)                  # lance la fonction de tri 'tri_select'
    # ajoute le temps de calcul pour l'axe y1
    tps_select.append(round(1000*(perf_counter()-t_actuel),0))
    # AXE Y2
    t_actuel = perf_counter()        # mémorise le temps actuel en µs
    tri_select2(lst)                  # lance la fonction de tri 'tri_select'
    # ajoute le temps de calcul pour l'axe y1
    tps_select2.append(round(1000*(perf_counter()-t_actuel),0))
# matplotlib (plt) : bibliothèque pour tracer des graphiques voir ecole directe
# pour la documentation
# traduire en python les lignes suivantes ##

##  supprime les tracés précédents
plt.clf()
##  ajoute le nom de l'axe x
plt.xlabel("Secondes")
##  trace l'axe y1 (liste axe x, liste axe y1, style de ligne, nom du tracé, couleur)
plt.plot(taille, tps_select, '-.', label='tri_select', color='blue')
plt.plot(taille, tps_select2, '-.', label='tri_select2', color='red')
##  trace l'axe y2 (liste axe x, liste axe y2, style de ligne, nom du tracé, couleur)
##  ajoute un titre au graphique
plt.title("Représentation")
##  ajoute les légendes
##  affiche le graphique
plt.show()