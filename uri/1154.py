total = 0
cont = 0
while True:
    idade = int(input())
    if idade > 0:
        total += idade
        cont += 1

    else:
        media = total / cont
        print('%.2f' %media)
        break