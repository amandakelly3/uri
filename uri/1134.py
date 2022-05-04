alcool = gasolina = diesel = 0
while True:
    codigo = int(input())
    if 1 > codigo > 4:
        codigo = int(input())
    else:
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
        elif codigo == 4:
            break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))