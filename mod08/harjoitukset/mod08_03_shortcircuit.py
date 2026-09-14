a = 5
b = 0
c = 3
d = 4

# a/b tuottaa virheen koska 5 ei voi jakaa 0

# and: Python lopettaa ohjelman ensimmäiseen False/True (c>d)
if (c > d and a / b):
    print('Moi')

# or: Python tuottaa virheen koska molemmat käydään läpi 
if (c > d or a / b):
    print('Moi')