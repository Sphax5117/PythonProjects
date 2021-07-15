import pyfiglet
import random

print(pyfiglet.figlet_format("Pendu"))

tryy = 0

gamemode = input("Tapez 1 pour jouer contre l'ordinateur, 2 pour jouer à deux : ")

if gamemode == "1":
    mots = ["angle", "armoire", "banc", "bureau", "cabinet", "carreau", "chaise", "classe", "clé", "coin", "couloir", "dossier", "eau", "école", "écriture", "entrée", "escalier", "étagère", "étude", "extérieur", "fenêtre", "intérieur", "lavabo", "lecture", "lit", "marche", "matelas", "maternelle", "meuble", "mousse", "mur", "peluche", "placard", "plafond", "porte", "portemanteau", "poubelle"]
    print("-"*70)
    print("Trois difficultés sont disponibles : Facile (8 fautes max), Normal (6 fautes max) et Difficile (4 fautes max)")   
    dif = input("Choissisez votre difficulté (1, 2 ou 3): ")
    if dif == "1":
        tryy = 8
    if dif == "2":
        tryy = 6
    if dif == "3":
        tryy == 4
    word_to_guess =  random.choice(mots)
    print(word_to_guess)
    print(f"Il vous reste {tryy} essais")
    lorw = input("Donnez une letre ou le mot")

    while lorw == word_to_guess:
        if lorw == word_to_guess[0]:
            print("Vous avez trouvé une lettre !")

