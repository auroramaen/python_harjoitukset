class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        #uusi hissi aloittaa alimmasta kerroksesta
        self.kerros = self.alin

    def ylös(self):
        self.kerros += 1

    def alas(self):
        self.kerros -= 1

    def siirry(self, kohde):
        while self.kerros < kohde:
            self.ylös()
        while self.kerros > kohde:
            self.alas()

h1 = Hissi(0, 6)
h1.siirry(6)
print(f'Hissin kerros on {h1.kerros}')