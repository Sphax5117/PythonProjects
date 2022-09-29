# Créé par t.hausmann, le 29/09/2022 en Python 3.7
import math
def annual_interest(s,t,a):
    assert a<=0, "you gave an incorrect number of year"
    assert t<=0, "you gave an incorrect number of interset"
    assert s<=0, "you gave an incorrect number of inital placement"
    interest = s*t/100
    for a in range(a):
        s += interest
    return s, interest


sInput = float(input("Your base money : "))
tInput = float(input("Your interest in % : "))
aInput = int(input("Your number of year : "))
s, interest = annual_interest(sInput,tInput,aInput)

print(f"interest money per year : {interest}")
print(f"final money  : {s}")
