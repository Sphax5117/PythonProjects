# Créé par t.hausmann, le 10/11/2022 en Python 3.7
import random
aliceTry = []
bobTry = []

def lancer(nbLancer):
    alicePoint = 0
    bobPoint = 0
    for i in range(nbLancer):
        aliceTry.append(random.randint(1,6))
        bobTry.append(random.randint(1,6))
        if aliceTry[i] == 6:
            alicePoint += 0.5
        elif bobTry[i] == 6:
            bobPoint += 0.5

    print(aliceTry,bobTry, alicePoint, bobPoint)


lancer(10)








