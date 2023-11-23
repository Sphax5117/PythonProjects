### Créé par t.hausmann, le 16/11/2023 en Python 3.7
##class Temps:
##
##    def __init__(self):
##        h = 0
##        m = 0
##        s = 0
##        h2 = 0
##        m2 = 0
##        s2 = 0
##
##
##    def additionner(self, t1, t2): ## t1 = [h,m,s]
##        h = t1[0]
##        m = t1[1]
##        s = t1[2]
##        h2 = t2[0]
##        m2 = t2[1]
##        s2 = t2[2]
##        h3 = 0
##        m3 = 0
##        s3 = 0
##        if s + s2 < 60:
##            s3 = s + s2
##            if m + m2 < 60:
##                m3 += m + m2
##            elif m + m2 > 60:
##                h3 += 1
##                m3 = m + m2 - 60
##        elif s + s2 > 60:
##            m3 += 1
##            s3 = s + s2 - 60
##            if m + m2 < 60:
##                m3 += m + m2
##            elif m + m2 > 60:
##                h3 += 1
##                m3 = m + m2 - 60
##
##
##
##        h3 = h + h2
##
##        return 't1 + t2 = {}h, {}min et {} secondes'.format(str(h3), str(m3), str(s3))



class Temps:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self): ##Affiche les attributs des objets instanciés par Temps
        return "{}h {}min et {}sec".format(self.h, self.m, self.s)

    def somme(self,t2):
        hF = self.h + getattr(t2, "h")
        mF = self.m + getattr(t2, "m")
        sF = self.s + getattr(t2, "s")
        return "La somme est de {}h, {}m et {}s".format(hF,mF, sF)

    def dif(self, t2):
        hF = self.h - getattr(t2, "h")
        mF = self.m - getattr(t2, "m")
        sF = self.s - getattr(t2, "s")
        return "La différence est de {}h, {}m et {}s".format(hF,mF, sF)




