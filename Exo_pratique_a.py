def chercher(T,n,i,j):
    if i < 0 or j > len(T) -1 :
        return "Erreur"
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] > n :
        print(m)
        print(T[m])
        return chercher(T,n, i, m-1)
    elif T[m] == n:
        return m
    else :
        return chercher(T,n, m+1, j)


assert chercher([1,5,6,6,9,12],7,0,10) == "Erreur", "/!\ defaut chercher"
assert chercher([1,5,6,6,9,12],7,0,5) == None, "/!\ defaut chercher"
assert chercher([1,5,6,6,9,12],9,0,5) == 4, "/!\ defaut chercher"
assert chercher([1,5,6,6,9,12],6,0,5) == 2, "/!\ defaut chercher"