num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
1 - Para binário
2 - Para octal
3 - Para hexadecimal''')

op = int(input('Digite uma opção: '))


convertido = None
if op == 1:
    convertido = f'{num:b}'
    escolha = 'binário'
elif op == 2:
    convertido = f'{num:o}'
    escolha = 'octal'
elif op == 3:
    convertido = f'{num:X}'
    escolha = 'hexadecimal'
else:
    print('Opção inválida')

if convertido is not None:
    print(f'O número {num} convertido para {escolha} é igual a {convertido}')