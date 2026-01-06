cont = 0
soma = 0

maior = 0
menor = 0
resp = 'S'

while resp == 'S':
    n = int(input('Digite um número: '))
    soma += n
    
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / cont

print('~' * 30)
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('~' * 30)
    
    
