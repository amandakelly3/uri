x = int(input())
for a in range(x):
    n = int(input())
    if (n%2)==0 and n > 0:
        print('EVEN POSITIVE')
    if(n%2)==0 and n < 0:
        print('EVEN NEGATIVE')
    if(n%2)!=0 and n > 0:
        print('ODD POSITIVE')
    if(n%2)!=0 and n < 0:
        print('ODD NEGATIVE')
    if n == 0:
        print('NULL')