valores = ()
for i in range(4):
    n = int(input('Digite um valor: '))
    valores = valores + (n,)
    
print('Você digitou os valores:', *valores)
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
    
pares = ()
for valor in valores:
    if valor % 2 == 0:
        pares = pares + (valor,)
if len(pares) > 0:     
    print('Os valores pares digitados foram:', *pares)
else:
    print('Nenhum número par foi encontrado')
