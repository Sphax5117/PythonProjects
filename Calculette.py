a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("donne nb 1: ")
    b = input("donne nb 2 : ")
    if not (a.isdigit () and b.isdigit()):
        print("Veuillez entrez deux nb valides")

print(f"Le résultat de l'ad est {int(a) + int(b)}")