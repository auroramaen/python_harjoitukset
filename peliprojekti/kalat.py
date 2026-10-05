import random

kalalajit = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki', 'Mamelukkikala']

class Kala:
        def __init__(self):
            self.laji = random.choice(kalalajit)
            if self.laji == 'Mamelukkikala':
                 self.paino = 100000
            else:
                 self.paino = random.randint(100, 3000)
#            print(f'{self.laji}, {self.paino}g')
            
        def create():
            return random.choice(kalalajit)