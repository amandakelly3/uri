horas = input().split()
hi = int(horas[0])
hf = int(horas[1])

if hi > hf:
    hora = 24 - (hi - hf)
    print('O JOGO DUROU %i HORA(S)' %hora)
elif hf > hi:
    hora = hf - hi
    print('O JOGO DUROU %i HORA(S)' %hora)
else:
    print('O JOGO DUROU 24 HORA(S)')
