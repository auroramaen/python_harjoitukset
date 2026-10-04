import random

kalalajit = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki']

class Kala:
        def __init__(self):
            self.laji = random.choice(kalalajit)
            self.paino = random.randint(100, 3000)
            print(f'{self.laji}, {self.paino}g')
            
        def create():
            return random.choice(kalalajit)