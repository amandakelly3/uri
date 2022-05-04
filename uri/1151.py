n = int(input())
if n>0 and n<46:
    for i in range(n):
        if i == 0:
            a = i
            if(i==n-1):
                print(str(i))
            else:
                print(i,end=" ")
        elif i == 1:
            b = i
            if(i==n-1):
                print(str(i))
            else:
                print(i,end=" ")
        else:
            c=a+b
            if(i==n-1):
                print(str(c))
            else:
                print(c,end=" ")
            a,b=b,c