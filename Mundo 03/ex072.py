extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        print(f'O número {n} por extenso é {extenso[n]}')
        print('-' * 30)
        while True:
            escolha = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
            if escolha in 'SN':
                break
        if escolha == 'N':
            break
    else:
        print('Tente novamente. ', end='')
        
