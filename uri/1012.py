numeros = input().split()

pi = 3.14159
A = float(numeros[0])
B = float(numeros[1])
C = float(numeros[2])

TRIANGULO = A * C / 2
CIRCULO = pi * (C * C)
TRAPEZIO = (A + B) * C / 2
QUADRADO = B * B
RETANGULO = A * B

print('TRIANGULO: %.3f' % TRIANGULO)
print('CIRCULO: %.3f' % CIRCULO)
print('TRAPEZIO: %.3f' % TRAPEZIO)
print('QUADRADO: %.3f' % QUADRADO)
print('RETANGULO: %.3f' % RETANGULO)
