valores = []
while True:
    n = int(input('Digite um valor: '))
    
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break
    
print('~' * 40)
valores.sort()
print(f'Você digitou os valores {valores}')
