import random


pv_ennemi1 = 60
pv_ennemi2= 50
pv_joueur = 50
potions = 3
attaque_ennemi = random.randint(5, 15)
attaque_joueur = random.randint(5, 11)
attaque_joueurboss = random.randint(10, 13)
vie_potion = random.randint(15, 30)
godmodepv = 500
godmodeatq = random.randint(0, 1000)
#-----------------------Petite mise en scène----------------        

print("""Bonjour et bienvenue ! Vous êtes entré dans un donjon mystérieux !\nDeux portes s'offrent à vous, l'une avec un gros monstre (1), l'autre avec un monstre plus petit (2)!""")
demande_porte = input("Quelle porte choisissez vous (1 ou 2): ")


#----------------------------Ennemi 1 (fort) -----------------------

if demande_porte == "1":
    print("-"*100)
    print("Vous êtes courageux aventurier ! Voyons si vous arrivez à vous défaire de cet ennemi !")
    print("L'ennemi a 60pv ! Vous en avez 50 !")
    while True:
        if pv_ennemi1 <= 0 and pv_joueur > 0:
            print("Bravo, vous avez vaincu cet ennemi !")
            break
        elif pv_joueur <= 0 and pv_ennemi1 > 0:
            print(f"Vous avez perdu... Il reste {pv_ennemi1} pv à l'ennemi.")
            break
        elif pv_joueur <= 0 and pv_ennemi1 <= 0:
            print("Vous avez perdu dans la gloire, en vaincant l'ennemi !")
            break
        atq_ou_pot = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
        if atq_ou_pot == "1":

            pv_ennemi1 = pv_ennemi1 - attaque_joueurboss
            pv_joueur = pv_joueur - attaque_ennemi
            print(f"Vous avez infligé {attaque_joueurboss} dégats à l'ennemi !")
            print(f"L'ennemi vous a infligé {attaque_ennemi} dégats !")
            if pv_joueur > 0:
                print(f"Il vous reste {pv_joueur} points de vie.")
            else:
                print("Vous n'avez plus de points de vie...")
            
            if pv_ennemi1 > 0 :
                print(f"Il reste {pv_ennemi1} points de vie à l'ennemi ...")
            else:
                if pv_joueur > 0:
                    print("L'ennemi n'a plus de pv !")
            print("-"*100)
        if atq_ou_pot == "2" and pv_joueur <= 50:
            if potions > 0:
                pv_joueur = pv_joueur + vie_potion
                if pv_joueur > 50:
                    print("Vous avez trop de pv pour faire ça !")
                    pv_joueur = 50
                else:
                    potions = potions - 1
                    print(f"Vous avez récupéré {vie_potion} point de vie.")
                    print(f"Vous avez utilisé une potion ! Il vous en reste {potions}")
                    pv_joueur = pv_joueur - attaque_ennemi
                    print(f"Il vous reste {pv_joueur} points de vie.")
                    print(f"Il reste {pv_ennemi1} points de vie à l'ennemi ...")
                    print("-"*100)
            else:
                print("Vous n'avez plus de potions !")
                print("-"*100)

#-------------------------------Ennemi 2 ( faible )---------------------       
if demande_porte == "2":
    print("-"*100)
    print("Vous avez donc choisi l'ennemi le moins fort... Compréhensible.")
    print("L'ennemi a 50 pv, vous en avez 50 également !")
    while True:
        if pv_ennemi2 <= 0 and pv_joueur > 0:
            print("Bravo, vous avez vaincu cet ennemi !")
            break
        elif pv_joueur <= 0 and pv_ennemi2 > 0:
            print(f"Vous avez perdu... Il reste {pv_ennemi2} pv à l'ennemi.")
            break
        elif pv_joueur <= 0 and pv_ennemi2 <= 0:
            print("Vous avez perdu dans la gloire, en vaincant l'ennemi !")
            break
        atq_ou_pot = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
        if atq_ou_pot == "1":

            pv_ennemi2 = pv_ennemi2 - attaque_joueur
            pv_joueur = pv_joueur - attaque_ennemi
            print(f"Vous avez infligé {attaque_joueur} dégats à l'ennemi !")
            print(f"L'ennemi vous a infligé {attaque_ennemi} dégats !")
            if pv_joueur > 0:
                print(f"Il vous reste {pv_joueur} points de vie.")
            else:
                print("Vous n'avez plus de points de vie...")
            
            if pv_ennemi1 > 0 :
                print(f"Il reste {pv_ennemi2} points de vie à l'ennemi ...")
            else:
                if pv_joueur > 0:
                    print("L'ennemi n'a plus de pv !")
            print("-"*100)
        if atq_ou_pot == "2" and pv_joueur <= 50:
            if potions > 0:
                pv_joueur = pv_joueur + vie_potion
                if pv_joueur > 50:
                    print("Vous avez trop de pv pour faire ça !")
                    pv_joueur = 50
                else:
                    potions = potions - 1
                    print(f"Vous avez récupéré {vie_potion} point de vie.")
                    print(f"Vous avez utilisé une potion ! Il vous en reste {potions}")
                    pv_joueur = pv_joueur - attaque_ennemi
                    print(f"L'ennemi vous a infligé {attaque_ennemi} dégats !")
                    print(f"Il vous reste {pv_joueur} points de vie.")
                    print(f"Il reste {pv_ennemi2} points de vie à l'ennemi ...")
                    print("-"*100)
            else:
                print("Vous n'avez plus de potions !")
                print("-"*100)