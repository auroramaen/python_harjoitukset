#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron
#jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
#Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenaika = "kevät", "kesä", "syksy", "talvi"
kuukaudet = ((3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 1, 2))

numero = int(input('Kerro kuukauden numero 1-12: '))
if numero in kuukaudet[0]:
    print(f'Vuodenaika on {vuodenaika[0]}')
elif numero in kuukaudet[1]:
    print(f'Vuodenaika on {vuodenaika[1]}')
elif numero in kuukaudet[2]:
    print(f'Vuodenaika on {vuodenaika[2]}')
elif numero in kuukaudet[3]:
    print(f'Vuodenaika on {vuodenaika[3]}')
