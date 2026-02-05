def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = input('Nome do jogador: ')
numero_gols = input('Número de Gols: ')

if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0
    
if nome_jogador.strip() == '':
    ficha(gols=numero_gols)
else:
    ficha(nome_jogador, numero_gols)
