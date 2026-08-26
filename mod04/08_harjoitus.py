#kysymys2 = (input('Mikä on lämpötila:\n'))
#kysymys = int(kysymys2)

#if kysymys <= 0:
 #   print('Tosi kylmä')
#elif kysymys <= 0 >= 10:
#    print('Vähän kylmä')
#elif kysymys <= 10 >= 15:
#    print('Ihan OK')
#elif kysymys <= 15 >= 20:
#    print('Ihan OK')
#elif kysymys >= 20:
#    print('Mahtavaa!')

luku = int(input('Mikä on lämpötila:\n'))

if luku <= 10:
    print(f'Lukusi oli {luku} ja se on pienempi kuin 20')
elif luku <= 10 >= 20:
    print(f'Lukusi oli {luku} ja se on 10 ja 20 välillä')
else:
    print(f'Lukusi oli {luku} ja se on suurempi kuin 20')