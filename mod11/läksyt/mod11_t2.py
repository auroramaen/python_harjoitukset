# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
# Kirjoita aliluokille alustajat. 
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, kiihdytys):
        muutos = self.nopeus + kiihdytys
        if muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif muutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = muutos

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) 
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
# Aseta kummallekin autolle haluamasi nopeus, 
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

a1 = Sahkoauto('ABC-15', 180, 52.5)
a2 = Polttomoottoriauto('ACD-123', 165, 32.3)

a1.kiihdytä(100)
a2.kiihdytä(80)

a1.kulje(3)
a2.kulje(3)

print(f'Sähkoauton {a1.rekisteritunnus} mittarilukema on {a1.matka} km')
print(f'Polttomoottoriauton {a2.rekisteritunnus} mittarilukema on {a2.matka} km')

