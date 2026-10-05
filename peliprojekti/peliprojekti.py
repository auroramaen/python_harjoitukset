import json
from pelaaja import Pelaaja

# Valikko ja komennot
k = '1 = KALASTA'
l = '2 = LIIKU'
i = '3 = INVENTAARIO'
s = '4 = TALLENNA'
e = '5 = LOPETA'

# Uuden pelin aloitus
uusipeli = int(input('1 = Uusi peli, 2 = Jatka peliä: '))
if uusipeli == 2:
    username = input('Kirjoita nimesi: ')
#    data_luettu = ''
    with open(f"save_{username}.json", "r", encoding="utf-8") as tiedosto:
        data_luettu = json.load(tiedosto)
    pelaaja = Pelaaja(nimi=data_luettu['nimi'], ikä=data_luettu['ikä'], inventaario=data_luettu['inventaario'])
    print(data_luettu)
else:
# Aloituskysymykset
    nimi = input('Syötä nimesi: ')
    ikä = int(input('Syötä ikäsi: '))
# Jos pelaaja on alle 12 vuotias, peli päättyy
    if ikä < 12:
        print('Olet alaikäinen. Peli päättyy.')
        quit()
# Jos pelaajan ikä on 12 tai yli, pelin intro tulostetaan      
    with open("intro.txt", "r", encoding="utf-8") as tiedosto:
        intro = tiedosto.read()
        print(intro)
# Uuden pelaajaolion luonti
    pelaaja = Pelaaja(nimi, ikä)
# Pääohjelma
print(f'\nTervetuloa, {pelaaja.nimi}!')
print(f'Aloituspaikka on {pelaaja.sijainti}')
while True:
    print('VALIKKO')
    print(k, l, i, s, e)
    komento = input('Valitse komento: ')
    if komento == '1':
        pelaaja.fish()
        if 'Mamelukkikala' in pelaaja.inventaario:
            print('👑 Voitit pelin! Sait saaliiksi legendaarisen Mamelukkikalan!')
            break
        ahvenet = pelaaja.inventaario.count('ahven')
        taimenet = pelaaja.inventaario.count('taimen')
        if ahvenet >= 4 or taimenet >= 3:
            print('👑 Voitit pelin! Sait tarvittavan määrän saalista.')
            break
    elif komento == '2':
        pelaaja.move()
    elif komento == '3':
        pelaaja.inventory()
    elif komento == '4':
        pelaaja.save()
    elif komento == '5':
        print('Peli päättyi.')
        break
