import random
import json
from paikat import paikat
from pelaaja import Pelaaja

# Valikko ja komennot
k = 'KALASTA'
l = 'LIIKU'
i = 'INVENTAARIO'
s = 'TALLENNA'
e = 'LOPETA'

# Uuden pelin aloitus
uusipeli = int(input('1 = Uusi peli, 2 = Jatka peliä: '))
if uusipeli == 2:
    username = input('Kirjoita nimesi: ')
#    data_luettu = ''
    with open(f"save_{username}.json", "r", encoding="utf-8") as tiedosto:
        data_luettu = json.load(tiedosto)
    pelaaja = Pelaaja(nimi=data_luettu['nimi'], ikä=data_luettu['ikä'], sijainti='Pieni järvi', inventaario=data_luettu['inventaario'])
    print(data_luettu)
else:

# Aloituskysymykset
    nimi = input('Syötä nimesi: ')
    ikä = int(input('Syötä ikäsi: '))
    aloituspaikka = random.choice(paikat)

# Jos pelaaja on alle 12 vuotias, peli päättyy
    if ikä < 12:
        print('Olet alaikäinen. Peli päättyy.')
        quit()

# Jos pelaajan ikä on 12 tai yli, pelin intro tulostetaan      
    with open("intro.txt", "r", encoding="utf-8") as tiedosto:
        intro = tiedosto.read()
        print(intro)

# Uuden pelaajaolion luonti
    pelaaja = Pelaaja(nimi, ikä, aloituspaikka)
    
# Pääohjelma
print(f'\nTervetuloa, {pelaaja.nimi}!')
while True:
    print('VALIKKO')
    print(k, l, i, e, s)
    komento = input('Valitse komento: ').upper()
    if komento == k:
        pelaaja.fish()
        if 'Mamelukkikala' in pelaaja.inventaario:
            print('👑 Voitit pelin! Kalastit legendaarisen Mamelukkikalan')
        ahvenet = pelaaja.inventaario.count('ahven')
        taimenet = pelaaja.inventaario.count('taimen')
        if ahvenet >= 4 or taimenet >= 3:
            print('Voitit pelin! Sait tarvittavan määrän saalista.')
            break
    elif komento == l:
        pelaaja.move(random.choice(paikat))
    elif komento == i:
        pelaaja.inventory()
    elif komento == s:
        pelaaja.save()
    elif komento == e:
        print('Peli päättyi.')
        break
        


    



