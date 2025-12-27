from random import randint
from time import sleep

print('''Suas opções:
1 - Pedra
2 - Papel
3 - Tesoura''')

usuario = int(input('Escolha qual você quer jogar: '))

if 0 < usuario <= 3:
    itens = ['Pedra', 'Papel', 'Tesoura']

    computador = randint(1, 3)
    print('JO')
    sleep(randint(1, 2))
    print('KEN')
    sleep(randint(1, 2))
    print('PO!!!')

    print('---' * 10)
    print(f'Computador escolheu: {itens[computador - 1]}')
    print(f'Jogador escolheu: {itens[usuario - 1]}')
    print('---' * 10)

    if computador == usuario:
        print('Empate')
    elif (computador == 1 and usuario == 2) or (computador == 2 and usuario == 3) or (computador == 3 and usuario == 1):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
else:
    print('Jogada Inválida!')
