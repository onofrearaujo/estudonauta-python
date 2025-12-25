n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if maior < n3:
    maior = n3
    

if n3 < menor:
    menor = n3


print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
