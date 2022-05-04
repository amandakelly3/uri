n = int(input())

coelho = 0
sapo = 0
rato = 0
total = 0

while n > 0:
    [numero, animal] = input().split()

    if animal == 'C':
        coelho += int(numero)
    elif animal == 'S':
        sapo += int(numero)
    elif animal == 'R':
        rato += int(numero)

    total += int(numero)
    n -= 1

print('Total: %d cobaias' %total)
print('Total de coelhos: %d' %coelho)
print('Total de ratos: %d' %rato)
print('Total de sapos: %d' %sapo)
print('Percentual de coelhos: %.2f %%' %(coelho * 100 / total))
print('Percentual de ratos: %.2f %%' %(rato * 100 / total))
print('Percentual de sapos: %.2f %%' %(sapo * 100 / total))