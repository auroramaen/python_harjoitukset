# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
#luku arvotaan ennen silmukkaa, joten luku ei vaihdu
luku = random.randint(1,10) 

while True:
    oikein = int(input('Arvaa oikea luku 1-10: \n'))
    if oikein > luku:
        print('Liian suuri arvaus')
    elif oikein < luku:
        print('Liian pieni arvaus')
    else:
        print('Oikein')
        break

    