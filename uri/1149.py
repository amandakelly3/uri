valores = input().split()
a = int(valores[0])
ultvalor = len(valores) -1
n = int(valores[ultvalor])
soma = 0

for x in range(0, n):
    soma += a + x
print(soma)