# Nyt ohjelmoidaan autokilpailu. 
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. 
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. 
# Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

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

autolista = []
for i in range(1, 11):
    rekisteritunnus = (f'ABC-{i}')

    huippunopeus = random.randint(100, 200)

    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autolista.append(uusi_auto)

