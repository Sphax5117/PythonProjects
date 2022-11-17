# Créé par LaBo, le 18/10/2022 en Python 3.7
# -*- coding UTF-8 -*-
# COURS DICTIONNAIRE 1NSI
""" Un dictionnaire est une collection d'objets composé de paires clé : valeur.
    On accède aux valeurs par leur clé associée, les clés sont uniques et de type
    non mutable (int, str, tuple) alors que les valeurs peuvent être mutables.
    Une paire d'accolades crée un dictionnaire vide : {}
"""
##>>> dic = {}  instancie un dictionnaire
##>>> dic
##{}
##>>> type(dic)
##<class 'dict'> dict est un mot réservé
##
##>>> dics = {}
##>>> dics["Test"] = 1234
##>>> dics
##{'Test': 1234}
##>>> dics["Test"] renvoie la valeur associée à la clé
##1234
## Il faut noter que les valeurs sont classés par ASCII
## del(dic[Key])    Supprime une entrée
##len(dic)
# renvoie la taille de dic
## dic.keys()
# Renvoie toutes les clés du dictionnaire
##
##>>> list(dics.keys())
##['Test', 'Test2']
#renvoie toutes les clés sous forme de liste

##>>> list(dics.values())
##[1234, 5678]
#  renvoie toutes les valeurs sous forme de listes

##>>> list(dics.items())    renvoie les couples sous forme de liste
##[('Test', 1234), ('Test2', 5678)]

## dic.get("clé")       renvoie la valeur associée mais ne renvoie pas d'erreur

# Une autre méthode d'interrogation de liste
##>>> "toto" in dic
####False
##>>> "Test" in dic
####True
# Parcourir un dictionnaire avec une boucle
## >>> for cle in dic
## ... print(cle)
## ...
## 356
## [45,21,45]





# Exo 13 p74 du manuel numerique https://mesmanuels.fr/acces-libre/9782017158370
#France : Paris Allemagne : Berlin Italie : Rome Espagne : Madrid Irlande : Dublin Portugal : Lisbonne Belgique : Bruxelles Luxembourg : Luxembourg Pays-Bas : Amsterdam

capitales ={"France":"Paris", "Allemagne":"Berlin", "Italie":"Rome", "Espagne":"Madrid", "Irlande":"Dublin", "Portugal":"Lisbonne", "Belgique":"Bruxelles", "Luxembourg":"Luxembourg", "Pays-Bas":"Amsterdam"}
def villes(capitales, ville):
    for i in capitales: ## Pour chaque pays dans capitales ("i => la clé)
        if capitales[i] == ville: ## si la valeur associée (capitales[i]) est ville
            return i ## retourner le pays associé (i => la clé)

    return None ## Si pas trouvé, on retourne None


assert villes(capitales, "Berlin") == "Allemagne", "/!\ villes()"
assert villes(capitales, "Ankara") == None, "/!\ villes()"


# Exo 14 p74
personnes ={"Jean Aymar":{"taille":178,"pays":"USA","age":31},"Clio Patre":{"pays":"Portugal","age":32,"taille":179}}
def age(recherche, personnes):
    for i in personnes:
        if i == recherche:
            print(personnes[i]["age"])
            return personnes[i]["age"]
    return None

assert age("Jean Aymar", personnes) == 31, "/!\ age()"
assert age("Clio Patre", personnes) == 32, "/!\ age()"
assert age("Twin Go", personnes) == None, "/!\ age()"

def taille_moyenne(personnes):
    total = 0
    for i in personnes:
        total += personnes[i]["taille"]
    print(total / len(personnes))
    return total / len(personnes)

assert taille_moyenne(personnes) == 178.5, "/!\ taille_moyenne()"

# Exo 25 p76
#question a modifiée : implementer une fonction 'score' qui satisfasse les assertions suivantes
valeur_scrabble = {'kwxyz':10,'jq':8,'fhv':4, 'bcp':3, 'dmg':2,'aeilnorst':1}

def score(mot):
    """
    But : trouver le score au scrabble d'un mot
    Entrées : mot à trouver le nb de points
    Sorties : score final

    """
    score = 0
    for c in range(len(mot)):
        for i in valeur_scrabble:
            for b in range(len(i)):
                if i[b] == mot[c]:
                    score += valeur_scrabble[i]
    return score



assert score("pizza") == 25, "/!\ score ne marche pas"
assert score("whisky") == 36, "/!\ score ne marche pas"
assert score("dedramatiser") == 15, "/!\ score ne marche pas"

def alpha_scrabble(lettre):
    scoreLettre = {}
    for i in valeur_scrabble:
        for b in range(len(i)):
            if i[b] == lettre:
                scoreLettre = {i[b]:valeur_scrabble[i]}

    return scoreLettre

assert alpha_scrabble("a") == {'a':1}, "/!\ alpha_scrabble()"
assert alpha_scrabble("z") == {'z':10}, "/!\ alpha_scrabble()"

#question b modifiée : implémenter une fonction "alpha_scrabble" qui renvoie le dictionnaire du score
# de chaque lettre de la forme {"lettre":score}
# on peut utiliser le code ASCII pour accéder aux 26 lettres de l'alphabet !

def valeur_mot(mot):
    scoreFinal = 0
    for i in range(len(mot)):
        scoreFinal += alpha_scrabble(mot[i])[mot[i]]
        ## Retourne la valeur associée à la clé de la lettre.

    print(scoreFinal)

valeur_mot("pizza")


# question c : implémenter une fonction 'valeur_mot' qui renvoie la valeur du mot grace à lettres_scrabble

# QCM sur les dictionnaires https://genumsi.inria.fr/qcm.php?h=3496adcb0c0b409ca17b2c8a4a024ae7