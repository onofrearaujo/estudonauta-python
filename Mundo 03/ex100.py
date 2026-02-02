from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[n]}', end=' ')
    print('PRONTO!')

def somaPar(lista):
    soma_pares = 0

    for n in lista:
        if n % 2 == 0:
            soma_pares += n
    print(f'Somandos os valores pares de {lista}, temos {soma_pares}')

numeros = []
sorteia(numeros)
somaPar(numeros)
