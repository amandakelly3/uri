v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

pares = 0
impares = 0
positivos = 0
negativos = 0

if v1 % 2 == 0:
    pares += 1
else:
    impares += 1
if v1 > 0:
    positivos += 1
if v1 < 0:
    negativos += 1


if v2 % 2 == 0:
    pares += 1
else:
    impares += 1
if v2 > 0:
    positivos += 1
if v2 < 0:
    negativos += 1

if v3 % 2 == 0:
    pares += 1
else:
    impares += 1
if v3 > 0:
    positivos += 1
if v3 < 0:
    negativos += 1

if v4 % 2 == 0:
    pares += 1
else:
    impares += 1
if v4 > 0:
    positivos += 1
if v4 < 0:
    negativos += 1

if v5 % 2 == 0:
    pares += 1
else:
    impares += 1
if v5 > 0:
    positivos += 1
if v5 < 0:
    negativos += 1

print('%i valor(es) par(es)' % pares)
print('%i valor(es) impar(es)' % impares)
print('%i valor(es) positivo(s)' % positivos)
print('%i valor(es) negativo(s)' % negativos)