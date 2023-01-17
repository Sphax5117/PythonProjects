### PSEUDO CODE

S = ((12,4), (1,2), (4,10), (1,1), (2,2))

def SaD(S, M):
    X = []
    value = 0
    poids = M
    while M > 0:
        for elem in S:
            print(elem[0])
            if elem[0] < poids:
                poids = poids - elem[0]
                value += elem[1]
                X.append(S.index(elem))
    print(X)
    return X


SaD(S, 15)