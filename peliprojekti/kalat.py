import random

kalalajit = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki', 'Mamelukkikala']
#indeksit 0 = kuha, 1 = taimen, 2 = saapas, 3 = ahven, 4 = särki, 5 = hauki, 6 = Mamelukkikala

class Kala:
        def __init__(self, laji):
            self.laji = laji
            if self.laji == kalalajit[6]:
                 self.paino = 100
            elif self.laji == kalalajit[5]:
                 self.paino = random.uniform(0.5, 6.0)
            elif self.laji == kalalajit[4]:
                 self.paino = random.uniform(0.05, 0.35)
            elif self.laji == kalalajit[3]:
                 self.paino = random.uniform(0.05, 1.2)
            elif self.laji == kalalajit[2]:
                 self.paino = random.uniform(1.0, 2.5)
            else:
                 self.paino = random.uniform(0.6, 4.0)
            
#        def create():
#            return random.choice(kalalajit)