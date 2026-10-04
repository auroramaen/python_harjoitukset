import random
from kalat import kalalajit

class Kalapaikka:
        def __init__(self, sijainti, kalalajit):
            self.sijainti = sijainti
            self.kalalajit = kalalajit

        def __str__(self):
            return self.sijainti