import cmath
z1 = -4j/3  
z2 = 2j
if cmath.phase(z1) == cmath.phase(z2):
    print("Les deux nombres ont le même point image sur le cercle trigonométrique.")
else:
    print("Les deux nombres ont des points images différents sur le cercle trigonométrique.")
