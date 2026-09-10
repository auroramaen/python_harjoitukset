#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, 
#kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
#Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

# Kaava: pi × (Halkaisija metreinä / 2)²
import math

#funktio joka laskee funktioon syötetyn pizzan pinta-alan ja sen jälkeen yksikköhinta = pinta-alan / hinta
def f(x, y):
    sade = (x / 100) / 2
    pinta_ala = math.pi * (sade ** 2)
    yksikkohinta = y / pinta_ala
    return(yksikkohinta)

#pääohjelma, joka kysyy kahden pizzan halkaisijat ja hinnat
halkaisija1 = float(input('Syötä ensimmäisen pizzan cm halkaisija: '))
hinta1 = float(input('Syötä ensimmäisen pizzan hinta euroissa: '))

halkaisija2 = float(input('Syötä toisen pizzan cm halkaisija: '))
hinta2 = float(input('Syötä toisen pizzan hinta euroissa: '))

#syöttää pizzojen halkaisijat ja hinnat funktioon
yksikkohinta1 = f(halkaisija1, hinta1)
yksikkohinta2 = f(halkaisija2, hinta2)

#ilmoittaa kummalla pizzalla on alhasempi yksikköhinta
if yksikkohinta1 < yksikkohinta2:
    print('Ensimmäisessä pizzasta saat enemmän vastinetta rahalle!')
elif yksikkohinta1 > yksikkohinta2:
    print('Toka pizzasta saat enemmän vastinetta rahalle!')
else:
    print('Pizzoilla on sama yksikköhinta')