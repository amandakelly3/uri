grenais = 0
empates = 0
inter = 0
gremio = 0
while True:
    gols = input().split()
    gol_inter = int(gols[0])
    gol_gremio = int(gols[1])
    grenais += 1
    if gol_inter == gol_gremio:
        empates += 1
    if gol_inter > gol_gremio:
        inter += 1
    else:
        gremio += 1


    print('Novo grenal (1-sim 2-nao)')
    codigo = int(input())
    if codigo == 2:
        break

print('%d grenais' %grenais)
print('Inter:%d' %inter)
print('Gremio:%d' %gremio)
print('Empates:%d' %empates)
if gremio < empates > gremio:
    print('Nao houve vencedor')
if gremio < inter > empates:
    print('Inter venceu mais')
else:
    print('Gremio venceu mais')