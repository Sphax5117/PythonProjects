import numpy as np
##########################Exercice 3#############################
#1) 

from tkinter import N


def minimum(a):
    min = 20
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min

assert minimum([-3,5,-9,-9,4]) == -9, "/!\ minimum"

#2)

def position_minimum(a):
    min = 0
    min_pos = 0
    for i in range(len(a)):
        if a[i] < min and a[i] != min:
            min = a[i]
            min_pos = i
    return min_pos

assert position_minimum([-3,5,-9,-9,4]) == 2, "/!\ position_minimum()"

#3) 

def position_minimum_multiple(a):
    min_values = minimum(a)
    min_index = []
    # for i in range(len(a)):
    #     if a[i] <= min:
    #         min = a[i]
    #         min_pos.append(i)
    #     elif a[i-1] < a[i]:
    #         print(min_pos[i-1])
    #         print(i-1)
    #         min_pos.pop(i-1)
    for i in range(0, len(a)):
        if min_values == a[i]:
            min_index.append(i)

    return min_index
assert position_minimum_multiple([-3,5,-9,-9,4,4]) == [2, 3], "/!\ position_minimum_multiple()"

########################################Exercice 4 #########################
#1)

def maximum(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

assert maximum([-3,5,-9,-9,4]) == 5, "/!\ maximum"

#2) 

def position_maximum(a):
    max = 0
    max_pos = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            max_pos = i
    return max_pos

assert position_maximum([-3,5,-9,-9,4]) == 1, "/!\ position_maximum()"

#3)

def position_maximum_multiples(a):
    max_values = maximum(a)
    max_index = []
    for i in range(0, len(a)):
        if max_values == a[i]:
            max_index.append(i)

    return max_index

assert position_maximum_multiples([-3,5,-9,-9,4,5]) == [1, 5], "/!\ position_maximum_multiple()"

###################################Exercice 5############################

def moyenne(a):
    moyenne = sum(a)/len(a)

    return moyenne

assert moyenne([3,5,-9,2,4]) == 1, "/!\ moyenne()"

##################################Exercice 6############################

def moy_pond(valeurs, coefficients):
    productSum = 0
    efTotal = 0
    for i in range(len(valeurs)):
        productSum += valeurs[i] * coefficients[i]
    for i in range(len(coefficients)):
        efTotal += coefficients[i]
    moy_ponde = productSum/efTotal

    return moy_ponde

assert moy_pond([10,16,5], [1,0.5,2]) == 8, "/!\ moy_pond()"

###############################Exercice 7###############################

def moy_geom(nombres):
    xTimesx = np.prod(np.array(nombres))
    n = len(nombres)
    moy = xTimesx ** (1/n)

    return round(moy)

assert moy_geom([2, 4, 8]) == 4, "/!\ moy_geom"
    
