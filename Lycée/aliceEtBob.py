# Créé par t.hausmann, le 10/11/2022 en Python 3.7
# coding __UTF8__
# BUT :  Créer un jeu de dé entre Alice et Bob, avec des lancers aléatoire
import random ## Le module qui permet de générer des nombres
import math
aliceTry = []
bobTry = []
alicePoint = 0
bobPoint = 0

def lancer():
    """
    Entrées : None
    Sorties : les lancers d'alice et bob (list)
    """
    for i in range(10):
        aliceTry.append(random.randint(1,6))
        bobTry.append(random.randint(1,6))

    print(f"Lancers d'Alice : {aliceTry} \nLancers de Bob : {bobTry}")
    return aliceTry, bobTry


while alicePoint < 10 and bobPoint < 10:
    """
    Cette boucle fait des lancers tant que le score de de l'un des deux n'est
    pas au dessus de 5 points (Donc 10, les points sont divisés par deux à la
    fin.
    """
    lancer()
    for i in range(len(aliceTry)):
        if aliceTry[i] == 6:
            alicePoint += 1
    for i in range(len(bobTry)):
        if bobTry[i] == 6:
            bobPoint += 1
    ## On parcourt la liste à chaque lancer, et on compte le nombre de 6
    aliceTry.clear()
    bobTry.clear()
    ## On supprime toutes les données de la liste pour la réutiliser ensuite
    if alicePoint == 12:
        alicePoint = alicePoint - 1
    if bobPoint == 12:
        bobPoint = bobPoint - 1
    ## On gère la "boucle en trop" en retirant un point, (ils ne peuvent pas
    ## avoir 6

    ## Impression des résultats
    print(f"Le nombre de point d'Alice est : {alicePoint // 2}")
    print(f"Le nombre de point de Bob est : {bobPoint // 2}")
    print("\n")

if bobPoint // 2 == alicePoint //2:
    print("Bob et Alice sont ex aequo")
elif alicePoint // 2 == 5:
    print("Alice a gagné !")
elif bobPoint // 2 == 5:
    print("Bob a gagné")












