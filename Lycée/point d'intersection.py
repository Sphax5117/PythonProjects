# Créé par t.hausmann, le 15/09/2022 en Python 3.7

import math
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d = int(input("d : "))

fx = a * 1 + b
gx = c * 1 + d
fresult = a * fx  + b
if (fx == gx):
    print("x : " + str(fx))
    print("y : " + str(fresult))

