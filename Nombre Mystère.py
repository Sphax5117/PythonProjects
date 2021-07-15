import random
import pyfiglet

print(pyfiglet.figlet_format("Le jeu du nombre mystere"))


essai = 5
mystery_number = random.randint(0, 100)
guess = input("Devine le nombre : ")

if not guess.isdigit:
    print("Veuillez rentrer des nombres !")



while True:

    if not guess.isdigit:
        print("Veuillez rentrer des nombres !")
        continue
    else:
        guess = int(guess)


    if mystery_number > guess :
        print(f"""Le nombre mystère est plus grand que {guess}..
        Il te reste {essai} essais !""")
        essai = essai - 1
        guess = input("Devine le nombre : ")

    if mystery_number < guess:
        print(f"""Le nombre mystère est plus petit que {guess}
                Il te reste {essai} essais !""")
        essai = essai - 1
        guess = input("Devine le nombre : ")
        
    if essai == 0:
        print(f"Mince... Tu as perdu ! Le nombre mystère était : {mystery_number}")
        break

    if mystery_number == guess:
        print(f"Bravo ! Tu as trouvé le nombre mystère en {essai} essais !")
        break

