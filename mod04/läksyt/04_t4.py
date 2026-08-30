vuosiluku = int(input('Kerro vuosiluku: \n'))

# Jos vuosi on jaollinen 400 -> karkausvuosi
if vuosiluku % 400 == 0:
    print(f'Vuosi {vuosiluku} on karkausvuosi.')
# 100 jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös 400
elif vuosiluku % 100 == 0:
    print(f'Vuosi {vuosiluku} ei ole karkausvuosi.')
# Vuosi on karkausvuosi jos se on jaollinen 4:llä
elif vuosiluku % 4 == 0:
    print(f'Vuosi {vuosiluku} on karkausvuosi.')
else:
    print(f'Vuosi {vuosiluku} ei ole karkausvuosi.')