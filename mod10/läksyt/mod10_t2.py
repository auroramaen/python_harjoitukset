# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. 
# Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        #uusi hissi aloittaa alimmasta kerroksesta
        self.kerros = self.alinkerros

    def kerros_ylös(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissitlkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissitlkm = hissitlkm

        self.hissit = []

        for item in range(hissitlkm):
            uusi_hissi = Hissi(alinkerros, ylinkerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, hissinumero, kohdekerros):
        hissin_indeksi = hissinumero
        self.hissit[hissin_indeksi].siirry_kerrokseen(kohdekerros)
        print(f'Hissi numero {hissin_indeksi} on kerroksessa {kohdekerros}')

talo1 = Talo(1, 12, 6)
talo1.aja_hissia(5, 11)

