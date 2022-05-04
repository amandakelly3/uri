v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

positivos = 0
total = 0

if v1 > 0:
    positivos += 1
    total += v1
if v2 > 0:
    positivos += 1
    total += v2
if v3 > 0:
    positivos += 1
    total += v3
if v4 > 0:
    positivos += 1
    total += v4
if v5 > 0:
    positivos += 1
    total += v5
if v6 > 0:
    positivos += 1
    total += v6

media = total/positivos
print('%.f valores positivos' %positivos)
print('%.1f'%media)
