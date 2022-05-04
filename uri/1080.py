pos_maior = 0
posicao = 0
lista = {}
while posicao < 100:
    valor = int(input())
    if(valor > pos_maior):
        pos_maior = valor
        lista[valor] = posicao
    posicao += 1
print(pos_maior)
print(lista[pos_maior]+1)