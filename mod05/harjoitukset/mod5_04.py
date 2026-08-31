def osa4():
    #printtaa kaikki luvut 1-20 parittomat:
    luku = 1
    while luku <= 20:
        print(luku)
        luku += 2
    #parilliset:
    luku2 = 1
    while luku2 <= 20:
        if luku2 % 2 == 0:
            print(luku2)
            luku2 += 1