#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
#Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. 
#Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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
        self.matka = self.nopeus * tunnit

auto = Auto("ABC-123", 142)
auto.kiihdytä(60)
auto.kulje(1.5)
print(f'Auto on kulkenut {int(auto.matka)} km matkan.')
#auto.kiihdytä(30)
#auto.kiihdytä(70)
#auto.kiihdytä(50)
#print(auto.nopeus)
#auto.kiihdytä(-200)
#print(auto.nopeus)

#print(f'Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus {auto.huippunopeus}km/h, tämänhetkinen nopeus {auto.nopeus}km/h ja kuljettu matka {auto.matka} km.')