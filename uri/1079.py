n = int(input())
for a in range(n):
    x1, x2, x3 = map(float,input().split())
    media = (x1 * 2 + x2 * 3 + x3 * 5)/10
    print ('%.1f'%media)
