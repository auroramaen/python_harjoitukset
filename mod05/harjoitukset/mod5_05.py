def osa5():
    #Kysy luku, positiivinen, kokonaisluku. Lähtölaskenta luvusta nollaan ja sitten Kaboom
    #bonusta jos saa ajastuksen, sekunti per numero
    luku5 = int(input("Anna luku:\n"))
    while luku5 > 0:
        print(luku5)
        luku5 -= 1
    print("Kaboom!")