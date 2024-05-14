# Créé par t.hausmann, le 18/12/2023 en Python 3.7

def score_max(i,j,p):
	if i == 0:
		score_max(len(p)-1,j,p) = p[len(p)-1][j]
	else:
		score_max(i,j,p) = p[i][j] + max(score_max(i+1,j,p), score_max(i+1,j+1,p))



def pyr_vide(n):
    pyr = []
    for i in range(1,n+1):
        pyr.append([0]*i)
    return pyr

def prog_dyn(p):
	n = len(p)
	s = pyr_vide(n)
	for j in s[-1]:
		s[n-1][j] = p[j]
	for i in s[0]:
		for j in s[0]:
			s[i][j] = p[j]
	return s[0]
