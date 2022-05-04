n = int(input())
soma = 0
maior = 0
menor = 0
for i in range(0, n):
    X, Y = map(int, input().split())
    if X > Y:
        maior = X
        menor = Y
    else:
        maior = Y
        menor = X
    for j in range(menor + 1, maior):
        if j % 2 != 0:
            soma += j
    print(soma)
    soma = 0