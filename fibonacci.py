# Créé par t.hausmann, le 05/12/2023 en Python 3.7
from time import perf_counter
import matplotlib.pyplot as plt


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)



def fibTDRec(n, Memo):
    if n == 0 or n == 1 :
        Memo[n] = n
    else:
        if Memo[n] == 0 :
            Memo[n] = fibTDRec(n-1, Memo) + fibTDRec(n-2, Memo)
    return Memo[n]

def fibTD(n):
    Memo = [0]*(n+1)
    return fibTDRec(n, Memo)

def fibBU(n):
    Memo = [0] * (n+1)
    Memo[1] = 1
    for i in range(2,n+1,1):
        Memo[i] = Memo[i-1] + Memo[i-2]
    return Memo[n]

temps_fib = []
temps_fibTD = []
temps_fibBU = []
ordre = []
for i in range(1,20):
    ordre.append(i)
    d = perf_counter()
    fib(i)
    temps_fib.append(perf_counter() - d)
    m = perf_counter()
    fibTD(i)
    temps_fibTD.append(perf_counter() - m)
    p = perf_counter()
    fibBU(i)
    temps_fibBU.append(perf_counter() - p)


plt.clf()
plt.plot(ordre, temps_fib, '-',label = "Récursive", color='blue')
plt.plot(ordre, temps_fibTD, '-',label = "Top Down", color='red')
plt.plot(ordre, temps_fibBU, '-',label = "Bottom Up", color='green')
plt.xlabel('valeur n')
plt.ylabel('Temps en ms')
plt.legend()
plt.show()
