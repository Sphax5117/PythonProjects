# Créé par t.hausmann, le 18/12/2023 en Python 3.7
def recherche_motif(texte, motif):
 n = len(texte)
 m = len(motif)
 occur = []
 i = 0
 while i != n - m:
    j = 0
    k = i
    while j < m and k < n and texte[k] == motif[j]:
        k += 1
        j += 1
    if j == m:
        occur.append(i)
        i += m
    else:
        i += 1
 return occur


def horspool_dico(motif):
    j = 1
    dico = {}
    for i in range(0, len(motif)):
        dico[motif[i]] = len(motif) - j
        j += 1
    dico.pop(motif[-1])
    print(dico)
    return dico

def horspool


assert horspool_dico("bug") == {'b': 2, 'u': 1}, "/!\ defaut horspool_decal()"
assert horspool_dico("FIFO") == {'F': 1, 'I': 2}, "/!\ defaut horspool_decal()"
assert horspool_dico("natation") == {'a': 4, 'i': 2, 'o': 1, 't': 3}, "/!\ defaut horspool_decal()"
