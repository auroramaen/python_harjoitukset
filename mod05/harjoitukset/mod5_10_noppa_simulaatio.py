import random

while True:
    noppa1 = random.randint(1,3)
    noppa2 = random.randint(1,3)
    if noppa1 == 3 and noppa2 == 3:
        print(f'Noppa 1 on {noppa1} ja noppa 2 on {noppa2}')
        print('Voitto!')
        break
    else:
        print(f'Noppa 1 on {noppa1} ja noppa 2 on {noppa2}')
    


