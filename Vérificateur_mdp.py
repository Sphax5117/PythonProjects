mdp = input("Entrez un mdp ( min 8 caractères) ")
mdp_trop_court = "votre mdp est trop court."
mdp_nombre = "votre mdp ne contient que des nombres."

if mdp.isdigit():
    print(mdp_nombre.capitalize())
elif len(mdp)  == 0:
    print(mdp_trop_court.capitalize())
elif len(mdp) < 8:
    print(mdp_trop_court.upper())
elif len(mdp) >= 8:
    print("Inscription terminée !")