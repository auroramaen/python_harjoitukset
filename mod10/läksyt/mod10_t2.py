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
        self.kerros = self.alin

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
        hissit = []

        for item in range(hissitlkm):
            uusi_hissi = Hissi()
            hissit.append(uusi_hissi)

    def __init__(self, hissinumero, kohdekerros):
        
