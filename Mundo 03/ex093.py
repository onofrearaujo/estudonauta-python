jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

gols = []
for i in range(0, partidas):
   gol = int(input(f'Quantos gols na partida {i + 1}: ')) 
   gols.append(gol)
jogador['gols'] = gols

jogador['total'] = sum(gols)
print('~'*45)
print(jogador)
print('~'*45)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('~' * 45)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'  => Na partida {p+1}, fez {jogador["gols"][p]} gols.')
