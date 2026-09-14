tup = (3, 5, 8, 10, (24, 25), 'moi', 200)

#tuplen pituus
print(len(tup))

#tulosta tup 10 id
id = tup.index(10)
print(id)

#Onko tup:issa numero 10
print(10 in tup)
print(210 in tup)

#Printtaa kaikki alkiot yksi kerrallaan
for item in tup:
    print(item)

#Tee kopio tup2 vastakkaisessa järjestyksessä
print(tup[::-1])