import random
from kalat import Kala

class Kalapaikka:
        def __init__(self, sijainti, kalalajit):
            self.sijainti = sijainti
            self.kalalajit = kalalajit

        def __str__(self):
            return self.sijainti

kp1 = Kalapaikka('Pieni järvi', Kala.create())
kp2 = Kalapaikka('Iso järvi', Kala.create())
kp3 = Kalapaikka('Joki', Kala.create())
kp4 = Kalapaikka('Koski', Kala.create())
paikat = [kp1, kp2, kp3, kp4]