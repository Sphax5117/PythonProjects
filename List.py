from random import randrange

L1 = [0 for i in range(10)]
L2 = [i for i in range(0, 52, 2)]
L3 = [i for i in range(1, 52, 2)]
L4 = [randrange(1, 100) for i in range(20)]
L5 = [i*i for i in range(15)]
L6 = [i for i in range(0, 2)]*10
L7 = [i for i in range(-1, 2, 2)]*50
b = -20
L8 = [i for i in range(b,21)]

print(L8)
