# Créé par t.hausmann, le 26/01/2023 en Python 3.7
Deuro = (1,2,5,10,20,50,100,200)

def RdM(S, D):

    assert S >= 0, "La somme à rendre doit être positive"
    i = len(D) - 1
    s = 0
    X = [0 for v in range(8)]
    while s < S:
        if D[i] <= (S - s):
            s =  s + D[i]
            X[i] += 1
        else:
            i = i -1
    return X

assert RdM(7, Deuro) == [0,1,1,0,0,0,0,0], "err"
assert RdM(844, Deuro) == [0,2,0,0,2,0,0,4], "err"
assert RdM(388, Deuro) == [1,1,1,1,1,1,1,1], "err"
assert RdM(0, Deuro) == [0,0,0,0,0,0,0,0], "err"


Deuro2 = (0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200)
Duk = (1,3,4,10,30,100,300,400)
Dusa = (0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100)
def RdM2(S, D):

    assert S >= 0, "La somme à rendre doit être positive"
    i = len(D) - 1
    s = 0
    X = [0 for v in range(len(D))]
    while s < S and i >= 0:
        if D[i] <= (S - s):
            s =  s + D[i]
            X[i] += 1
        else:
            i = i -1
    if D[i] > 0.009:
        X[0] += 1
    print(f"Pour {S} :")
    for i in range(0, len(X)):
            print(str(D[i]) + " € : " + str(X[i]) + " pièce / billet")
    print("\n")
    return X


def RdMProf(S,D):
    i = len(D) - 1
    s = 0
    X = [0]*(i+1)
    x = int(100*S) # On multiplie toute les devise par 100 (probleme float)
    while s < x:
        if int(100 * D[i]) <= (x-s): #si la valeur à l'index est plus petite
            s += int(100*D[i]) #on l'ajoute a la somme
            X[i] += 1 #on actualise l'index
        else:
            i -=1 #on décrémente i

    print(X)



RdM2(616, Duk)
## La façon optimale serait de rendre un billet de 400, deux billets de 100, un billet de 10, un pièce de 4 et deux pièce de 1
## Le système britannique est cannonique

RdM2(580, Deuro)


## Rendre un billet de 10, un billet de 5, un pièce de 2, 25 cents, un pièce de 10 cents et trois pièce de 0.01 $
## Le sytème américain est cannonique
RdM2(17.38, Dusa)

RdMProf(17.38, Dusa)




