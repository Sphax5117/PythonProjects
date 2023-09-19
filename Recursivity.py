# Créé par t.hausmann, le 19/09/2023 en Python 3.7

def pgcd(a,b):
        if b == 0:
            return a
        elif b >= 1:
            return pgcd(b, a % b)


pgcd(168589,46295)



def syracuse(u):
    ## Note : we could use a list to show the data, but the exercise
    ## is about recursivity
    while u > 1:
        print(int(u))
        if u % 2 == 0:
            return syracuse(u/2)
        else:
            return syracuse(3*u+1)

    print(int(u))
    return u


def factorielle(n):
    while n > 0:
        if n == 1 or n ==0:
            return 1
        elif n >1:
            return n * factorielle(n-1)

##c = factorielle(10)
##print(c)

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    while n > 1:
        return fibonnaci(n-2)+fibonnaci(n-1)

##
##c = fibonnaci(30)
##print(c)

def puissance(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    while n > 1:
        if n % 2 == 0:
            return puissance(x,n/2)**2
        elif n % 2 != 0:
            return puissance(x, (n-1)/2)**2
##
##c = puissance(2,8)
##print(c)

import matplotlib.pyplot as plt

def f91(n):
    if n>100:
        return n - 10
    while n <= 100:
        return f91(f91(n+11))

n = [i for i in range(0,130,1)]
r = []

for i in n:
    r.append(f91(i))

##plt.clf()
##plt.plot(n,r)
##plt.xlabel('n')
##plt.ylabel('f91(n)')
##plt.title('Fonction f91 de John Mc Carthy')
##plt.show()

from turtle import *

def koch(n,l):
    if n == 0:
        forward(l)
    else:
        koch(n -1 , l/3)
        left(60)
        koch(n-1, l/3)
        right(120)
        koch(n-1, l/3)
        left(60)
        koch(n-1, l/3)

l = 500
n = 4

def star(n,l):
    for i in range(1,4):
        koch(n,l)
        right(120)
##
##
##
##clearscreen()
##speed(0)
##hideturtle()
##penup()
##setposition(-l/2,0)
##pendown()
##pensize(1)
##star(n,l)
##exitonclick()


def a(n):
    if n == 0:
        return 0
    while n >= 1:
        return ((4/9)**n + a(n-1))


n = a(10)
print(n)
def aire(n):
    aire = 3*(3**.5)*(1**2)*(4/3 + n)/16
    return aire

c = aire(10)
print(c)