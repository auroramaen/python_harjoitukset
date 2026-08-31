oikea1 = 'James'
oikea2 = 'Bond'
sala = input('Anna salasanasi: ')

while sala != oikea1:
    print('Väärä salasana, kokeile uudelleen!')
    sala = input('Anna salasanasi: ')
    if sala == oikea2:
        break

else:
    print('Nyt else kohta')