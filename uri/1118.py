soma = 0
cont = 0
codigo = 0
while True:
    n = float(input())
    if 0 <= n <= 10:
        cont += 1
        soma += n
    else:
        print('nota invalida')
    if cont == 2:
        print('media = {:.2f}'.format(soma / 2))
        cont = soma = codigo = 0
        while codigo != 1:
            print('novo calculo (1-sim 2-nao)')
            codigo = int(input())
            if codigo == 2:
                break
        if codigo == 2:
            break