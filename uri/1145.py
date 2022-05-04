valores = input().split()
x = int(valores[0])
y = int(valores[1])
count = 0
for i in range(1, y+1):
    if count < x-1:
        print(i, end=" ")
        count += 1
    else:
        print(i)
        count = 0