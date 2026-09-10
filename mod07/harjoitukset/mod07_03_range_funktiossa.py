#for luku in range(10):
    # range(10) tarkoittaa = including 0, excluding 10, step 1
#    print(luku)

#def nimeni(x, y):
#    for num in range(y):
#        print(f'{x} {num + 1}. kerta')
#    
#nimeni('Pekka', 5)

def f(x):
    x.append(4)
#    x = x + 1
    print(x)

#x = 10
x = [1, 2, 3]
f(x)
print(x)