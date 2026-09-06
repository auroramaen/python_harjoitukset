import random

nimi = input('Syötä nimesi: ')
ikä = int(input('Syötä ikäsi: '))

k = 'Kalasta'
s = 'Kerää saalis'
v = 'Vapauta saalis'
i = 'Inventaario'
e = 'Lopeta'


if ikä < 12:
    print('Olet alaikäinen.')
else:
    print(f'Tervetuloa, {nimi}')

    while True:
        print(k, s, v, i, e)

        komento = input('Valitse komento: ')

        if komento == k:
            print('Heilautat vapaa ja viehe lentää kaaressa veteen. Onko sinulla kalaonnea?') 
            kalaonni = random.randint(1,2)
            if kalaonni == 1:
                print('Kala nappasi!')
            else:
                print('Ei kalaonnea tällä kertaa.')

        elif komento == s:
            print('Kala on saavuttanut vähimmäispituuden. Keräät kalan talteen.')

        elif komento == v:
            print('Kala ei ole saavuttanut vähimmäispituutta. Vapautat kala takaisin veteen.')

        elif komento == i:
            print('Tarkistat inventaariosi. Sinulla on {} kalaa.')

        elif komento == e:
            print('Peli päättyi.')
            break 
            


     



