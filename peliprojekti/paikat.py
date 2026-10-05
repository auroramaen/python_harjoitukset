import random
from kalat import Kala, kalalajit
#kalalajit = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki', 'Mamelukkikala']
#indeksit kuha = 0, taimen = 1, saapas = 2, ahven = 3, särki = 4, hauki = 5, mamelukkikala = 6

class Kalapaikka:
        def __init__(self, sijainti, kalakanta):
            self.sijainti = sijainti
            self.kalakanta = kalakanta

        def __str__(self):
            return self.sijainti

        def kanta(self):
             lajit = list(self.kalakanta.keys()) #Kalapaikka olion dictionaryn kalalaji
             painot = list(self.kalakanta.values()) #Kalapaikka olion dictionaryn painoarvo

             arvottu_kanta = random.choices(lajit, painot, k=1)[0]
             return Kala(laji=arvottu_kanta)

kp1 = Kalapaikka(
     'Pieni järvi',
     {kalalajit[0]: 3, #kuha, todennäköisyys 30%
      kalalajit[2]: 1, #saapas, todennäköisyys 10%
      kalalajit[3]: 3, #ahven, todennäköisyys 30%
      kalalajit[4]: 3} #särki, todennäköisyys 30%
)
kp2 = Kalapaikka(
     'Iso järvi',
     {kalalajit[0]: 2, #kuha, todennäköisyys 20%
      kalalajit[1]: 2, #taimen, todennäköisyys 20%
      kalalajit[2]: 2, #saapas, todennäköisyys 20%
      kalalajit[3]: 2, #ahven, todennäköisyys 20%
      kalalajit[5]: 2, #hauki, todennäköisyys 20%
      }
)
kp3 = Kalapaikka(
     'Joki',
     {kalalajit[1]: 4, #taimen, todennäköisyys 40%
      kalalajit[2]: 4, #saapas, todennäköisyys 40%
      kalalajit[3]: 1, #ahven, todennäköisyys 10%
      kalalajit[5]: 1} #hauki, todennäköisyys 10%
)
kp4 = Kalapaikka(
     'Meri',
     {kalalajit[0]: 2, #kuha, 20%
      kalalajit[1]: 2, #taimen, 20%
      kalalajit[2]: 2, #saapas, 20%
      kalalajit[3]: 2, #ahven, 20%
      kalalajit[6]: 1} #mamelukkikala, 10%
)
paikat = [kp1, kp2, kp3, kp4]