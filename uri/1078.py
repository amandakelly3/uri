n = int(input())
contador = 1
while n > 0:
    multi = contador * n
    print('{} x {} = {}' .format(contador, n, multi))
    contador += 1
    if contador == 11:
        break
