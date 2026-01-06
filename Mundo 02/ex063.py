print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

termos = int(input('Quantos termos você quer mostrar? '))
atual = 0
proximo = 1
soma = 0
cont = 3

print(f'{atual} - {proximo}', end = ' - ')
while cont <= termos:
    soma = atual + proximo
    print(f'{soma}', end = ' - ')
    
    atual = proximo
    proximo = soma
    cont += 1
    
print('ACABOU')
