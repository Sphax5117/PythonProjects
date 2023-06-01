# Créé par t.hausmann, le 30/05/2023 en Python 3.7
class CodeCesar:
    def __init__(self, cle):
        assert cle <= 26, "Clé + grande que 26 !!"
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"

    def decale(self, lettre):
        num1 = self.alphabet.find(lettre)
        num2 = num1+self.cle
        if num2 >= 26:
            num2 = num2 - 26
        if num2 < 0:
            num2 = num2 + 26
        nouvelle_lettre = self.alphabet[num2]
        return nouvelle_lettre

    def chiffrage(self, text):
        finalTxT = ""
        for i in range(len(text)):
            num1 = self.alphabet.find(text[i])
            num2 = num1 + self.cle
            if num2 >= 26:
                num2 = num2 - 26
            elif num2 < 0:
                num2 = num2 + 26
            finalTxT += self.alphabet[num2]
        return finalTxT

    def dechiffrage(self, text):
        finalTxT = ""
        for i in range(len(text)):
            num1 = self.alphabet.find(text[i])
            num2 = num1 - self.cle
            if num2 >= 26:
                num2 = num2 - 26
            elif num2 < 0:
                num2 = num2 + 26
            finalTxT += self.alphabet[num2]
        return finalTxT

def convert():
    cle = int(input("Clé de chiffrement : "))
    code1 = CodeCesar(cle)
    print(code1.chiffrage(input("Texte à chiffrer : ")))
