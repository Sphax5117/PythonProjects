# Créé par t.hausmann, le 10/10/2023 en Python 3.7
from PIL import Image
def echange2pix(img, pixa,pixb):
    RVBa = img.getpixel(pixa)
    RVBb = img.getpixel(pixb)
    img.putpixel(pixa, RVBb)
    img.putpixel(pixb, RVBa)

def permut_circul(img, i0, j0, i1, j1, n):
    for i in range(n): ## ET PAS N//2 ! On échange les quadrants sur toute la
        for j in range(n): ##longueur
            echange2pix(img, (i0 +i, j0 +j), (i1+i, j1+j))


def rotat_quadrants(img,i,j,taille):
    if taille < 2 : return
    n = taille//2
    rotat_quadrants(img,i,j,n)
    rotat_quadrants(img,i+n,j,n) ## en haut a droite
    rotat_quadrants(img,i,j+n,n) ## en bas a gauche
    rotat_quadrants(img,i+n,j+n,n) ## en bas à droite
    permut_circul(img,i,j,i+n,j,n)
    permut_circul(img,i+n,j,i,j+n,n)
    permut_circul(img,i,j,i,j+n,n)

def rotat_img(img):
    assert img.size[0] == img.size[1],"Dimensions non conformes"
    rotat_quadrants(img, 0,0, img.size[0])


img = Image.open("route_512.png")
img.show()
rotat_img(img)
img.show()