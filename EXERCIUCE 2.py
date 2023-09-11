# Créé par t.hausmann, le 07/09/2023 en Python 3.7
taille = ['XS', 'S', 'M', 'L', 'XL', 'XXL']

p = 8

def prix(taille, p):
    result = {}

    for i in range(len(taille)):
        if i == 0:
            result[taille[0]] = p
        else:
            result[taille[i]] = p + 2
            p += 2
    print(result)

prix(taille, p)
