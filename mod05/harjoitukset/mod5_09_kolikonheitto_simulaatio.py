import random
# generoidaan 10 satunnaista lukua randomilla
muut = 0

# 1:kruunu, 2:klaava
while muut <=10:
    kolikko = random.randint(1,2)
    if kolikko == 1:
        print('Kruunu')
    elif kolikko == 2:
        print('Klaava')
    muut = muut + 1

# if kolikko == 2:
#    print('Kruuna')
# else:
#    print('Klaava')