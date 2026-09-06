luku = 20

#varmistetaan että mennään loopin sisään lisäämällä True
#jos on While True, on pakko käyttää break

while True:
    if luku % 2 == 0:
        print(luku)
        # ollaan yhä loopissa, vähennetään luvusta 1
    luku = luku - 1
    # looppi jatkuisi loputtomiin, jos ei tehtäisi break ehtoa
    if luku < 0:
        break