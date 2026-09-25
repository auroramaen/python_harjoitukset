class Animal:
    def __init__(self, weight):
        self.weight = weight
    def speak(self):
        print('Minä olen eläin.')

class Dog(Animal):
    def __init__(self, weight, color):
        self.color = color
        #extend ominaisuus luokasta Animal
        super().__init__(weight)
    def speak(self):
        #extend metodi luokasta Animal
        super().speak()
        print('Itse asiassa olen koira.')

d1 = Dog(13, 'White')
d1.speak()
