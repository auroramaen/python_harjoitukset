# Arvotaan numerolukon koodit kahdella eri tavalla
import random
koodi1 = (random.randint(0, 9))
koodi2 = (random.randint(0, 9))
koodi3 = (random.randint(0, 9))
print(f'Kolmenumeroinen koodi: {koodi1}{koodi2}{koodi3}')

# # range() tarkoittaa kuinka monta kertaa asia tehdään
# # for _ in (for (arvo) in)
# # str() muutetaan arvot tekstiksi
# # ''.join() yhdistää merkit
koodi4 = ''.join(str(random.randint(1, 6)) for item in range(4))
print(f'Nelinumeroinen koodi: {koodi4}')