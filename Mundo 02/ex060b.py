n = int(input('Digite um número para ver seu fatorial: '))


if n < 0:
    print('Não existe fatorial de número negativo!')
elif n == 0:
    print('0! = 1')
else:
    fatorial = 1
    print(f'{n}! = ', end = '')
    for i in range(n, 0, -1):
        fatorial *= i
        print(f'{i}', end = '')
        if i != 1:
            print(' x ', end = '')
    print(f' = {fatorial}')
