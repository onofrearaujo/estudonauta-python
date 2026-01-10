tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 
          'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 
          'Corinthians', 'Vasco da Gama', 'EC Vitória', 'Internacional', 'Ceará SC', 
          'Fortaleza', 'Juventude', 'Sport Recife')

print(f'Lista de times do Brasileirão: {tabela}')
print('-' * 30)
print('Os 5 primeiros são:')
for pos, time in enumerate(tabela[:5], start=1):
    print(f'{pos}º - {time}')
    
print('-' * 30)
print('Os 4 últimos são:')
for pos, time in enumerate(tabela[-4:], start=len(tabela) - 4 + 1):
    print(f'{pos}º - {time}')
    
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-' * 30)

time_procurar = 'Chapecoense'
if time_procurar in tabela:
    posicao_procurar = tabela.index(time_procurar)
    print(f'O time {time_procurar} está na {posicao_procurar + 1}ª posição.')
else:
    print(f'O time {time_procurar} não está na tabela.')
