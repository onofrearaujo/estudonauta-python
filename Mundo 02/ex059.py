from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

op = 0
while op != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    
    print('=' * 10)
    op = int(input('Escolha a opção: '))
    print(' ')
    if op == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os dois números são iguais ({n1}, {n2})')
    elif op == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Digite uma opção válida!')
    print(' ')
