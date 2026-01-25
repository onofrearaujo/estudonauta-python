from random import randint
jogadores = {}

print('Valores sorteados')

for c in range(1, 5):
    sorteado = randint(1, 6)
    jogador = "jogador"+str(c)
    print(f'O {jogador} tirou {sorteado}')
    jogadores[jogador] = sorteado
print('~'*30)
for p, i in enumerate(sorted(jogadores, key=jogadores.get, reverse=True), start=1):
    print(f'{p}º lugar: {i} com {jogadores[i]}')
