from ex107 import moeda
preco = float(input('Digite o preço: R$'))
porcento_aumentar = 10
porcento_diminuir = 13
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando {porcento_aumentar}%, temos {moeda.aumentar(preco, porcento_aumentar)}')
print(f'Reduzindo {porcento_diminuir}%, temos {moeda.diminuir(preco, porcento_diminuir)}')

