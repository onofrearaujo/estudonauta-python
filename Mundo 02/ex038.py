n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O PRIMEIRO número ({n1}) é MAIOR que o SEGUNDO ({n2})')
elif n2 > n1:
    print(f'O SEGUNDO número ({n2}) é MAIOR que o PRIMEIRO ({n1})')
else:
    print('Não existe valor maior, os dois são iguais')
