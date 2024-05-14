# Créé par t.hausmann, le 19/12/2023 en Python 3.7
# Créé le 04/04/2023 en Python 3.7
# -*- coding utf-8 -*-
# algorithme de recherche textuelle
from time import perf_counter_ns

texte_1 = "Le langage de programmation Python a été créé en 1989 par Guido van Rossum, aux Pays-Bas. Le nom Python vient d’un hommage à la série télévisée Monty Python’s Flying Circus dont G. van Rossum est fan. La première version publique de ce langage a été publiée en 1991. La dernière version de Python est la version 3. Plus précisément, la version 3.7 a été publiée en juin 2018. La version 2 de Python est désormais obsolète et cessera d’être maintenue après le 1er janvier 2020. Dans la mesure du possible évitez de l'utiliser. La Python Software Foundation est l’association qui organise le développement de Python et anime la communauté de développeurs et d’utilisateurs. Ce langage de programmation présente de nombreuses caractéristiques intéressantes : Il est multiplateforme. C’est-à-dire qu’il fonctionne sur de nombreux systèmes d’exploitation : Windows, Mac OS X, Linux, Android, iOS, depuis les mini-ordinateurs Raspberry Pi jusqu’aux supercalculateurs. Il est gratuit. Vous pouvez l’installer sur autant d’ordinateurs que vous voulez (même sur votre téléphone !). C’est un langage de haut niveau. Il demande relativement peu de connaissance sur le fonctionnement d’un ordinateur pour être utilisé. C’est un langage interprété. Un script Python n’a pas besoin d’être compilé pour être exécuté, contrairement à des langages comme le C ou le C++. Il est orienté objet. C’est-à-dire qu’il est possible de concevoir en Python des entités qui miment celles du monde réel (une cellule, une protéine, un atome, etc.) avec un certain nombre de règles de fonctionnement et d’interactions. Il est relativement simple à prendre en main. Enfin, il est très utilisé en bioinformatique et plus généralement en analyse de données. Toutes ces caractéristiques font que Python est désormais enseigné dans de nombreuses formations, depuis l’enseignement secondaire jusqu’à l’enseignement supérieur"
chaine_adn = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTT"
adn = "CAATGTCTGCACCAAGACGC"
motif_adn = "ACCTTCG"
texte = "un papou papa à poux a des poux papas et des poux pas papas"
motif = "papou"

def horspool_dico(motif):
    j = 1
    dico = {}
    for i in range(0, len(motif)):
        dico[motif[i]] = len(motif) - j
        j += 1
    dico.pop(motif[-1])
    return dico


# Algorithme de BOYER_MOORE_HORSPOOL ----------------------------------------------------
def horspool (texte, motif) :
    """ recherche un motif dans un texte
        : param texte(str) le texte dans lequel on effectue la recherche
        : param motif(str) le motif recherché
        : return pos(list) liste des positions du motif dans le texte
        variables :
            i : position du caractère dans le "texte"
            j : position du caractère  dans le "motif"
            k : position du caractère du "motif" dans le "texte"
    """
    n = len(texte)
    m = len(motif)
    dic_decal = horspool_dico(motif)
    # algo de horspool
    i = m - 1                       # initialise i au dernier caractère de motif
    pos = []                      # liste des positions de l'occurence de motif ds texte
    while i < n:           # parcour texte de gauche à droite
        j = m - 1                    # curseur de motif
        k = i                     # curseur de texte
        while j >= 0 and texte[k] == motif[j] :
        # la comparaison est True
        # on décale les curseurs vers la gauche
            j -= 1
            k -= 1
        if j == -1:                # on a trouvé motif ds texte
            pos.append(k+1)                 # ajoute la position ds la liste
            i = i + m               # déplace le curseur i ds texte
        else :
            # le caractère de texte est ds motif
            if texte[k] in dic_decal :                       # le caractère est ds le dic_decal
                if k + dic_decal[texte[k]] > i :    # le décalage ne peut pas etre négatif
                    i = k + dic_decal[texte[k]]
                else :
                    i += 1                          # sinon
            # le caractère de texte n'est pas ds motif
            else :
                i += m -1                         # le décalage est de len(motif)
    print(pos)
    return pos

assert horspool(adn,"CAAT") == [0], "/!\ défaut horspool()"
assert horspool(adn,"TGCA") == [7], "/!\ défaut horspool()"
assert horspool(adn,"CAGT") == [], "/!\ défaut horspool()"
assert horspool(adn,"ACGC") == [16], "/!\ défaut horspool()"
assert horspool("CAATGTCTGCACCAATACGC","CAAT") == [0, 12], "/!\ défaut horspool()"
assert horspool(texte_1,"Python") == [28, 97, 150, 290, 392, 529, 607, 1246, 1423, 1761], "/!\ défaut horspool()"
assert horspool(chaine_adn,motif_adn) == [32], "/!\ défaut horspool()"




for i in range(4,100,10):
    S = [(randint(1,10), randint(5,10)) for j in range(i)]
    nb_objet.append(i)
    P = i*7
    d = perf_counter()
    sdTd(S,P)
    tps_TD.append(perf_counter() - d)
    m = perf_counter()
    sdBU(S,P)
    tps_BU.append(perf_counter() - m)



plt.clf()
plt.yscale("log")
plt.plot(nb_objet, tps_BU, '-',label = "Bottom Up", color='green')
plt.plot(nb_objet, tps_TD, '-',label = "Top Down", color='red')
plt.xlabel('valeur n')
plt.ylabel('Temps en ms')
plt.legend()
plt.show()