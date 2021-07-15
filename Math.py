Nombre = input("Insérez un nombre : ")
b = int(Nombre)

print(f"Le carré de {b} est {b ** 2}")

liste = [1, 2, 4, 5, "patate"]
liste.append(7)
liste.extend([10, 15, 25])
liste.remove(5)
print(liste)
print(liste[0:4])

nba = input("Insérez le premier nombre :")
nbb = input("Insérez un deuxième nombre :")
rep = int(nba) + int(nbb)
print("L'addition de " + nba + " et " + nbb + " est " + str(rep))

print(f"L'addition de {nba} et {nbb} est {int(nba) + int(nbb)}")

age = input("Quel est votre âge : ")

age = int(age)
if age >= 18:
    print("Vous êtes majeur")
elif age < 18:
    print("Vous êtes mineur")

for i in liste:
    print("Bonjour")

    
