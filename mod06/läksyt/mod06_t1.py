#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
#Käytä for-toistorakennetta.

import random

silmäluvut = []
heitot = int(input('Kuinka monta arpakuutiota?: '))

for item in range(heitot):
    silmäluvut.append(random.randint(1,12))
    summa = sum(silmäluvut)
    
print(f'Silmälukujen summa on {summa}')

