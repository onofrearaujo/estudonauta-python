from time import sleep
from random import randint
print('-=' * 30)
print(f"{'JOGO NA MEGA SENA':^60}")
print('-=' * 30)
quantidade_jogos = int(input('Quantos jogos você deseja quer que eu sorteie? '))

jogos = []

print(f"{f' SORTEANDO {quantidade_jogos} JOGOS ':=^60}")
for c in range(quantidade_jogos):
    jogo = []
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    jogos.append(jogo)
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print(f"{' < BOA SORTE! > ':=^60}")
