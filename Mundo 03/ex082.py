valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break

pares = []
impares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)


print('~' * 40)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
