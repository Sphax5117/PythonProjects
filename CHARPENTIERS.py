# Créé par t.hausmann, le 21/02/2023 en Python 3.7
# Mini projet 1 Spé NSI Algo Glouton en Python 3.7
# Pb d'optimisation de remplissage d'un véhicule

def logistic(mat,V,M) :
    '''
        mat : (dict) du matériel clé (str) valeur(tuple(m3,T))
        V : (int) volume du véhicule
        M : (int) masse transportable
    renvoie une liste de listes (list(list(str)) du nom des matériels pour chaque voyage
    '''
    lst = sorted(mat.items(), key=lambda d:d[1][0], reverse=True)
    final = []
    volume = V
    i = 0
    while len(lst) > 0:
        final.append([])
        for i in range(len(lst)):
            print(i)
            print(final)
            print(lst)
            if lst[i][1][0] < V and lst[i][1][1] < M:
                final[0].append(lst[i])
                lst.pop(i)
                i = i - 1

        print(final)


#POUR DÉBUTER AVEC UN JEU DE DONNÉES RÉDUIT
mtrl = {'armoire':(3,0.07),'aspirateur1':(2.3,0.15),'aspirateur2':(0.66,0.08),'compresseur':(0.5,0.1),
            'degau':(1.4,0.3), 'entraineur':(0.55,0.1)}
logistic(mtrl, 5, 1.2)

##
##[['armoire', 'degau', 'entraineur'],
## ['aspirateur1', 'aspirateur2', 'compresseur']]


materiels = {'etabli_2':(2.4,0.3),'perçeuse':(0.6,0.15),'toupie':(1.15,0.4),'rabo':(0.7,0.15),'degau':(1.4,0.3),
            'scie1':(1.4,0.17),'armoire':(3,0.07),'compresseur':(0.5,0.1),'scie2':(2,0.6),'touret':(0.35,0.5),
            'aspirateur1':(2.3,0.15),'aspirateur2':(0.66,0.08),'tour':(2.5,0.8),'entraineur':(0.55,0.1),
            'ponceuse':(0.78,0.56),'etabli_1':(1.4,0.1),'mortaiseuse':(0.3,0.78),}

## lst(tuple) UNE FOIS TRIÉE par VOLUME /  d'autre critères existent
##[('armoire', (3, 0.07)), ('tour', (2.5, 0.8)), ('etabli_2', (2.4, 0.3)), ('aspirateur1', (2.3, 0.15)),
##    ('scie2', (2, 0.6)), ('degau', (1.4, 0.3)), ('scie1', (1.4, 0.17)), ('etabli_1', (1.4, 0.1)),
##    ('toupie', (1.15, 0.4)), ('ponceuse', (0.78, 0.56)), ('rabo', (0.7, 0.15)), ('aspirateur2', (0.66, 0.08)),
##    ('perçeuse', (0.6, 0.15)), ('entraineur', (0.55, 0.1)), ('compresseur', (0.5, 0.1)), ('touret', (0.35, 0.5)),
##     ('mortaiseuse', (0.3, 0.78))]


## __________________________________________________________________________________________________________________
##                             RESULTATS
## __________________________________________________________________________________________________________________
## TRIÉ PAR VOLUME
##[['armoire', 'scie2'],
## ['tour', 'etabli_2'],
## ['aspirateur1', 'degau', 'toupie'],
## ['scie1', 'etabli_1', 'ponceuse', 'rabo', 'aspirateur2'],
## ['perçeuse', 'entraineur', 'compresseur', 'touret'],
## ['mortaiseuse']]

## TRIÉ PAR MASSE
##[['tour', 'toupie'],
## ['mortaiseuse', 'etabli_2', 'compresseur'],
## ['scie2', 'ponceuse'],
## ['touret', 'degau', 'scie1', 'perçeuse', 'aspirateur2'],
## ['rabo', 'aspirateur1', 'entraineur', 'etabli_1'],
## ['armoire']]

## TRIÉ PAR VOLUME / MASSE
##[['armoire', 'etabli_1', 'entraineur'],
## ['aspirateur1', 'aspirateur2', 'scie1', 'compresseur'],
## ['etabli_2', 'rabo', 'degau'],
## ['perçeuse', 'scie2', 'toupie'],
## ['tour'],
## ['ponceuse', 'touret'],
## ['mortaiseuse']]

## TRIÉ PAR MASSE / VOLUME
##[['mortaiseuse', 'toupie'],
## ['touret', 'ponceuse', 'compresseur'],
## ['tour', 'perçeuse', 'rabo', 'entraineur'],
## ['scie2', 'degau', 'scie1'],
## ['etabli_2', 'aspirateur2', 'etabli_1'],
## ['aspirateur1'],
## ['armoire']]


