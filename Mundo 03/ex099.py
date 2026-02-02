def maior(*num):
    print('-=' * 40)
    print('Analisando os valores passados...')

    total_numeros_informados = len(num)
    maior_numero_informado = 0
    if total_numeros_informados > 0:
        maior_numero_informado = num[0]

    for n in num:
        print(n, end=' ')
        if maior_numero_informado < n:
            maior_numero_informado = n

    print(f'Foram informados {total_numeros_informados} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero_informado}.')

maior(2, 3, 8, 5, 9, 10)

maior()
