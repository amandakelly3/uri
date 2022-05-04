x = int(input())
y = int(input())
cont = 0
for a in range(y+1,x):
    if (a%2)!=0:
        cont += a
print(cont)