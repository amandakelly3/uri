x = int(input())
y = int(input())
soma = 0
if x < y:
    maior = y
    menor = x
else:
    maior = x
    menor = y
for a in range(menor, maior +1):
    if a % 13 != 0:
        soma += a

print(soma)