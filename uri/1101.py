soma = 0
while True:
    m, n = map(int, input().split())
    maior = 0
    menor = 0
    if m <= 0 or n <= 0:
        break
    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m
    for x in range(menor, maior+1):
        print(x, end=' ')
        soma += x
    print('Sum={}' .format(soma))
    soma = 0