# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = int(input('Kuinka monta tuumaa: '))
senttimetri = 2.54 * tuuma

while tuuma >= 0:
    print(f'{tuuma} tuumaa on {senttimetri} cm')
    break
else:
    print = tuuma