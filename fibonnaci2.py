import pyfiglet

print(pyfiglet.figlet_format("La suite de fibonacci"))

def fibonnaci(n):
    if (n <= 1):
        return n
    else:
        return (fibonnaci(n -1) + fibonnaci(n -2))

n = int(input("Combien d'occurences voulez vous : "))

print("La suite de fibonnaci en utilisant la récursivité :")

for i in range(n):
    print(fibonnaci(i))