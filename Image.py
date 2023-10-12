# Créé par t.hausmann, le 10/10/2023 en Python 3.7

from PIL import Image
from time import perf_counter

img = Image.open("route_128.png")
img.show()
print("taille_image :", img.size[0], "x", img.size[1])

def echange2pix(img, pixa,pixb):
    RVBa = img.getpixel(pixa)
    RVBb = img.getpixel(pixb)
    img.putpixel(pixa, RVBb)
    img.putpixel(pixb, RVBa)

def tourne4pix(img, pix0, pix1, pix2, pix3):
    echange2pix(img, pix0, pix1)
    echange2pix(img, pix1, pix2)
    echange2pix(img, pix2, pix3)

def rotat_img(img):
    assert img.size[0] == img.size[1], "The format should be n*n"
    n = img.size[0]
    for i in range(n//2):
        for j in range(n//2):
            ri = (n-1)-i
            rj = (n-1)-j
            ##tourne4pix(img, (i,j), (rj, i), (ri,rj), (j,ri))
            tourne4pix(img, (j,i), (i, rj), (rj,ri), (ri,j))

rotat_img(img)
img.show()

def Complex(images):
    dic = {}
    for i in images:
        img = Image.open(i)
        temps_origine = perf_counter()
        rotat_img(img)
        dic[str(img.size[0]) + "x" + str(img.size[1])] = str(round(perf_counter() -temps_origine, 3))

    return dic

images = ["route_128.png", "route_256.png", "route_512.png", "route_1024.png", "route_2048.png"]
print(Complex(images))

