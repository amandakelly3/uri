x = int(input())
z = int(input())
cont = 0
while z <= x:
    z = int(input())
total = x
while total < z:
    total += x + cont
    cont += 1
if z <= 0:
    print(cont)
else:
    print(cont + 1)