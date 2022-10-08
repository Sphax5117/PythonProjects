# nH2 = 2
# nO2 = 3.5
# nH2O = 0
# x = 0
# xi = 0.01

# while nH2 > 0 and nO2 >0:
#     x= x+xi
#     nH2 = nH2-2*xi
#     nO2 = nO2-xi
#     nH2O = nH2O + 2*xi

# print("Avancement maximal : \n \t" + str(round(x,1)) + 'mol')

# #Réactif limitant
# if nO2<0:
#     print("Le réactif limitant est O2")
#     print("Il reste " + str(round(nH2,1)) + " mol de H2")

# if nH2<0:
#     print("Le réactif limitant est H2")
#     print("Il reste " + str(round(nO2,1)) + " mol de O2")



############################# Mon programme #############################""
ntrigly = 0.5 #mol de triglycéride
nNAOH = 2 #mol de Soude
nSavon = 0 #mol de savons 
x = 0 # avancement
xi = 0.01 #pas

while ntrigly > 0 and nNAOH >0: #tant que la quantité de Triglycéride ou de Soude est >0
    x= x+xi #on incrémente l'avancement de 0.01
    ntrigly -= xi # on enlève x à l'état initial
    nNAOH = nNAOH - 3 * xi #même chose avec coef. stoechiométrique de 3
    nSavon += xi # on rajoute le pas au savon

print("Avancement maximal : \n \t" + str(round(x,1)) + 'mol') 
#imprime l'avancement maximal pour cette formule


#Réactif limitant
if ntrigly<0:
    print("Le réactif limitant est la triglycéride")
    print("Il reste " + str(round(nNAOH,1)) + " mol de Soude")

if nNAOH<0:
    print("Le réactif limitant est la Soude")
    print("Il reste " + str(round(ntrigly,1)) + " mol de Triglycéride")