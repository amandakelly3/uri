valor = int(input())

horas = valor // 3600
minutos = (valor % 3600) // 60
segundos = ((valor % 3600) % 60)

print("%d:%d:%d" % (horas, minutos, segundos))
