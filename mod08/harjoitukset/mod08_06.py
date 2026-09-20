import math

num = math.pi
num2 ='koira'
num3 = 8
print(f'{num: 10.2f}')

def f(x, y):
    z = 2 * x
    return z

print (f('koira', 'kissa'))
print(type(f))

for item in range(1,10):
    print(item)

eka = 1
while eka <= 3:
    toka = 1
    while toka <= 3:
        print(f'{eka} kertaa {toka} on {eka*toka}')
        toka = toka + 1
    eka = eka + 1