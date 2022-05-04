n = int(input())

while n  > 0:
    numero = int(input())
    x = 1
    total = 0

    while x < numero:
        if numero % x == 0:
            total += x
        x += 1

    if numero == total:
        print('%d eh perfeito' % numero)
    else:
        print('%d nao eh perfeito' % numero)

    n -= 1