# Créé par l.bonnaud, le 22/11/2022 en Python 3.7
# -*- coding UTF-8 -*-
# Mini projet sur les dictionnaires Premiere Spe NSI
texte0 = open("file2.txt", "r")   #ouvre le fichier.txt
texte1 = texte0.read()                                          #converti en str
##texte2 = texte1.replace('\n',' ')
texte2 = texte1.lower()                                         #bascule les MAJ en min
texte0.close()

def cpt_ltr():
    texte3Len = 0 ##Le nombre de lettres de l'alphabet dans le texte
    lettres = {}
    for a in texte2:
        lettres[a] = lettres.get(a,0)+1 ## pour chaque char dans le txt,
    lettres = dict(lettres)
    for i in range(97,123):
        if chr(i) not in lettres:
            continue
        texte3Len += lettres[chr(i)]
    for i in range(97,123):
        if chr(i) not in lettres:
            continue
        percent = (lettres[chr(i)] * 100) / texte3Len
        print(f"{chr(i)} : {round(percent, 2)} %")

def cpt_ltr2():
    lettersCount = {}
    for c in texte2:
        for i in range(97,123):
            if c == chr(i):
                lettersCount[c] = lettersCount.get(c,0)+1
            else:
                continue
    print(lettersCount)
    for i in range(97,123):
        if chr(i) in lettersCount:
            percent = (lettersCount[chr(i)] * 100) / sum(lettersCount.values())
        else:
            continue
        print(f"{chr(i)} : {round(percent, 2)} %")








    """ Ecrire une fonction cpt_ltr() qui prend en paramètre la chaine de caracteres
    (tous minuscules) 'texte2' et affiche dans la console le pourcentage de
    présence de chacune des lettres dans le texte. Le resultat est de la forme :
        % des lettres présentes dans le texte :
        e  :  15.71 %
        s  :  9.3   %
        t  :  7.58  %
        a  :  7.57  %

    on ne compte pas les ponctuations !

    on peut reconnaitre les lettres minuscules par leur code ASCII

    on peut trier un dictionnaire en le convertisant en list puis trier la list
    avec : list.sort(key=lambda x: x["values"], reverse = True)
"""
cpt_ltr()
print("\n")
cpt_ltr2()