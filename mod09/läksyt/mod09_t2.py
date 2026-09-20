#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). 
#Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. 
#Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. 
#Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
#Tulosta tämän jälkeen auton nopeus. 
#Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. 
#Kuljettua matkaa ei tarvitse vielä päivittää.
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

auto = Auto("ABC-123", 142)
auto.kiihdytä(30)

auto.kiihdytä(70)

auto.kiihdytä(50)

#print(auto.nopeus)

auto.kiihdytä(-200)

#print(auto.nopeus)

print(f'Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus {auto.huippunopeus}km/h, tämänhetkinen nopeus {auto.nopeus}km/h ja kuljettu matka {auto.matka} km.')