def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: Retorna o valor do fatorial de um número.
    """
    fat = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end='')

            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= i
    return fat
print(fatorial(2, True))

help(fatorial)
