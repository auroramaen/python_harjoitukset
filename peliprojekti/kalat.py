import random

kalalajit = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki', 'Mamelukkikala']

class Kala:
        def __init__(self, laji):
            self.laji = laji
            if self.laji == 'Mamelukkikala':
                 self.paino = 100000
            elif self.laji == 'hauki':
                 self.paino = random.randint(500, 6000)
            elif self.laji == 'särki':
                 self.paino = random.randint(50,350)
            elif self.laji == 'ahven':
                 self.paino = random.randint(50, 1200)
            elif self.laji == 'saapas':
                 self.paino = random.randint(1000, 2500)
            else:
                 self.paino = random.randint(600, 4000)
#            print(f'{self.laji}, {self.paino}g')
            
        def create():
            return random.choice(kalalajit)