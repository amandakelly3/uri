n = int(input())
for i in range(n):
    entradas = input().split()
    nome = str(entradas[0])
    forca = int(entradas[1])
    if nome == "Thor":
        print('Y')
    else:
        print('N')