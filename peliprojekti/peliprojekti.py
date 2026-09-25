import random
# Valikko ja komennot
k = 'Kalasta'
l = 'Liiku'
i = 'Inventaario'
e = 'Lopeta'

# Listat
kalat = ['kuha', 'taimen', 'saapas', 'ahven', 'särki', 'hauki']
inventaario = []

#Funktiot
def fish():
    print('Heilautat vapaa ja viehe lentää kaaressa veteen. Onko sinulla kalaonnea?')
    kalaonni = random.randint(1, 4)
    if kalaonni in (1, 2, 3):
        kalasaalis = random.choice(kalat)
        print(f'Sinulla on kalaonnea, saaliisi on {kalasaalis} 🐟!')
        paatos = input('Haluatko kerätä vai vapauttaa kalan? K = KERÄÄ/V = VAPAUTA: ')
        if paatos == 'K':
            print('Kala lisättiin inventaarioosi.')
            inventaario.append(kalasaalis)
        elif paatos == 'V':
            print('Vapautat kalan takaisin veteen.')
        return
    else:
        print('Ei kalaonnea tällä kertaa. 😞')
        return

def move():
    tarkastus = random.randint(1,3)
    if tarkastus == 1:
        print('Törmäät lupatarkastajaan.')
        if len(inventaario) <= 2:
            print('Tarkastaja tarkistaa inventaariosi mutta vapauttaa sinut ilman lupatarkastusta.')
        elif len(inventaario) > 2:
            print('Tarkastaja tarkistaa inventaariosi ja huomaa ettet ole maksanut vaadittua kalastonhoitomaksua.\nTarkastaja takavarikoi inventaariosi.')
            inventaario.clear()
    else:
        print('Vaihdat kalastuspaikkaa.\nOnneksi tarkastajaa ei näy, sillä et muista, oliko sinulla kalastusluvat kunnossa.')
        return

def inventory():
    print(f'Inventaariosi on {inventaario}')
    return

# Pääohjelma
nimi = input('Syötä nimesi: ')
ikä = int(input('Syötä ikäsi: '))

if ikä < 12:
    print('Olet alaikäinen. Peli päättyy.')
else:
    print(f'\nTervetuloa, {nimi}!\n')
    print('Olet kalastamassa veneellä keskellä järveä.\nSinun pitää kalastaa illalliseksi joko 4 ahventa tai 3 taimenta.\nOlikohan sinulla kalastusluvat kunnossa?\n')
    while True:
        print('VALIKKO')
        print(k, l, i, e)
        komento = input('Valitse komento: ')
        if komento == k:
            fish()
            ahvenet = inventaario.count('ahven')
            taimenet = inventaario.count('taimen')
            if ahvenet >= 4 or taimenet >= 3:
                print('Voit pelin! Kalastit tarpeeksi kalaa illallista varten!')
                break
        elif komento == l:
            move()
        elif komento == i:
            inventory()
        elif komento == e:
            print('Peli päättyi.')
            break
            


     



