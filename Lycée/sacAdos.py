### PSEUDO CODE
## (poids, valeur )
S = [{"poids":12, "valeur": 4}, {"poids":1, "valeur": 2}, {"poids":4, "valeur": 10}, {"poids":1, "valeur": 1}, {"poids":2, "valeur": 2},  {"poids":72, "valeur": 2}]

## Ici la valeur maximale 
## Le but est de remplir le sac à dos avec une valeur élevée et le moins de poids (poids étant limité) 
## on peut prendre un seul truc
## La solution est donc de remplir avec 3 * 4kg (donc 12kg valeur 30) et 3 * 1 kg (donc 3kg valeur 6)

def SaD(S, M):
    for object in S:
        object["valeur_poids"] = object["valeur"] / object["poids"]
    masse_sac = 0
    final = []
    j = 0
    liste_triee = sorted(S, key= lambda x:x["valeur_poids"])
    liste_triee.reverse()
    while j < len(liste_triee):
        if masse_sac + liste_triee[j]["poids"] <= M:
            masse_sac += liste_triee[j]["poids"]
            final.append([liste_triee[j]["poids"], liste_triee[j]["valeur"]])
        j += 1
        print("j : ", j)
        print("masse : ", masse_sac)
    print(final)
    return final




SaD(S, 20)