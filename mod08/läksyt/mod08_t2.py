#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, 
#kunnes käyttäjä syöttää tyhjän merkkijonon. 
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, 
#syötettiinkö nimi ensimmäistä kertaa. 
#Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
#Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
while True:
    kysymys = (input('Anna nimi: '))

    if kysymys == '':
        break
    if kysymys in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
        nimet.add(kysymys)

for item in nimet:
    print(item)