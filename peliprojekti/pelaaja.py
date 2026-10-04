import random
import json
from kalat import Kala

class Pelaaja:
    def __init__(self, nimi, ikä, sijainti = 'Pieni järvi', inventaario = list()):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.inventaario = list()

    def move(self, sijainti):
        self.sijainti = sijainti
        print(f'Vaihdat kalastuspaikkaa.\nUusi paikka on {self.sijainti}')
        tarkastus = random.randint(1,3)
        if tarkastus == 1:
            print('Törmäät kalastuslupatarkastajaan.')
            if len(self.inventaario) <= 2:
                print('Tarkastaja tarkistaa inventaariosi mutta vapauttaa sinut.')
            elif len(self.inventaario) > 2:
                print('Tarkastaja tarkistaa inventaariosi ja huomaa ettet ole maksanut kalastonhoitomaksua.\nTarkastaja takavarikoi inventaariosi.')
                self.inventaario.clear()
        return

    def fish(self):
        print('Heilautat vapaa ja viehe lentää kaaressa veteen. Onko sinulla kalaonnea?')
        kalaonni = random.randint(1, 5)

        if kalaonni in (1, 2, 3):
            kala = Kala()
            kalasaalis = kala.laji
            print(f'Sinulla on kalaonnea, saaliisi on {kala.paino}g painava {kalasaalis} 🐟!')
            paatos = input('Haluatko kerätä vai vapauttaa kalan? K = KERÄÄ/V = VAPAUTA: ').upper()
            if paatos == 'K':
                print('Kala lisättiin inventaarioosi.')
                self.inventaario.append(kalasaalis)
            elif paatos == 'V':
                print('Vapautat kalan takaisin veteen.')
        else:
            print('Ei kalaonnea tällä kertaa. 😞')
        return

    def inventory(self):
        print(f'Inventaariosi on {self.inventaario}')
        return

    def save(self):
        tallennus_data = {
            "nimi": self.nimi,
            "ikä": self.ikä,
            "inventaario": self.inventaario
            }
        with open(f'save_{self.nimi}.json', "w") as tiedosto:
            json.dump(tallennus_data, tiedosto)

