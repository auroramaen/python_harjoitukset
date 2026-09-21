#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input('Anna jokin kokonaisluku: '))
tarkistus = True

for item in range(2, luku):
    if luku % item == 0:
        tarkistus = False
        break

if tarkistus:
    print(f'{luku} on alkuluku.')
else:
    print(f'{luku} ei ole alkuluku.')