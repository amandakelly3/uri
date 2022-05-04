n = int(input())
cont = 0
contout = 0

for a in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        cont += 1

    else:
        contout += 1

print('{} in'.format(cont))
print('{} out'.format(contout))