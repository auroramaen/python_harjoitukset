#luodaan luokka
class Person:
    #jokaisella classilla on ominaisuudet
    def __init__(self, name):
        self.nimi = name
    #ja metodit
    def walk(self):
        print('Kävelen.')

class Viesti:
    #luokan muuttuja / staattinen muuttuja
    send = 0
    def __init__(self, content):
        self.content = content
        #tarkastetaan montako viestiä on lähetetty
        Viesti.send += 1

v1 = Viesti('Tänään on maanantai.')
v2 = Viesti('Tänään on tiistai.')
v3 = Viesti('Tänään on keskiviikko.')

print(Viesti.send)