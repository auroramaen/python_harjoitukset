#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa listassa olevien lukujen summan. 
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

#funktio
def f(x):
    return(sum(x))

#pääohjelma
lista = [1, 5, 7, 10]
print(f(lista))