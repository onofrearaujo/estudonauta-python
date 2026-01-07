total_gasto = 0
total_mil = 0
cont = 0
menor_preco = 0

print('-' * 30)
print(f'{"SUPER BARATÃO":^30}')
print('-' * 30)

while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input(f'Qual é o preço do produto {produto}? R$ '))
    
    total_gasto += preco
    cont += 1
    if preco > 1000:
        total_mil += 1
        
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = produto
        
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
    if continuar == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto na compra foi de R$ {total_gasto:.2f}')
print(f'Temos {total_mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R$ {menor_preco:.2f}')
