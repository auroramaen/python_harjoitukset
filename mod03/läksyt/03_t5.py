print('Muunnetaan kappaleen massa nykymittoihin keskiaikaisten mittojen mukaan leiviskä, naula ja luoti. 1 leiviskä on 20 naulaa, 1 naula on 32 luotia ja 1 luoti 13,3 grammaa.')
leiviskä = float(input('Anna leiviskät: '))
naula = float(input('Anna naulat: '))
luoti = float(input('Anna luodit: '))

# Muunnetaan kaikki ensin grammoiksi
g3 = luoti * 13.3
g2 = naula * 32 * 13.3
g1 = leiviskä * 20 * 32 * 13.3

# Lasketaan yhteen koko grammamäärä
massa = g1 + g2 + g3

# Lasketaan kilogrammat ja ylitse jäävät grammat. // on kokonaislukujako, % on jakojäännös
kilogrammat = massa // 1000
grammat = massa % 1000

print (f'Kappaleen massa on nykymittojen mukaan: {kilogrammat:.0f} kg ja {grammat:.2f} g')