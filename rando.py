# Créé par t.hausmann, le 27/04/2023 en Python 3.7
import csv ##Importe le module csv qui permet de lire les fichiers csv
import matplotlib.pyplot as plt

entree = open("rando_init.csv", "r") ##ouvre le fichier "Rando_init.csv"
Rando = list(csv.reader(entree)) ##transforme les valeur du fichier en liste
## dans la variable Rando
entree.close ##conserve les valeurs dans la variable, même si le nom change et
##ferme le fichier

def crea_list(Rando):
    alti = []
    dist = []
    n= len(Rando) - 1
    for i in range(n):
        alti.append(int(Rando[i + 1 ][0]))
        dist.append(float(Rando[i + 1][1]))
    return (alti, dist)

alti, dist = crea_list(Rando)
crea_list(Rando)

def deniveles(alti):
    deniCumuPos = 0
    deniCumuNeg = 0
    maxAlt = 0
    for i in range(len(alti) - 1):
        if (alti[i+1] - alti[i]) > 0:
            deniCumuPos += (alti[i+1] - alti[i])
        if (alti[i + 1] - alti[i]) < 0:
            deniCumuNeg += (alti[i+1] - alti[i])
        if alti[i] > maxAlt:
            maxAlt = alti[i]
    print("Le denivelé positif est de :", deniCumuPos, "m")
    print("Le denivelé négatif est de :", abs(deniCumuNeg), "m")
    print("L'altitude max est :", maxAlt, "m")
    return(deniCumuNeg, deniCumuPos, maxAlt)


def cumul_distance(dist):
    cumul = [dist[0]]
    for i in range(len(dist) - 1):
        cumul.append(cumul[i] + dist[i + 1])
    return(cumul)





deniveles(alti)
cumul = cumul_distance(dist)


def profil_alti(alti, cumul):
    "Trace le profil altimétrique de rand_init.csv"
    x = cumul
    y = alti
    plt.xlabel("Distance")
    plt.ylabel("Altitude")
    plt.grid(color='grey', linestyle='-', linewidth=0.3)
    plt.title("Profil altimétrique")
    plt.plot(x, y)
    plt.show()

def ecrire_csv(Rando, cumul):
    n = len(Rando) - 1
    for i in range(n):
        Rando[i + 1][1] = round(cumul[i],2)
    print(Rando)
    sortie = open("rando_final.csv", "w")
    ecrire=csv.writer(sortie, dialect='excel')
    for i in range(len(Rando)):
        ecrire.writerow(Rando[i])
    sortie.close
    return None

def vitesse_moyenne(cumul):
    vit = float(input("Entrez une vitesse moyenne (entre 3 et 6.5km/h: ")) * 1000
    all = sum(cumul)
    assert vit >= 3000 and vit <= 6500, "VITESSE INCORECTE"
    tps = vit/all
    print(tps)


##profil_alti(alti, cumul)
ecrire_csv(Rando, cumul)
vitesse_moyenne(cumul)