valor = int(input())

anos = valor // 365
mes = (valor % 365) // 30
dia = ((valor % 365) % 30)

print("%d ano(s)" % anos)
print("%d mes(es)" % mes)
print("%d dia(s)" % dia)