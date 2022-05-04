valores = input().split()
hi = int(valores[0])
mi = int(valores[1])
hf = int(valores[2])
mf = int(valores[3])

if hf == hi == mi == mf:
    horas, minutos = 24, 0
else:
    if mf >= mi:
        minutos = mf - mi
    else:
        minutos = 60 - abs(mf - mi)
        hf -= 1
    if hf >= hi:
        horas = hf - hi
    else:
        horas = 24 - abs(hf - hi)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))