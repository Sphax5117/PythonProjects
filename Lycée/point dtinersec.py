# Créé par t.hausmann, le 20/09/2022 en Python 3.7
from sympy import symbols, Eq, solve

x, y = symbols('x y')

a = float(input("Entrez a selon ax + b l'equation 1 : "))
b = float(input("Entrez b selon ax + b l'equation 1 : "))
c = float(input("Entrez c selon cx + d l'equation 2 : "))
d = float(input("Entrez d selon cx + d l'equation 2 : "))

eq1 = Eq(y, a * x + b)
eq2 = Eq(y, c * x + d)
if eq1 == eq2:
    print("Les solutions sont infinies, les droites sont confondues")
else:
    print(str(solve([eq1, eq2])))