continuar = 'S'

jogadores = []

while continuar == 'S':
    jogador = {}
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    gols = []
    for part in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {part + 1}? '))
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador)
    
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('~'*45)

print('-=' * 30)

print(f'cod {"nome":<15} {"gols":<15} {"total":<3}')
print('-' * 40)

for i, j in enumerate(jogadores):
    print(f'{i:<3} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<3}')

print('-' * 40)
while True:
    opc = int(input('Mostrar dados de qual jogador? '))
    if opc == 999:
        break
    if opc >= 0 and opc < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}')
        for i, j in enumerate(jogadores[opc]['gols']):
            print(f'No jogo {i+1} fez {j}')
    else:
        print(f'Jogador {opc} não encontrado')
