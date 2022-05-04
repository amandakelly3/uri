valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

triangulo = a + b + c
trapezio = (a+b)*c/2

if (a+b > c and b+c > a and a+c > b ):
   print('Perimetro = %.1f' %(triangulo))

else:
    print('Area = %.1f' %trapezio)
