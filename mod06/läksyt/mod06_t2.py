#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

kaikkiluvut = []
luku = input('Anna luku: ')

while True:
    if luku == '':
        break
    else:
        kaikkiluvut.append(luku)
        luku = input('Anna luku: ')

kaikkiluvut.sort(reverse=True)
print(kaikkiluvut)

