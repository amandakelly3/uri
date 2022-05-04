n = int(input())
for a in range(n):
    x, y = map(int, input().split())
    soma = 0
    for b in range(x, x + (y * 2)):
        if b % 2:
            soma += b
    print(soma)