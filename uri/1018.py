N = int(input())
n100 = N // 100
r = N % 100
n50 = r // 50
r = r % 50
n20 = r // 20
r = r % 20
n10 = r // 10
r = r % 10
n5 = r // 5
r = r % 5
n2 = r // 2
r = r % 2
n1 = r // 1
r = r % 1
print(str(N))
print(str(n100) + ' nota(s) de R$ 100,00')
print(str(n50) + ' nota(s) de R$ 50,00')
print(str(n20) + ' nota(s) de R$ 20,00')
print(str(n10) + ' nota(s) de R$ 10,00')
print(str(n5) + ' nota(s) de R$ 5,00')
print(str(n2) + ' nota(s) de R$ 2,00')
print(str(n1) + ' nota(s) de R$ 1,00')
