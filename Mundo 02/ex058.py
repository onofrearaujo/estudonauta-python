from random import randint

computador = randint(0, 10)
print('Acabei de pensar em um número de 0 a 10. Tente Adivinhar')
palpites = 0
acertou = False

while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('O número sorteado é maior... Tente novamente!')
    else:
        print('O número sorteado é menor... Tente novamente!')

print(f'Você acertou o número do computador em {palpites} palpites. Parabéns!')

