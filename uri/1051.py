renda = float(input())

if renda <= 2000.00:
    print('Isento')

elif renda > 2000.00 and renda <= 3000.00:
    isento = renda - 2000.00
    imposto = isento *8/100
    print('R$ %.2f' % imposto)

elif renda > 3000.00 and renda <= 4500.00:
    isento = renda - 3000.00
    imposto = isento * 18/100 + 80.00
    print('R$ %.2f' % imposto)

elif renda > 4500.00:
    isento = renda - 4500.00
    imposto = isento *28/100 + 350.00
    print('R$ %.2f' % imposto)
