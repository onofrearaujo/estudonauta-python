from random import randint
pontos = 0
while True:
    while True:
        escolha = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
        if escolha in 'PI':
            break
        
    jogador = int(input('Digite um valor: '))
    
    computador = randint(0, 10)
    
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end = '')
    
    if soma % 2 == 0:
        resultado = 'P'
        print('DEU PAR')
    else:
        resultado = 'I'
        print('DEU IMPAR')
        
    if escolha == resultado:
        print('VOCÊ GANHOU!')
        pontos += 1
    else:
        print('VOCÊ PERDEU!')
        break
        
    print('Vamos jogar novamente...')
        
print(f'GAME OVER! Você venceu {pontos} VEZES.')
