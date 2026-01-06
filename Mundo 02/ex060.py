n = int(input('Digite um número para ver seu fatorial: '))

if n < 0:
    print('Não existe fatorial de número negativo!')
elif n == 0:
    print('0! = 1')
else:
    c = n
    fatorial = 1
    print(f'{n}! = ', end = '')
    
    while c > 0:
        fatorial *= c
        print(f'{c}', end='')
        c -= 1
        if c != 0:
            print(' x ', end = '')
    print(f' = {fatorial}')
