preco_produto = float(input('Digite o preço do produto: '))

print('1 - A vista dinheiro/cheque')
print('2 - A vista no cartão')
print('3 - Parcelar')

forma_pagamento = int(input('Escolha a forma de pagamento: '))

pagamento = None

if forma_pagamento == 1:
    pagamento = preco_produto - 10/100 * preco_produto
elif forma_pagamento == 2:
    pagamento = preco_produto - 5/100 * preco_produto
elif forma_pagamento == 3:
    parcelas = int(input('Em quantas parcelas dividir: '))

    if parcelas > 0 and parcelas <= 2:
        pagamento = preco_produto
    elif 3 <= parcelas <= 12:
        pagamento = preco_produto + 20/100 * preco_produto
    else:
        print('Parcelas invalida! ')
else:
    print('Essa forma de pagamento não existe')

if pagamento is not None:
    print(f'Você irá pagar {pagamento:.2f} no produto que custa {preco_produto:.2f}')