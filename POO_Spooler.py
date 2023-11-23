# Créé par t.hausmann, le 20/11/2023 en Python 3.7
from POO_File_Cir import *

spooler = File_Cir(5)
spooler.enfile("Fichier1")
spooler.enfile("Fichier2")
spooler.enfile("Fichier3")
spooler.enfile("Fichier4")
print(spooler, '\n')

while spooler.est_vide() == False:
    imp = spooler.defile()
    print("Le document ", imp, " est en cours d'impression")
    print("Il reste ", spooler.taille(), " documents en attente")
    if spooler.est_vide() == False:
        print("La file d'attente est :", spooler, "\n")
    else:
        print("Fini")