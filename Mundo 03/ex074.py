from random import randint
valores = ()
for i in range(5):
    valores = valores + (randint(0, 10),)

print('Os valores sorteados foram:', *valores)

maior = menor = valores[0]
for valor in valores[1:]:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

    
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
