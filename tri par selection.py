#Created by Hausmann Tom on 06/12/2022
# coding _utf8_


nbr = [3,4,2,1,0,4,8,3,84,1]
def tri_select(nbr,choice):
    """
    But : Trier une liste de donnée par sélection
    Entrée : la liste, et le paramètre pour choisir le mode
    Sortie : la liste triée
    """
    if choice == "croissant":
        for i in range(len(nbr)):
            variant = len(nbr) - i
            print(variant)
            mini = i
            for j in range(i+1, len(nbr)):
                if nbr[mini] > nbr[j]:
                    index = j
                    nbr[mini], nbr[index] = nbr[index], nbr[mini]
    elif choice == "decroissant":
        for i in range(len(nbr)):
            maxi = i
            for j in range(i+1, len(nbr)):
                if nbr[maxi] < nbr[j]:
                    index = j
                    nbr[maxi], nbr[index] = nbr[index], nbr[maxi]



    print(nbr)

tri_select(nbr, "decroissant")
tri_select(nbr, "croissant")


