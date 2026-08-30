luku = int(input('Anna luku:\n'))

if luku < 100:
    print(f'Antamasi luku oli {luku} ja lukusi on pienempi kuin 100')
elif luku == 100:
    print(f'Antamasi luku oli {luku} ja lukusi on tasan 100')
elif luku > 100:
    print(f'Antamasi luku oli {luku} ja lukusi on suurempi kuin 100')