import math
n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

raiz = (b**2)-(4 * a * c)
if (raiz <0 or a==0):
    print('Impossivel calcular')
else:
    raiz = math.sqrt(raiz)
    r1 = (-b + raiz) /(2*a)
    r2 = (-b - raiz) /(2*a)
    print('R1 = %.5f' %r1)
    print('R2 = %.5f' %r2)
