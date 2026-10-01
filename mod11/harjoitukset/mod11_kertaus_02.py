#Luokkamuuttuja

class Koira:
    tehty = 0
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä
        Koira.tehty = Koira.tehty + 1

koira1 = Koira('k1', 12)
koira2 = Koira('k2', 10)

print(Koira.tehty)