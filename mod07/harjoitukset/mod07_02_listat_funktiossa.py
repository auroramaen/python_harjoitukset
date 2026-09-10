def f(x):
    lista2 = []
    for luku in x:
        if luku % 2 == 0:
            lista2.append(luku)
    return lista2 

lista1 = [2, 5, 7, 10]
print(f(lista1))