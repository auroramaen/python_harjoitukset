# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).

käyttäjätunnus = 'python'
salasana = 'rules'

yritys = 0

while yritys < 5:
    kysymys1 = input('Anna käyttäjätunnus:\n')
    kysymys2 = input('Anna salasana:\n')
    if kysymys1 == käyttäjätunnus and kysymys2 == salasana:
        print('TERVETULOA')
        break
    yritys = yritys + 1
if yritys == 5:
    print('PÄÄSY EVÄTTY')