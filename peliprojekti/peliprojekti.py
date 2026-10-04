import random
from kalat import Kala
from paikat import Kalapaikka
from pelaaja import Pelaaja

# Valikko ja komennot
k = 'KALASTA'
l = 'LIIKU'
i = 'INVENTAARIO'
e = 'LOPETA'

kp1 = Kalapaikka('Pieni järvi', Kala.create())
kp2 = Kalapaikka('Iso järvi', Kala.create())
kp3 = Kalapaikka('Joki', Kala.create())
kp4 = Kalapaikka('Koski', Kala.create())
paikat = [kp1, kp2, kp3, kp4]

# Aloituskysymykset
nimi = input('Syötä nimesi: ')
ikä = int(input('Syötä ikäsi: '))
aloituspaikka = random.choice(paikat)

with open("intro.txt", "r", encoding="utf-8") as tiedosto:
    intro = tiedosto.read()
    print(intro)

# Pääohjelma
if ikä < 12:
    print('Olet alaikäinen. Peli päättyy.')
else:
# Uuden pelaajan luonti
    pelaaja = Pelaaja(nimi, ikä, aloituspaikka)
    print(f'\nTervetuloa, {nimi}!')
    while True:
        print('VALIKKO')
        print(k, l, i, e)
        komento = input('Valitse komento: ').upper()
        if komento == k:
            pelaaja.fish()
            ahvenet = pelaaja.inventaario.count('ahven')
            taimenet = pelaaja.inventaario.count('taimen')
            if ahvenet >= 4 or taimenet >= 3:
                print('Voitit pelin! Sait tarvittavan määrän saalista.')
                break
        elif komento == l:
            pelaaja.move(random.choice(paikat))
        elif komento == i:
            pelaaja.inventory()
        elif komento == e:
            print('Peli päättyi.')
            break
            


     



