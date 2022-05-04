n = int(input())
while n > 0:
    numero = int(input())
    x = 1
    divisor = 0

    while x <= numero:
        if numero % x == 0:
            divisor += 1
        x += 1

    if divisor == 2:
        print('%d eh primo' % numero)
    else:
        print('%d nao eh primo' % numero)

    n -= 1