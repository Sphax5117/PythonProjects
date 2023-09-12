# Créé par t.hausmann, le 12/09/2023 en Python 3.7

lettre = "P"
mot = "informatiques"

def chiffrage(contenu):
    motChiffre = ""
    for i in range(len(contenu)):
        tempChar = ""
        r = ((3 * ord(contenu[i]) - 61) % 91) + 33

        c1 = chr(r)
        tempChar += c1
        if r % 2 == 0:
            c2 = ((2 * ord(c1) - 31) % 91) + 33
            tempChar += chr(c2)
            motChiffre += tempChar
        elif r % 2 != 0:
            c2 = ((2 * ord(contenu[i]) - 32) % 91) + 33
            tempChar += chr(c2)
            c3 = chr(((3 * ord(contenu[i]) - 60) % 91) + 33)
            tempChar += c3
            motChiffre += tempChar

    return motChiffre

def chiffrageMot(contenu):
    listeChiffre = {}
    motChiffre = ""
    for i in range(32, 123):
        listeChiffre[chr(i)] = str(chiffrage(chr(i)))
    for l in contenu:
        motChiffre += listeChiffre.get(l)

    print(motChiffre)
    return motChiffre

chiffrageMot(mot)