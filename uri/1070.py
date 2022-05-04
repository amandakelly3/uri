x = int(input())
contador = 0
while x > 0:
    if (x%2)==1:
        print(x)
        x += 2
        contador += 1
    else:
        x +=1
    if contador == 6:
        break
