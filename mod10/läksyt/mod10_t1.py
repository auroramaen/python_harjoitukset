class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        #uusi hissi aloittaa alimmasta kerroksesta
        self.kerros = self.alinkerros

    def siirry_kerrokseen(self, siirry):
        if siirry > self.kerros:
            for item in range(siirry - self.kerros):
                self.kerros_ylös()
        elif siirry < self.kerros:
            for item in range (self.kerros - siirry):
                self.kerros_alas()

    def kerros_ylös(self, ylös):
        if ylös > 0:
            self.kerros = self.kerros + 1


    def kerros_alas(self, alas):
        if alas < 0:
            self.kerros = self.kerros - 1

h1 = Hissi(0, 6)
h1.kerros_ylös(1)
h1.siirry_kerrokseen(6)
print(f'Hissin kerros on {h1.kerros}')