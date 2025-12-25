preco = float(input('Qual é o preço do produto? R$'))

com_desconto = preco - (5 / 100 * preco)

print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${com_desconto:.2f}')
