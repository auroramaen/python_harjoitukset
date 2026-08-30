import math
# Kysytään kanta ja korkeus
kanta = float(input('Kerro suorakulmion kannan pituus: '))
korkeus = float(input('Kerro suorakulmion korkeus: '))

# Lasketaan suorakulmion piiri ja pinta-ala. 
# piiri = neljän sivun yhteispituus [2 * (kanta + korkeus)], pinta-ala = kanta * korkeus
print (f'Suorakulmion piiri on{2 * (kanta + korkeus): .2f} ja pinta-ala{kanta * korkeus: .2f}')