n = int(input())
for a in range(n):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])
    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print('%1.1f' % divisao)