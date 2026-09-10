#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
#ja palauttaa paluuarvonaan vastaavan litramäärän. 
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
#Muunnos on tehtävä aliohjelmaa hyödyntäen. 
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.


# aliohjelma muuttaa käyttäjän syöttämän määrän litroiksi
def f(x):
    return(3.785 * x)

# pääohjelma
while True:
      gallona = int(input('Syötä gallonien määrä: '))
      if f(gallona) < 0:
        break
      print(f'{gallona} gallonaa on {f(gallona):.2f} litraa.')



