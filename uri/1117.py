cont = 0
total = 0
while cont < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        cont += 1
        total += nota
    else:
        print('nota invalida')


print('media = %.2f' %(total/2))