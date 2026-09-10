#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def f(maksimi):
    luku = random.randint(1,maksimi)
    return(luku)

maksimi = int(input('Määritä nopan maksimisilmäluku: '))

while True:
      noppa = (f(maksimi))
      print(noppa)
      if noppa == maksimi:
           break