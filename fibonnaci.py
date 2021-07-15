import pyfiglet

print(pyfiglet.figlet_format("La suite de fibonacci"))



def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


n = int(input("Entrez le nombre de termes:")) #demande le nombre de fois que l'on répête

print("Suite de Fibonacci en utilisant la recursion :")

for i in range(n): #pour le nombre de fois qu'il y a de n ( exemple 5)
    print(fibonacci(i)) #on fait fibonacci avec i comme paramètre (0 puis 1 puis 2 puis 3 puis 4)