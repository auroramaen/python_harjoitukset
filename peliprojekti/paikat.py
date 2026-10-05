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

        def kanta(self): #tämän funktion luomiseen kysytty apua, en osannut
             lajit = list(self.kalakanta.keys())
             painot = list(self.kalakanta.values())

             arvottu_kanta = random.choices(lajit, weights=painot, k=1)[0]
             return Kala(laji=arvottu_kanta)

kp1 = Kalapaikka(
     'Pieni järvi',
     {kalalajit[0]: 30, #kuha, todennäköisyys 30%
      kalalajit[2]: 10, #saapas, todennäköisyys 10%
      kalalajit[3]: 30, #ahven, todennäköisyys 30%
      kalalajit[4]: 30} #särki, todennäköisyys 30%
)
kp2 = Kalapaikka(
     'Iso järvi',
     {kalalajit[0]: 20, #kuha, todennäköisyys 20%
      kalalajit[1]: 20, #taimen, todennäköisyys 20%
      kalalajit[2]: 20, #saapas, todennäköisyys 20%
      kalalajit[3]: 20, #ahven, todennäköisyys 20%
      kalalajit[5]: 20, #hauki, todennäköisyys 20%
      }
)
kp3 = Kalapaikka(
     'Joki',
     {kalalajit[1]: 40, #taimen, todennäköisyys 40%
      kalalajit[2]: 40, #saapas, todennäköisyys 40%
      kalalajit[3]: 10, #ahven, todennäköisyys 10%
      kalalajit[5]: 10} #hauki, todennäköisyys 10%
)
kp4 = Kalapaikka(
     'Meri',
     {kalalajit[0]: 20, #kuha, 20%
      kalalajit[1]: 20, #taimen, 20%
      kalalajit[2]: 20, #saapas, 20%
      kalalajit[3]: 20, #ahven, 20%
      kalalajit[6]: 20} #mamelukkikala, 20%
)
# kp1 = Kalapaikka(
#      'Pieni järvi', kalalajit[2:6])
# kp2 = Kalapaikka('Iso järvi', kalalajit[0:6])
# kp3 = Kalapaikka('Joki', Kala.create())
# kp4 = Kalapaikka('Koski', Kala.create())
# kp5 = Kalapaikka('Meri', Kala.create())

paikat = [kp1, kp2, kp3, kp4]