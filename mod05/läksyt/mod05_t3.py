# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

kaikkiluvut = []
while True:
    luku = (input('Anna luku: '))

    if luku == ' ':
        break
    else:
        kaikkiluvut.append(luku)

kaikkiluvut.sort(key=int)
print(kaikkiluvut[0], kaikkiluvut[-1])
    