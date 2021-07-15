a = "Bonjour je suis un dev".replace("jour", "soir").upper()
print(a)

b = input("Donnez une liste de nombre : ")
print(b)
c = "-".join(b.split(","))
c = "-".join(b.split(";"))
c = "-".join(b.split(" "))
print(c)

if "Image.jpg".endswith(".png"):
    print("L'image fini bien par png")
else:
    print("L'image ne fini pas par png")

if "Phota.png".startswith("Photo"):
    print("Le nom du fichier est bien photo")
else:
    print("Le nom du fichier n'est pas photo, veuillez changer son nom.")


print("50".isdigit())
print("Bonjour le jour".count("jour"))

