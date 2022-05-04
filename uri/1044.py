valores = input().split()
x = int(valores[0])
y = int(valores[1])

if (x % y == 0) or (y % x == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
