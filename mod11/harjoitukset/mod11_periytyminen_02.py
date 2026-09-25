class Muoto:
    def __init__(self, color):
        self.color = color

    def mitta(self):
        print('Nyt lasken piirin.')

class Suorakulmio(Muoto):
    def __init__(self, color, length, width):
        self.length = length
        self.width = width
        super().__init__(color)

    def mitta(self):
        super().mitta()
        print(f'Piiri on {2*self.length + 2*self.width}cm')

m1 = Suorakulmio('Red', 20, 30)
m2 = Suorakulmio('Blue', 8, 6)
m1.mitta()
m2.mitta()
