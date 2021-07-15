while True:
    conti = input("Voulez vous continuer ? o/n ")
    if conti == "n":
        quit()
    if conti != "o":
        print("Tu n'a pas rentré o ou n !")
    if conti == "o":
        print("On continue !")