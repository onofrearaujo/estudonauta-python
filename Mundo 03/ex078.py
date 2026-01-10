valores = []
maior = menor = 0

for cont in range(5):
    n = int(input(f'Digite um valor para a Posição {cont}: '))
    valores.append(n)
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('=-' * 40)

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições:', end='')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f' {pos}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f' {pos}...', end='')
print()
