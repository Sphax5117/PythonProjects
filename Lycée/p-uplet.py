# Créé par t.hausmann, le 22/09/2022 en Python 3.7
jour = 15
mois = "décembre"
année = 2006
iden = (('Edouard', jour, mois, 2005), ('Jacque', jour, mois, 2002), ('Menes', jour, mois, 2003))
print(type(iden))
lenght = int(len(iden))
print(len(iden[0]))
print(iden[0][0])
for a in range(lenght):
    print(iden[a][3])

iden[0][0] = "Jean"
print(iden[0][0])