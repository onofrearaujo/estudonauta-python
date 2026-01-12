valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)

    op = ' '
    while op not in 'SN':
        op = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break
print('~' * 40)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'Lista ordenada em forma descrecente {valores}')
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
