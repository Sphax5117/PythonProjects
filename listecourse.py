import pyfiglet
word = pyfiglet.figlet_format("Sphax")
print(word)
run_once = 0
choices = ["1", "2", "3", "4", "5"]
print("ATTENTION, veuillez à ne pas remmettre plusieurs fois le même élément !")
print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")

choix = input("-> Votre choix : ")
courses = []
while True:
    if choix not in choices:
        print("Veuillez entrer un nombre.")
        print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
        print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
        choix = input("-> Votre choix : ")

    if choix == "1"  :        
        ajout = input("Entrez le nom d'un élément à ajouter à votre liste : ")
        if run_once != ajout:
            courses.append(ajout)
            print(courses)
            print(f"L'élément {ajout} à bien été ajouté à la liste.")
            run_once = ajout
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        elif run_once == ajout:
            print(f"{ajout} est déjà dans votre liste.")
            print(courses)
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")

    if choix == "2":        
        rem = input("Entrez le nom de l'élément que vous voulez supprimer : ")        
        if rem in courses:
            courses.remove(rem)
            print(f"L'élément {rem} à été supprimé.")
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        else:
            print(f"L'élément {rem} n'est pas dans la liste.")
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")

    if choix == "3":
        if courses != []:
            print("   -   ".join(courses))
        else:
            print("Votre liste est vide !")
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        show = 1
        if show == 1:
            show = 0
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        
    if choix == "4":
        if courses != []:
            courses.clear
            print("Votre liste à étée vidée.")
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        else:
            print("Votre liste est vide !")
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")

    if choix == "5":
        quitt = input("Etes vous sûr de quitter ? o/n ")
        if quitt == "o":
            quit()
        elif quitt == "n":
            print("------------------------------------------------- \n Choisissez parmi les 5 options suivantes :")
            print(" 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter")
            choix = input("-> Votre choix : ")
        elif quitt == "prout":
            print("BRAVO ! TU AS TROUVE MON EASTER EGG !")

















    