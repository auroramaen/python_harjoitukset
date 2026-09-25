class Koira:
    def __init__(self, nimi, ikä, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.ikä = ikä
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for item in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

koira = Koira('Musti', 11)
koira.hauku(5)
print(f'{koira.nimi} {koira.ikä} {koira.haukahdus}')